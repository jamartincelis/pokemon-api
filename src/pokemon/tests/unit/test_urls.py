from django.test import TestCase
from django.urls import reverse
from pokemon import MODULE_SETTINGS

class TestWeatherUrls(TestCase):
    def test_resolution_for_pokemon_detail(self):
        url = reverse('detail', args=[MODULE_SETTINGS['POKEMON_NAME_EXAMPLE']])
        self.assertEqual(url, MODULE_SETTINGS['URL_POKEMON_DETAIL']) 