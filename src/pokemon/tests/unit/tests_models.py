from django.test import TestCase
from pokemon import MODULE_SETTINGS as settings
from pokemon.models import Pokemon
from pokemon.tests.factories.pokemon_factories import RatataFactory
from pokemon.tests import helpers

class PokemonTestCase(TestCase):
    def setUp(self):

        self.pokemon_factory = RatataFactory() # with factory
        Pokemon.objects.create( # create pokemon in database
            name="rattata", 
            details=helpers.load_json(settings['POKEMON_JSON_EXAMPLE'])
        )
        
    def test_pokemon(self):
        """
        Pokemon example
        """
        pokemon = Pokemon.objects.get(name="rattata")
        self.assertEqual(pokemon.name, 'rattata')
        self.assertEqual(pokemon.details, self.pokemon_factory.details)