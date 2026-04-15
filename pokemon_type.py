from enum import Enum, auto

class Tipo(str,Enum):
    HIERBA = "hierba"
    FUEGO = "fuego"
    ELECTRICO = "electrico"
    NORMAL = "normal"
