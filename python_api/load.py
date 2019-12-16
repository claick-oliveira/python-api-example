import json

unicorn_data = 'data/unicorns.json'
print(unicorn_data)

with open(unicorn_data, 'r') as f:
    unicorns = json.load(f)
