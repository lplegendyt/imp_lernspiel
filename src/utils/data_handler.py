import os
import json

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'user_data.json')

def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as file:
            return json.load(file)
    return {"klasse": 3, "coins": 0}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, 'w') as file:
        json.dump(data, file)
