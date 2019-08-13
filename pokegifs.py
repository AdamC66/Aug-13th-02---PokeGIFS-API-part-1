import json
import requests
import os
from random import randint

key = os.environ.get("GIPHY_KEY")

pokemon = randint(1,500)


res = requests.get(f"http://pokeapi.co/api/v2/pokemon/{pokemon}/")
body = json.loads(res.content)
name = body["name"] # should be "pikachu"
poke_id = body['id']  
poke_type = (body['types'][0]['type']['name'])
print(name, poke_id, poke_type)

url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}&rating=g".format(key,name)
res2 = requests.get(url)
gif_body = json.loads(res2.content)
print(gif_body['data'][0]['url'])