import os
import csv
import json

def csv_to_json(csv_content):
    json_dictionary = []
    csv_reader = csv.DictReader(csv_content)
    for row in csv_reader:
        json_dictionary.append()  
    return json.dumps(json_dictionary,indent=4)


def read_json_file(file_path)-> dict:
         with open(file_path) as f:
              config_dict = json.load(f)
         return config_dict


 
def get_env_var(name):
        value = os.getenv(name)
        try:
            return json.loads(name)
        except(json.JSONDecodeError,TypeError):
            return value