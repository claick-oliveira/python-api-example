import json
import os

unicorn_data = os.path.dirname(__file__) + '/data/unicorns.json'

with open(unicorn_data, 'r') as f:
    unicorns = json.load(f)
