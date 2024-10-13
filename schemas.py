from re import S
from pydantic import BaseModel

class Schema_User_Mail(BaseModel):
    mail: str

class Schema_User_Message(BaseModel):
    mail: str
    message: str

class Schema_User_Login(BaseModel):
    mail: str
    username: str
    password: str

class Schema_User_Register(BaseModel):
    mail: str
    username: str
    password: str
    conf_pass: str