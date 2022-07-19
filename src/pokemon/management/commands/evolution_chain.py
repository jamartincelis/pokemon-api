import imp
from django.core.management.base import BaseCommand, CommandError
from  ._helpers import get_pokemon
from pokemon.models import Pokemon
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Get information about the pokemon evolution chain'

    def add_arguments(self, parser):
        parser.add_argument(
            '--id', help='Id of the pokemon evolution chain', type=int, default=67)

    def handle(self, *args, **options):

        print(options['id'])
        id_evolution_chain = options['id']
        pokemon_dict = get_pokemon(id_evolution_chain)

        pokemon = Pokemon(
            name=pokemon_dict['pokemon_name'],
            details=pokemon_dict
        )
        try:
            pokemon.save()
        except IntegrityError:
            self.stdout.write(self.style.WARNING(f"The evolution chain for pokemon {pokemon_dict['pokemon_name']} already exists in the database."))
        else:
            self.stdout.write(self.style.WARNING('Successfully load evolution chain'))