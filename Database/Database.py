import sqlite3
import DataParser.pokemon

connection = ""
cursor = ""

def startDbConn() :
    print("Starting connection to Database")
    global connection
    global cursor
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    return cursor

def closeDbConn() :
    global connection
    global cursor
    print("Closing connection to Database")
    cursor.close()
    connection.close()

def queryDb() :
    global connection
    cursor = connection.execute('select * from pokemon')
    rows = cursor.fetchall()
    return rows

def createDatabaseSkeleton() :
    print("Creating Database and Structure")
    global cursor
    global connection
    startDbConn()
    cursor.execute('CREATE TABLE IF NOT EXISTS allTimePokemon(disappear_time REAL, encounter_id TEXT, pokemon_id REAL, pokemon_name TEXT, rarity TEXT, move1 REAL, move2 REAL, individual_attack REAL, individual_defense REAL, individual_stamina REAL, latitude REAL, longitude REAL, last_modified REAL, spawnpoint_id TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS activePokemon(disappear_time REAL, encounter_id TEXT, pokemon_id REAL, pokemon_name TEXT, rarity TEXT, move1 REAL, move2 REAL, individual_attack REAL, individual_defense REAL, individual_stamina REAL, latitude REAL, longitude REAL, last_modified REAL, spawnpoint_id TEXT)')
    #cursor.execute('CREATE TABLE IF NOT EXISTS ')
    connection.commit()

def insertNewFinding(pokemon):
    global cursor
    global connection
    cursor.execute("INSERT INTO allTimePokemon VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (pokemon.disappear_time,pokemon.encounter_id,pokemon.pokemon_id,pokemon.pokemon_name,pokemon.rarity,pokemon.move1,pokemon.move2,pokemon.individual_attack,pokemon.individual_defense,pokemon.individual_stamina,pokemon.latitude,pokemon.longitude,pokemon.last_modified,pokemon.spawnpoint_id))
    connection.commit()
