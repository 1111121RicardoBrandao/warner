from configparser import SafeConfigParser
import requests
import time
import json

api, neLat, swLat, neLng, swLng = "","","","",""


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

#print("Writing Data to the file ...")
#createconfigfile()
print("Reading data from config file ...")
readconfigfile()
print("Grabbing data ...")
print("api = " + api)
print("NE = " + neLat + "," + neLng)
print("SW = " + swLat + "," + swLng)

timestamp = int(time.time())
payload = {'timestamp' : timestamp, 'pokemon' : 'true', 'lastpokemon' : 'false', 'pokestops' : 'false', 'lastpokestops' : 'false', 'luredonly' : 'false', 'gyms' : 'false', 'scanned' : 'false', 'spawnpoints' : 'false', 'swLat' : swLat, 'swLng' : swLng, 'neLat' : neLat, 'neLng' : neLng, 'oSwLat' : swLat, 'oSwLng' : swLng, 'oNeLat' : neLat, 'oNeLng' : neLng, 'reids' : '' , 'eids' : '', '_' : '1482712998794'}
request = requests.get(api, params = payload)
print(request.url)

data = request.json()
print("Get " + str(len(data["pokemons"])) + " pokemons.")