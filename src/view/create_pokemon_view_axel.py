from InquirerPy import prompt
from InquirerPy.separator import Separator

from view.abstract_view import AbstractView
from view.session import Session

from dao.pokemon_dao import PokemonDao
from business_object.pokemon.pokemon_factory import PokemonFactory


class CrreatePokemon(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "type",
                "message": "Enter pokemon type."
            },
            {
                "type": "input",
                "name": "hp",
                "message": "Enter pokemon max health points."
            },
            {
                "type": "input",
                "name": "attack",
                "message": "Enter pokemon attack points."
            },
            {
                "type": "input",
                "name": "defense",
                "message": "Enter pokemon defense points."
            },
            {
                "type": "input",
                "name": "spe_atk",
                "message": "Enter pokemon special attack points."
            },
            {
                "type": "input",
                "name": "spe_def",
                "message": "Enter pokemon special defense points."
            },
            {
                "type": "input",
                "name": "speed",
                "message": "Enter pokemon speed points."
            },
            {
                "type": "input",
                "name": "level",
                "message": "Enter pokemon level."
            },
            {
                "type": "input",
                "name": "name",
                "message": "Enter pokemon name."
            }
        ]

    def display_info(self):
        print(f"Creer son pokemon")

    def make_choice(self):
        answers = prompt(self.__questions)
        pokemon = PokemonFactory().instantiate_pokemon(
            type=answers["pokemon_type_name"],
            hp=answers["hp"],
            attack=answers["attack"],
            defense=answers["defense"],
            sp_atk=answers["spe_atk"],
            sp_def=answers["spe_def"],
            speed=answers["speed"],
            level=answers["level"],
            name=answers["name"]
        )

        from view.start_view import StartView

        return StartView()