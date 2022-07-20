from pokemon.tests.factories.pokemon_factories import RatataFactory
from django.urls import reverse
from rest_framework.test import APITestCase
from pokemon.models import Pokemon
from rest_framework import status

class PokemonDetailTest(APITestCase):

    def setUp(self):
        factory = RatataFactory()

        self.pokemon = Pokemon.objects.create( # create pokemon in database
            name=factory.name, 
            details=factory.details
        )

    def test_if_pokemon_exists(self):

        response = self.client.get(
            reverse('detail',kwargs={'name':'rattata'})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)
        self.assertTrue('id' in str(response.content))
        self.assertTrue('name' in str(response.content))
        self.assertTrue('height' in str(response.content))
        self.assertTrue('weight' in str(response.content))
        self.assertTrue('evolutions' in str(response.content))
        self.assertTrue('stats' in str(response.content))
        self.assertEqual(len(response.json()['stats']), 6)

    def test_if_pokemon_not_exists(self):

        response = self.client.get(
            reverse('detail',kwargs={'name':'ivasur'})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)