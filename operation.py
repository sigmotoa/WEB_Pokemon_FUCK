import os
import csv
from typing import Optional
from model import *

CSV_FILE = "pokedex.csv"
columns = ["id","name", "tipo","level"]


def newID():
    try:
        with open(CSV_FILE, mode="r",newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            max_id=max(int(row['id']) for row in reader)
            return max_id+1
    except (FileNotFoundError, csv.Error):
        return 1


def savePokemonID(pokemon:PokemonID):
    pokedex_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a+", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        if not pokedex_exists:
            writer.writeheader()
        writer.writerow(pokemon.model_dump())


def createPokemon(pokemon: PokemonBase):
    id = newID()
    new_pokemon = PokemonID(id=id, **pokemon.model_dump())
    savePokemonID(new_pokemon)
    return new_pokemon


def showPokemons():
    with open(CSV_FILE) as csvfile:
        reader = csv.DictReader(csvfile)
        return [PokemonID(**row) for row in reader]


def showPokemon(id:int):
    with open (CSV_FILE) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['id']) == id:
                return PokemonID(**row)


