import json
from time import strftime
import requests
import csv
from datetime import datetime

""" 
Rick and Morty API for all data - https://rickandmortyapi.com/api/character 
Using "Request" library
"""
date = datetime.now().strftime('%Y_%m_%d-%I:%M:%S_%p')
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

r = requests.get(baseurl + endpoint)

response = json.loads(r.content)

data = response['results']
# print(r) # used to verify connect successful, expected response 200
print(data) # used to print all data in console 

headers = data[0].keys()
# print(headers)
# print(data)

all_items = []
# Add column headers 
all_items.append(headers)
#  Loop over values in list of dictionaries 
#  cloumn's of interest names: id, name, status, species, type, gender, origin, location, image, episode, url, created
for character in data:
    items = []
    # items.append(character)
    # items.append(character)
    items.append(character['id'])
    items.append(character['name'])
    items.append(character['status'])
    items.append(character['species'])
    items.append(character['type'])
    items.append(character['gender'])
    items.append(character['origin'])
    items.append(character['location'])
    items.append(character['image'])
    items.append(character['episode'])
    items.append(character['url'])
    items.append(character['created'])

    
    all_items.append(items)


export_file = f"RnM_{endpoint}-output_{date}.csv"

with open(export_file, 'w') as f:
    document = csv.writer(f, delimiter = ',')
    document.writerows(all_items)

f.close()

print(all_items)