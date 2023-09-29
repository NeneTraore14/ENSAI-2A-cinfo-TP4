from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from dao.pokemon_dao import PokemonDao

class StartView(AbstractView):
    def __init__(self):
        self.__dao = PokemonDao()
        choix = [pokemon.name for pokemon in dao.find_all(limit=30)] + ["Menu"]
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Voici une liste de pokemons",
                "choices": choix
            }
        ]

    def display_info(self):
        print("Voici une liste non exhaustive de pokemons.")

    def make_choice(self):
        reponse = prompt(self.__questions)

        if reponse["choix"] == "Menu":
            from view.start_view import StartView

            return StartView()
        else:
            from view.pokemon_details_view import PokemonDetailsView

            return PokemonDetailsView(reponse["choix"])
