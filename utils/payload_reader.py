import json
import os


def read_json(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    payload_path = os.path.join(base_path, "../payloads", file_name)
    with open(payload_path,'r') as file:
        return json.load(file)
