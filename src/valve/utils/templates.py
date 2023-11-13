import json
    
def read_json_template(file):
    with open(file, 'r') as f:
        return json.load(f)