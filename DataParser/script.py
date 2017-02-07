from configparser import SafeConfigParser
import requests
import time
import json
import Database.Database

from DataParser.pokemon import Pokemon

api, neLat, swLat, neLng, swLng = "","","","",""
activePokemons = []

def createconfigfile() :
    config = SafeConfigParser()
    config.read('config.ini')

    config.add_section('site')
    config.set('site', 'url', 'http://overdose.suporteaereo.com/raw_data')
    config.add_section('location')
    config.set('location', 'neLat', '41.21378266048811')
    config.set('location', 'swLat', '41.15189853273638')
    config.set('location', 'neLng', '-8.471919150107396')
    config.set('location', 'swLng', '-8.801508993857396')

    with open('config.ini', 'w') as f:
        config.write(f)


def readconfigfile() :
    config = SafeConfigParser()
    config.read('config.ini')
    global api
    api = config.get('site', 'url')
    global neLat
    neLat= config.get('location', 'neLat')
    global swLat
    swLat= config.get('location', 'swLat')
    global neLng
    neLng= config.get('location', 'neLng')
    global swLng
    swLng= config.get('location', 'swLng')

def apicall(api,neLat, neLng, swLat, swLng, timestamp) :
    payload = {  # 'timestamp' : timestamp,
        'pokemon': 'true',
        'lastpokemon': 'false',
        'pokestops': 'false',
        'lastpokestops': 'false',
        'luredonly': 'false',
        'gyms': 'false',
        'scanned': 'false',
        'spawnpoints': 'false',
        'swLat': swLat,
        'swLng': swLng,
        'neLat': neLat,
        'neLng': neLng,
        'oSwLat': swLat,
        'oSwLng': swLng,
        'oNeLat': neLat,
        'oNeLng': neLng,
        'reids': '',
        'eids': '',
        '_': initial_timestamp}
    request = requests.get(api, params=payload)
    print(request.url)
    data = request.json()
    print("Get " + str(len(data["pokemons"])) + " pokemons.")




#print("Writing Data to the file ...")
#createconfigfile()
print("Reading data from config file ...")
readconfigfile()
print("Grabbing data ...")
print("api = " + api)
print("NE = " + neLat + "," + neLng)
print("SW = " + swLat + "," + swLng)

initial_timestamp = int(time.time())
timestamp = int(time.time())




pokemons = data["pokemons"]
new_timestamp = data["timestamp"]

print("New TimeStamp = " + str(new_timestamp))

for poke in pokemons:
    p = Pokemon(poke["pokemon_id"], poke["pokemon_name"], poke["individual_attack"], poke["individual_defense"], poke["individual_stamina"], poke["latitude"], poke["longitude"])
    iv = 0
    activePokemons.append(p)
    try:
        iv = p.calcPokemonIV()
    except :
        print(poke)
    if (iv>90) :
        print(poke["pokemon_name"] + " = " + str(p.calcPokemonIV()) + "% IV")
    #Database.insertNewFinding(p)

initial_timestamp = initial_timestamp+1
payload = {#'timestamp' : new_timestamp,
           'pokemon' : 'true',
           'lastpokemon' : 'false',
           'pokestops' : 'false',
           'lastpokestops' : 'false',
           'luredonly' : 'false',
           'gyms' : 'false',
           'scanned' : 'false',
           'spawnpoints' : 'false',
           'swLat' : swLat,
           'swLng' : swLng,
           'neLat' : neLat,
           'neLng' : neLng,
           'oSwLat' : swLat,
           'oSwLng' : swLng,
           'oNeLat' : neLat,
           'oNeLng' : neLng,
           'reids' : '' ,
           'eids' : ''}
           #'_' : initial_timestamp}
request = requests.get(api, params = payload)
print(request.url)

data = request.json()
print("Get " + str(len(data["pokemons"])) + " pokemons.")