from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from sqlmodel import Session
from starlette.responses import JSONResponse
from db import create_all_tables, SessionDep

from utils import (save_img)
from model import PokemonBase, PokemonID, PokemonUpdate
from operation_csv import createPokemon, showPokemons, showPokemon, updatePokemon, deletePokemon
from operation_db import create_pokemon_db, find_one_pokemon_db, all_pokemon_db, updated_pokemon_db, kill_one_pokemon_db

app = FastAPI(lifespan=create_all_tables)



##def save_csv(pokemon:PokemonBase):


##pokedex = []

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": f"{exc.detail} Ooops. TODOOO fallo"},)


@app.post("/image")
async def image_save(file: UploadFile = File(...)):
    path = save_img(file)
    return {"saved at": path}


@app.post("/pokemon", response_model=PokemonID, status_code=201)
async def catch_pokemon(pokemon: PokemonBase, session:SessionDep):
     return create_pokemon_db(pokemon, session)
    ##pokedex.append(pokemon)




@app.get("/pokemon", response_model=list[PokemonID])
async def show_all_pokemon(session:SessionDep):
    pokemons = all_pokemon_db(session)
    return pokemons


@app.get("/pokemon/{id}", response_model=PokemonID)
async def show_pokemon(id: int, session:SessionDep):
    pokemon = find_one_pokemon_db(id, session)
    if not(pokemon):
        raise HTTPException(status_code=404, detail="Pokemon has not been caught")
    return pokemon

@app.patch("/pokemon/{id}", response_model=PokemonID)
async def update_pokemon(id: int, pokemon_update: PokemonUpdate, session:SessionDep):
    updated = updated_pokemon_db(id, pokemon_update, session)
    if not (updated):
        raise HTTPException(status_code=404, detail="Pokemon has not been evolved")
    return updated

@app.delete("/pokemon/{id}", response_model=PokemonBase)
async def delete_pokemon(id: int, session:SessionDep):
    deleted = kill_one_pokemon_db(id, session)
    if not (deleted):
        raise HTTPException(status_code=404, detail="Pokemon has not been caught")
    return deleted

'''

@app.get("/")
async def root():
    return {"message": "Hello in Pycharm"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
'''