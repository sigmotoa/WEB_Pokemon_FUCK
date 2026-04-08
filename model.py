from pydantic import BaseModel, Field
from enum import Enum, auto

class Tipo(str,Enum):
    HIERBA = "hierba"
    FUEGO = "fuego"
    ELECTRICO = "electrico"
    NORMAL = "normal"

class PokemonBase(BaseModel):
    name: str = Field(..., min_length=4, max_length=50)
    tipo: Tipo = Field(default=Tipo.NORMAL)
    level: int = Field(..., gt=0, le=100,default=40)

class PokemonID(PokemonBase):
    id: int = Field(..., gt=0)

class PokemonUpdate(PokemonBase):
    level: int = Field(..., gt=0, le=100)
