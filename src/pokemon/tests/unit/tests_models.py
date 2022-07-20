from django.test import TestCase
from pokemon import MODULE_SETTINGS as settings
from pokemon.models import Pokemon
from pokemon.tests.factories.pokemon_factories import RatataFactory
from pokemon.tests import helpers
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

class PokemonTestCase(TestCase):
    def setUp(self):
        self.pokemon_factory = RatataFactory() # create factory object
        
    def test_pokemon(self):
        """
        Pokemon example
        """
        pokemon = Pokemon.objects.get(name="rattata")
        self.assertEqual(pokemon.name, self.pokemon_factory.name)
        self.assertEqual(pokemon.details, self.pokemon_factory.details)

    def test_unique_constraint_pokemon_name(self):
        with self.assertRaises(IntegrityError) as err:
            Pokemon.objects.create(
                name="rattata", 
                details=helpers.load_json(settings['POKEMON_JSON_EXAMPLE'])
            )
        self.assertEqual(
            str("UNIQUE constraint failed: pokemon.name"),
            str(err.exception)
        )   

    def test_max_length_constraint_pokemon_name(self):
        with self.assertRaises(ValidationError) as err:
            name = "a"*51
            p = Pokemon(
                name=name, 
                details=helpers.load_json(settings['POKEMON_JSON_EXAMPLE'])
            )
            p.full_clean()
            p.save()

        self.assertEqual(
            str({'name': ['Ensure this value has at most 50 characters (it has 51).']}),
            str(err.exception)
        )

    def test_null_constraint_pokemon_name(self):
        with self.assertRaises(IntegrityError) as err:
            Pokemon.objects.create(
                name=None, 
                details=helpers.load_json(settings['POKEMON_JSON_EXAMPLE'])
            )
        self.assertEqual(
            "NOT NULL constraint failed: pokemon.name",
            str(err.exception)
        )