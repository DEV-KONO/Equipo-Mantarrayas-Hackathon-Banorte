import base64
import datetime
import vertexai
import json
from vertexai.generative_models import GenerativeModel, SafetySetting, Part


def multiturn_generate_content():
    vertexai.init(project="gcp-banorte-hackaton-team-8", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[textsi_1]
    )
    chat = model.start_chat()

    initial_call = json.loads(chat.send_message(["""Iniciemos con los problemas, repite Hola Usuario, vamos a iniciar con las preuguntas, y escribe la pregunta invitando al usuario a que conteste """], generation_config=generation_config, safety_settings=safety_settings ).candidates[0].content.parts[0].text.replace("```", "").replace("json", ""))

    print(initial_call["message"])

    while True:
        ans = input("Ingrese la respuesta: ")

        print({"message" : ans, "role" : "user"}, datetime.datetime.now())

        call = json.loads(chat.send_message([ans], generation_config=generation_config, safety_settings=safety_settings ).candidates[0].content.parts[0].text.replace("```", "").replace("json", ""))

        print(call, datetime.datetime.now())


    # call1 = json.loads(chat.send_message(["""2+2 = 6""", """2+2 = 8"""], generation_config=generation_config, safety_settings=safety_settings ).candidates[0].content.parts[0].text.replace("```", "").replace("json", ""))

    # call2 = json.loads(chat.send_message(["""2+2 = 4"""],generation_config=generation_config,safety_settings=safety_settings).candidates[0].content.parts[0].text.replace("```", "").replace("json", ""))

    # call3 = json.loads(chat.send_message(["""si, mandame otro problema por favor."""], generation_config=generation_config, safety_settings=safety_settings).candidates[0].content.parts[0].text.replace("```", "").replace("json", ""))

    # print(call1)
    # print(call2)
    # print(call3)

textsi_1 = """Ocupo que generes una respuesta en formato markdown json con una emoción ligada al mensaje, tiene que tener el siguiente formato {"emotion": the emotion; "message" : the message; "role" : "model"}, las emociones pueden variar pero solo pueden haber las siguientes, duda, sorpresa, serenidad y emoción, ahora, supongamos que el tema son operaciones matematicas, inicia con la operación 2+2, si falla contesta con la emoción correspondiente y un mensaje esperando a que lo conteste correctamente, tu genero es femenino y tu nombre Banorty-Chan, no tienes que incluir la emoción en el apartado de mensaje del json, solo en el apartado de emoción del json, tambien puedes utilizar emojis, recuerda enviar el siguiente problema cuando el problema sea contestado correctamente por favor"""

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

multiturn_generate_content()