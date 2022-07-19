from django.urls import path

from pokemon.views import PokemonDetail

urlpatterns = [
   path('<str:name>/', PokemonDetail.as_view(), name="detail")
]
