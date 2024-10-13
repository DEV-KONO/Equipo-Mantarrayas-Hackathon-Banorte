import os
import datetime
from dotenv import load_dotenv
from urllib.parse import quote
from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String, create_engine
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, relationship


load_dotenv()

DB_PASS = os.getenv("DB_PASS")

# postgres_url = "postgresql+psycopg2://postgres:%s@localhost:5432/hackathon_banorte_equipo_mantarrayas" % quote(DB_PASS)

# engine = create_engine(postgres_url)

engine = create_engine("sqlite:///C:\\Users\\samue\\Documents\\GitHub\\Equipo-Mantarrayas-Hackathon-Banorte\\hackathon_banorte_equipo_mantarrayas.db")

Base = declarative_base()

class Chat_History(Base):
    __tablename__ = "Chat_History"

    id = Column(Integer, primary_key=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    json_entry = Column(JSON, nullable=False)

    user_mail = Column(ForeignKey("users.mail"))
    _user = relationship("Users", back_populates="chat_hist")

class Users(Base):
    __tablename__ = "users"

    mail = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)

    chat_hist = relationship(Chat_History)

Base.metadata.create_all(engine)