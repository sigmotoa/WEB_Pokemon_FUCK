from fastapi import FastAPI, HTTPException
from model import PokemonBase
import csv
import os

app = FastAPI()



##def save_csv(pokemon:PokemonBase):


##pokedex = []

@app.post("/pokemon")
async def catch_pokemon(pokemon: PokemonBase):
    ##pokedex.append(pokemon)
    save_csv(pokemon)
    return {"Pokemon capturado": PokemonResponse(**pokemon.model_dump())}


@app.get("/pokemon", response_model=list[PokemonResponse])
async def show_all_pokemon():
    pokemons=[]
    with open(CSV_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for p in reader:
            pokemons.append(PokemonBase(**p))
    return pokemons


@app.get("/pokemon/{id}", response_model=PokemonResponse)
async def show_pokemon(id: int):
    with open(CSV_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for p in reader:
            if int(p["id"]) == id:
                return PokemonResponse(**p)
    raise HTTPException(status_code=404, detail="Pokemon no capturado aún")


@app.get("/")
async def root():
    return {"message": "Hello in Pycharm"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
