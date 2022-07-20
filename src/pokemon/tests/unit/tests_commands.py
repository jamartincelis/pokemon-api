from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from pokemon.models import Pokemon
from pokemon.tests.factories.pokemon_factories import RatataFactory

class EvolutionChainTest(TestCase):

    def test_command_without_id(self):
        out = StringIO()
        call_command('evolution_chain', stdout=out)
        self.assertIn("The evolution chain 'id' it's required.", out.getvalue())

    def test_query_invalid_pokemon_object(self):
        with self.assertRaises(Pokemon.DoesNotExist) as err:
            Pokemon.objects.get(name="rattata")
        self.assertEqual(
            str("Pokemon matching query does not exist."),
            str(err.exception)
        )   

    def test_existing_ratata_evolution_chain(self):
        RatataFactory() # creo el objeto ratata
        out = StringIO()
        call_command('evolution_chain', '--id=7', stdout=out)
        self.assertIn('The evolution chain for pokemon rattata already exists in the database.', out.getvalue())

    def test_ratata_evolution_chain(self):
        out = StringIO()
        call_command('evolution_chain', '--id=7', stdout=out)
        self.assertIn('Successfully load evolution chain', out.getvalue())
        Pokemon.objects.get(name="rattata")