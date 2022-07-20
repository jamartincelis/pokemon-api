from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from pokemon.models import Pokemon
from pokemon.tests.factories.pokemon_factories import RatataFactory
from django.urls import reverse
from rest_framework import status

class EvolutionChainFuncionalTest(TestCase):

    def test_ratata_evolution_chain(self):
        pokemon_name = "rattata"

        out = StringIO()
        call_command('evolution_chain', '--id=7', stdout=out)
        self.assertIn('Successfully load evolution chain', out.getvalue())

        response = self.client.get(
            reverse('detail',kwargs={'name':pokemon_name})
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 6)
        self.assertEqual(data['name'], pokemon_name)
        self.assertTrue('id' in str(data))
        self.assertTrue('name' in str(data))
        self.assertTrue('height' in str(data))
        self.assertTrue('weight' in str(data))
        self.assertTrue('evolutions' in str(data))
        self.assertTrue('stats' in str(data))
        self.assertEqual(len(response.json()['stats']), 6)

    def test_bulbasaur_evolution_chain(self):
        pokemon_name = "bulbasaur" 

        out = StringIO()
        call_command('evolution_chain', '--id=1', stdout=out)
        self.assertIn('Successfully load evolution chain', out.getvalue())
        
        response = self.client.get(
            reverse('detail',kwargs={'name':pokemon_name})
        )
        data = response.data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 6)
        self.assertEqual(data['name'], pokemon_name)
        self.assertTrue('id' in str(data))
        self.assertTrue('name' in str(data))
        self.assertTrue('height' in str(data))
        self.assertTrue('weight' in str(data))
        self.assertTrue('evolutions' in str(data))
        self.assertTrue('stats' in str(data))
        self.assertEqual(len(response.json()['stats']), 6)

    def test_eevee_evolution_chain(self):
        pokemon_name = "eevee" 

        out = StringIO()
        call_command('evolution_chain', '--id=67', stdout=out)
        self.assertIn('Successfully load evolution chain', out.getvalue())
        
        response = self.client.get(
            reverse('detail',kwargs={'name':pokemon_name})
        )
        data = response.data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 6)
        self.assertEqual(data['name'], pokemon_name)
        self.assertTrue('id' in str(data))
        self.assertTrue('name' in str(data))
        self.assertTrue('height' in str(data))
        self.assertTrue('weight' in str(data))
        self.assertTrue('evolutions' in str(data))
        self.assertTrue('stats' in str(data))
        self.assertEqual(len(response.json()['stats']), 6)
