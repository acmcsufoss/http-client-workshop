import sys
import requests
import json

pokemon = sys.argv[1]

baseURL = "https://pokeapi.co/api/v2"

r = requests.get(f"{baseURL}/pokemon/{pokemon}")

if r.status_code == 200:
    data = r.json()

    print(f"Name: {data['name']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")

else:
    print(f"Status code: {r.status_code}")
