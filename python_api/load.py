import json

unicorn_data = 'data/unicorns.json'

with open(unicorn_data, 'r') as f:
    unicorns = json.load(f)
