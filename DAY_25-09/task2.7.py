types = {
    "Electric": [],
    "Grass": [],
    "Fire": [],
}

types["Electric"].append("Pikachu")
types["Grass"].append("Bulbasaur")
types["Fire"].append("Charmander")
types["Grass"].append("Leafeon")
types["Grass"].append("Scovillain")   
types["Fire"].append("Scovillain")   

for pokemon_type, pokemons in types.items():
    if "Pikachu" in pokemons:
        print(pokemon_type)
