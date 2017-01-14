class Pokemon:
    'Commom base class to declare all pokemons'

    def __init__(self,disappear_time , encounter_id , pokemonid , name , rarity , move1 , move2 , individual_attack , individual_defense , individual_stamina, latitude, longitude, last_modified, spawnpoint_id):
        self.pokemonid = pokemonid
        self.name = name
        self.disappear_time = disappear_time
        self.encounter_id = encounter_id
        self.rarity = rarity
        self.move1 = move1
        self.move2 = move2
        self.individual_attack = individual_attack
        self.individual_defense = individual_defense
        self.individual_stamina = individual_stamina
        self.latitude = latitude
        self.longitude = longitude
        self.last_modified = last_modified
        self.spawnpoint_id = spawnpoint_id

    def __init__(self, pokemon_id, name, individual_attack, individual_defense, individual_stamina, latitude, longitude):
        self.pokemon_id = pokemon_id
        self.name = name
        self.individual_attack = individual_attack
        self.individual_defense = individual_defense
        self.individual_stamina = individual_stamina
        self.latitude = latitude
        self.longitude = longitude

    def calcPokemonIV(self):
        iv = ((self.individual_attack + self.individual_defense + self.individual_stamina)/45)*100
        return int(iv)


#pok = Pokemon(111111,11111,111,'bulbasaur','normal',123,123,10,10,10,100,100,100,100213)
#print(pok.calcPokemonIV())
