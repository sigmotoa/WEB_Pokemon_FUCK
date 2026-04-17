from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from model import PokemonBase, PokemonID, PokemonUpdate


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

def updated_pokemon_db(pokemon_id:int,new_pokemon:PokemonUpdate, session: Session):
    pokemon = find_one_pokemon_db(pokemon_id, session)
    if pokemon is None:
        return None
    pokemon_update = new_pokemon.model_dump(exclude_unset=True)
    pokemon.sqlmodel_update(pokemon_update)
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)

    return pokemon
