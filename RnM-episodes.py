import requests
import csv
from datetime import datetime
import json

""" 
Rick and Morty API for all episodes - https://rickandmortyapi.com/api/episodes 
Using "Request" library
"""

date = datetime.now().strftime('%Y_%m_%d-%I:%M:%S_%p')
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'episode'

r = requests.get(baseurl + endpoint)
data = json.loads(r.content)

# print(r) # used to verify connect successful, expected response 200
# print(data) # used to print all data in console 

values = data['results']

keys = data['results'][0].keys() 

# print(keys, values) # verify that desired values and header keys are returned 
# Keys output: 'id', 'name', 'air_date', 'episode', 'characters', 'url', 'created'
# add keys to list and then loop over values and add to list 

all_items = []

all_items.append(keys)

for value in values:
    items = []
    items.append(value['id'])
    items.append(value['name'])
    items.append(value['air_date'])
    items.append(value['episode'])
    items.append(value['characters'])
    items.append(value['url'])
    items.append(value['created'])

    # add all stored items the larger items (all_items) list which already contains the keys (file headers) 
    all_items.append(items)

print(all_items)

# create csv file 
output_file = f'RnM_{endpoint}-output_{date}.csv'

with open(output_file, 'w') as f:
    new_csv = csv.writer(f, delimiter =',')
    new_csv.writerows(all_items)

f.close()
