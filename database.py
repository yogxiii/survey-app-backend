from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import os

SQLALCHEMY_DATABASE_URL = 'sqlite:///./survey_app.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})


## creating schema while initiating app
sql_scripts = os.listdir("sql_scripts")
with engine.connect() as con:
    for scripts in sql_scripts:
        with open(f"sql_scripts/{scripts}") as file:
            query = text(file.read())
            con.execute(query)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()