from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404


class PokemonDetail(RetrieveAPIView):
    """
    Permite obtener el detalle del pokemon.
    """
    serializer_class = PokemonSerializer

    def get_queryset(self):
        return Pokemon.objects.filter(name=self.kwargs['name'])

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends

        obj = get_object_or_404(queryset)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj