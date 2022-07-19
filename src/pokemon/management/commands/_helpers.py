import requests
from urllib.parse import urlparse


def validate_api(url=""):
    response = requests.head(url)
    if response.status_code != 200: 
        return {'reason':response.reason}
    return {}
        
def api_evolution_chain(id_evolution_chain=None):
    url = f'https://pokeapi.co/api/v2/evolution-chain/{id_evolution_chain}/'
    
    is_valid = validate_api(url)
    if 'reason' in is_valid:
        return is_valid['reason']

    response = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{id_evolution_chain}/')
    return response.json()

def api_pokemon(id_pokemon=None):
    url = f'https://pokeapi.co/api/v2/pokemon/{id_pokemon}/'
    
    is_valid = validate_api(url)
    if 'reason' in is_valid:
        return is_valid['reason']

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id_pokemon}/')
    return response.json()
    
def check_url(url):
    parsed_url = urlparse(url)
    if bool(parsed_url.scheme):
        return parsed_url
    return False

def get_pokemon_id(poke_object={}, is_evolution=False):
    if is_evolution:
        return get_id(poke_object['species']['url'])
    else:
        return get_id(poke_object['chain']['species']['url'])
    
def get_id(url=""):
    # chequear si url es valida
    parsed_url = check_url(url)
    return parsed_url.path.split('/')[-2]

def add_evolution(evolves_to={}):
    evolution_dict = {}
    evolution_dict['id'] = get_pokemon_id(evolves_to, is_evolution=True)
    evolution_dict['name'] = evolves_to['species']['name']
    return evolution_dict


def get_pokemon_evolutions(evolution_chain={}):
    evolutions = []
    for evolution in evolution_chain['chain']['evolves_to']:
        evolutions.append(add_evolution(evolution))
        if evolution['evolves_to']:
            print(evolution['evolves_to'])
            evolutions.append(add_evolution(evolution['evolves_to'][0]))

    return evolutions

def get_pokemon_name(evolution_chain={}):
    return evolution_chain['chain']['species']['name']

def get_evolution_chain(evolution_chain={}):
    evolutions_dict = {}
    evolutions_dict['pokemon_id'] = get_pokemon_id(evolution_chain, is_evolution=False)
    evolutions_dict['pokemon_name'] = get_pokemon_name(evolution_chain)
    evolutions_dict['evolutions'] = get_pokemon_evolutions(evolution_chain)
    return evolutions_dict

def get_evolutions(id_evolution_chain=None):
    evolution_chain_response = api_evolution_chain(id_evolution_chain)
    return get_evolution_chain(evolution_chain_response)

def get_pokemon(id_evolution_chain=None):
    pokemon_dict = {}
    pokemon_dict = get_evolutions(id_evolution_chain)
    print(pokemon_dict)
    pokemon_id = pokemon_dict['pokemon_id']
    pokemon_detail = api_pokemon(pokemon_id)
    print("*"*20)
    pokemon_dict['height'] = pokemon_detail['height']
    pokemon_dict['weight'] = pokemon_detail['weight']
    pokemon_dict['stats'] = pokemon_detail['stats']
    print(pokemon_dict)
    
    return pokemon_dict