import django
import factory
from pokemon.models import Pokemon
from pokemon import MODULE_SETTINGS as settings
from pokemon.tests import helpers
from factory.django import DjangoModelFactory

class RatataFactory(DjangoModelFactory):
    class Meta:
        model = Pokemon

    name = 'rattata'
    details = factory.Dict(helpers.load_json(settings['POKEMON_JSON_EXAMPLE']))