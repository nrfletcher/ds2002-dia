'''
Simple utility class to fix JSON being parsed incorrectly from SQLite3 database
'''
import json

with open('data.json', 'r') as f:
    data = f.read().replace("'", '"')

fixed_data = json.loads(data)

with open('fixed.json', 'w') as f:
    json.dump(fixed_data, f, indent=4)