from fastapi import FastAPI, HTTPException, Request
from sqlmodel import Session
from starlette.responses import JSONResponse
from db import create_all_tables, SessionDep

from model import PokemonBase, PokemonID, PokemonUpdate
from operation_csv import createPokemon, showPokemons, showPokemon, updatePokemon, deletePokemon
from operation_db import create_pokemon_db, find_one_pokemon

app = FastAPI(lifespan=create_all_tables)



##def save_csv(pokemon:PokemonBase):


##pokedex = []

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": f"{exc.detail} Ooops. TODOOO fallo"},)


@app.post("/pokemon", response_model=PokemonID, status_code=201)
async def catch_pokemon(pokemon: PokemonBase, session:SessionDep):
     return create_pokemon_db(pokemon, session)
    ##pokedex.append(pokemon)




@app.get("/pokemon", response_model=list[PokemonID])
async def show_all_pokemon():
    pokemons = showPokemons()
    return pokemons


@app.get("/pokemon/{id}", response_model=PokemonID)
async def show_pokemon(id: int, session:SessionDep):
    pokemon = find_one_pokemon(id, session)
    if not(pokemon):
        raise HTTPException(status_code=404, detail="Pokemon has not been caught")
    return pokemon

@app.patch("/pokemon/{id}", response_model=PokemonID)
async def update_pokemon(id: int, pokemon_update: PokemonUpdate):
    updated = updatePokemon(id, pokemon_update.model_dump(exclude_unset=True))
    if not (updated):
        raise HTTPException(status_code=404, detail="Pokemon has not been evolved")
    return updated

@app.delete("/pokemon/{id}", response_model=PokemonBase)
async def delete_pokemon(id: int):
    deleted = deletePokemon(id)
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