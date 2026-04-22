import os

from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated
from fastapi import Depends, FastAPI
from dotenv import load_dotenv

load_dotenv()

neon_url_db = os.getenv("DATABASE_URL")


sqlite_name = "pokemondb.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(neon_url_db)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
