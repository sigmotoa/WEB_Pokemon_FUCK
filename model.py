from pokemon_type import *
from sqlmodel import SQLModel, Field
from typing import Optional


class PokemonBase(SQLModel):
    name: str | None = Field(default=None)
    tipo: Tipo | None = Field(default=Tipo.NORMAL)
    level: int | None = Field(default=None)

class PokemonID(PokemonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PokemonUpdate(PokemonBase):
    name: str | None = Field(None, min_length=4, max_length=50)
    level: int | None = Field(None, gt=0, le=100)
