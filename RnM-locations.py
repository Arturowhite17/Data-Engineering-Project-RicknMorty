import requests
import pandas as pd 
import csv
import json 
from datetime import datetime

""" 
Rick and Morty API for all locations - https://rickandmortyapi.com/api/locations 
Using "Request" library
"""
date = datetime.now().strftime('%Y_%m_%d-%I:%M:%S_%p')
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'location'

r = requests.get(baseurl + endpoint)

response = r.json()

data = json.loads(r.content)

# print(r) # used to verify connect successful, expected response 200
# print(data) # used to print all data in console 

headers = data['results'][0].keys() # list of keys - 'id', 'name', 'type', 'dimension', 'residents', 'url', 'created'
values = data['results']

all_items = []

# print(headers)

# Loop through keys and values and add to list

all_items.append(headers)

for value in values:
    items = [] # interm list to hold/ collect values  
    items.append(value['id'])
    items.append(value['name'])
    items.append(value['type'])
    items.append(value['dimension'])
    items.append(value['residents'])
    items.append(value['url'])
    items.append(value['created'])

    all_items.append(items)

print(all_items)

# create CSV output 

export_file = f'RnM_{endpoint}-output_{date}.csv'

with open(export_file, 'w') as f:
    document = csv.writer(f, delimiter = ',')
    document.writerows(all_items)

f.close()