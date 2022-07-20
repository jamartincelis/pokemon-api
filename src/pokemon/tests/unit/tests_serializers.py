from django.test import TestCase
from pokemon.tests.factories.pokemon_factories import RatataFactory
from pokemon.serializers import PokemonSerializer
from pokemon.tests import helpers
from pokemon import MODULE_SETTINGS as settings

class PokemonTestCase(TestCase):
    def setUp(self):
        self.pokemon_factory = RatataFactory() # create factory object
        
    def test_empty_pokemon_serializer(self):
        """
        Test empty pokemon serializer.
        """
        serializer = PokemonSerializer(data={})
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(set(serializer.errors.keys()), set(['name', 'details']))
        errors = "{'name': [ErrorDetail(string='This field is required.', code='required')], 'details': [ErrorDetail(string='This field is required.', code='required')]}"
        self.assertEqual(str(serializer.errors), errors)

    def test_serialize_valid_pokemon_object(self):
        """
        Test serialize pokemon object.
        """
        serializer = PokemonSerializer(self.pokemon_factory)
        data = serializer.data
        self.assertEqual(serializer.data, helpers.load_json(settings['POKEMON_SERIALIZER_EXAMPLE']))
        self.assertTrue('id' in str(data))
        self.assertTrue('name' in str(data))
        self.assertTrue('height' in str(data))
        self.assertTrue('weight' in str(data))
        self.assertTrue('evolutions' in str(data))
        self.assertTrue('stats' in str(data))
        self.assertEqual(len(data['stats']), 6)

    def test_serialize_invalid_pokemon_data_name(self):
        """
        Test empty pokemon serializer.
        """
        name = "a"*51
        data = {
            'name': name,
            'details': self.pokemon_factory.details

        }
        errors = "{'name': [ErrorDetail(string='Ensure this field has no more than 50 characters.', code='max_length')]}"
        serializer = PokemonSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(str(serializer.errors), errors)

    def test_serialize_valid_pokemon_data_name(self):
        """
        Test empty pokemon serializer.
        """
        name = "a"*50
        data = {
            'name': name,
            'details': self.pokemon_factory.details

        }
        serializer = PokemonSerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)
        validated_data = serializer.validated_data
        self.assertTrue('id' in str(validated_data))
        self.assertTrue('name' in str(validated_data))
        self.assertTrue('height' in str(validated_data))
        self.assertTrue('weight' in str(validated_data))
        self.assertTrue('evolutions' in str(validated_data))
        self.assertTrue('stats' in str(validated_data))
        self.assertEqual(len(validated_data['details']['stats']), 6)      

        
