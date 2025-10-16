import sys
import requests
import json

pokemon = sys.argv[1]
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

resp = requests.get(url)

# Basic error handling
if resp.status_code == 200:
    data = resp.json()

    # To pretty print (works with tools like 'jq'):
    # print(json.dumps(data))

    # To print event prettier:
    # print(json.dumps(data, indent=2))

    # Get basic info
    name = data["name"]
    weight = data["weight"]
    height = data["height"]

    # Get types
    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])

    # Get abilities
    abilities = []
    for ability in data["abilities"]:
        abilities.append(ability["ability"]["name"])

    # Get flavor text
    species_url = data["species"]["url"]
    species_resp = requests.get(species_url)
    species_data = species_resp.json()

    for entry in species_data["flavor_text_entries"]:
        # only get the english one
        if entry["language"]["name"] == "en":
            flavor_text = entry["flavor_text"].replace("\n", " ").replace("\f", " ")
            break

    print(f"Name: {name}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Types: {types}")
    print(f"Abilities: {abilities}")
    print(f"Description: {flavor_text}")


else:
    print(f"Status code: {resp.status_code}")
