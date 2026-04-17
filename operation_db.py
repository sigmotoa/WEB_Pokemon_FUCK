from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from model import PokemonBase, PokemonID


def create_pokemon_db(pokemon:PokemonBase, session: Session):
    new=PokemonID.model_validate(pokemon)
    session.add(new)
    session.commit()
    session.refresh(new)
    return new

def find_one_pokemon_db(pokemon_id:int, session: Session):
    try:
        return session.get_one(PokemonID, pokemon_id)
    except NoResultFound:
        return None

def all_pokemon_db(session: Session):
    #return session.query(PokemonID).all()
    statement = select(PokemonID)
    results = session.exec(statement)
    return results