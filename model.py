from pydantic import BaseModel, Field
from pokemon_type import *
from typing import Optional


class PokemonBase(BaseModel):
    name: str = Field(..., min_length=4, max_length=50)
    tipo: Tipo = Field(default=Tipo.NORMAL)
    level: int = Field(..., gt=0, le=100)

class PokemonID(PokemonBase):
    id: int = Field(..., gt=0)

class PokemonUpdate(PokemonBase):
    name: str | None = Field(None, min_length=4, max_length=50)
    level: int | None = Field(None, gt=0, le=100)
