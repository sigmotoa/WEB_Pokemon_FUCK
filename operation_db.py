from db import SessionDep
from model import PokemonBase, PokemonID


def create_pokemon_db(pokemon, session: SessionDep) -> PokemonID:
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)

    return pokemon
