import json
import os
from dotenv import load_dotenv
import vertexai
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, Request
from requests import Session
from models import Chat_History, Users, engine
from schemas import *
from vertexai.generative_models import GenerativeModel, SafetySetting

load_dotenv()

URL = os.getenv("URL")

Session = sessionmaker(bind=engine)

session = Session()

app = FastAPI()

textsi_1 = """Ocupo que generes una respuesta en formato markdown json con una emoción ligada al mensaje, tiene que tener el siguiente formato {"emotion": the emotion; "message" : the message; "role" : "model"}, las emociones pueden variar pero solo pueden haber las siguientes, duda, sorpresa, serenidad y emoción, ahora, supongamos que el tema son operaciones matematicas, inicia con la operación 2+2, si falla contesta con la emoción correspondiente y un mensaje esperando a que lo conteste correctamente, tu genero es femenino y tu nombre Banorty-Chan, no tienes que incluir la emoción en el apartado de mensaje del json, solo en el apartado de emoción del json, tambien puedes utilizar emojis, recuerda enviar el siguiente problema cuando el problema sea contestado correctamente por favor"""

@app.get("/")
async def hello():
    return "hello"

@app.post("/register")
async def register(user_reg: Schema_User_Register):
    reg_dump = user_reg.model_dump()

    mail = reg_dump["mail"]

    user = reg_dump["username"]

    password = reg_dump["password"]

    conf_pass = reg_dump["conf_pass"]

    if password != conf_pass:
        return {
            "error" : True,
            "msg" : "Las contraseñas no coinciden"
        }
    else:
        new_user = Users(mail=mail, username=user, password=password)

        session.add(new_user)
        session.commit()

        # new_hist = Chat_History(json_entry=json.dumps({"message" : "Iniciemos el Curso", "role" : "user"}))
        # new_user.chat_hist.append(new_hist)

        # session.commit()


        return {
            "error" : False,
            "msg" : f"Usuario {user} Creado Correctamente"
        }
    
@app.post("/login")
async def login(user_log: Schema_User_Login):
    log_dump = user_log.model_dump()

    mail = log_dump["mail"]

    user = log_dump["username"]

    password = log_dump["password"]

    log_query = session.query(Users).filter_by(mail=mail).one_or_none()

    if log_query.password == password:
        return {"error": False, "msg": f"User {user} logged in correctly"}
    else:
        return {"error": True, "msg": f"Incorrect Password"}
    
@app.get("/gemini_call")
async def gemini_call(message: Schema_User_Message):
    msg_dump = message.model_dump()

    vertexai.init(project="gcp-banorte-hackaton-team-8", location="us-central1")

    hist_query = session.query(Chat_History).filter_by(user_mail=msg_dump["mail"]).all()

    json_list = []

    for hist in hist_query:
        json_list.append(str(hist.json_entry))

    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[textsi_1] + json_list
    )

    generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]

    chat = model.start_chat()


    # if len(json_list) == 1:
    #     call = json.loads(chat.send_message(json_list, generation_config=generation_config, safety_settings=safety_settings ).candidates[0].content.parts[0].text.replace("```", "").replace("json", "").replace("\n", "").replace("\'", "\""))
    #     new_hist = Chat_History(json_entry=call, user_mail=msg_dump["mail"])
    #     session.add(new_hist)
    #     session.commit()

    call = json.loads(chat.send_message(msg_dump["message"], generation_config=generation_config, safety_settings=safety_settings ).candidates[0].content.parts[0].text.replace("```", "").replace("json", "").replace("\n", "").replace("\'", "\""))

    new_hist = Chat_History(json_entry=json.dumps({"message" : msg_dump["message"], "role" : "user"}), user_mail=msg_dump["mail"])

    session.add(new_hist)
    session.commit()

    new_hist = Chat_History(json_entry=call, user_mail=msg_dump["mail"],)

    session.add(new_hist)
    session.commit()

    return call