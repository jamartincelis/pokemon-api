from rest_framework import serializers
from pokemon.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una ciudad.
    """
    class Meta:
        model = Pokemon
        fields = '__all__'

    def to_representation(self, instance):
        """
        Permite modificar la forma en que se retornan las ciudades.
        """
        data = super(PokemonSerializer, self).to_representation(instance)

        data.pop('id')
        data.pop('name')
        details = data.pop('details')
        
        data['id'] = details['pokemon_id']
        data['name'] = details['pokemon_name']
        data['height'] = details['height']
        data['weight'] = details['weight']
        data['evolutions'] = details['evolutions']
        data['stats'] = details['stats']
                
        data.update(data)
        return data