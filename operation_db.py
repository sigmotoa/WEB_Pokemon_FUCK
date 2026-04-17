from sqlalchemy.exc import NoResultFound
from sqlmodel import Session
from model import PokemonBase, PokemonID


def create_pokemon_db(pokemon:PokemonBase, session: Session):
    new=PokemonID.model_validate(pokemon)
    session.add(new)
    session.commit()
    session.refresh(new)
    return new

def find_one_pokemon(pokemon_id:int, session: Session):
    try:
        return session.get_one(PokemonID, pokemon_id)
    except NoResultFound:
        return None
