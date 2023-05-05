import os
import csv
import json

def csv_to_dict(csv_file,primary_key):
    data_dict = {}
    with open(csv_file,encoding="utf-8") as csv_handler:
        csv_reader = csv.DictReader(csv_handler)
        for row in csv_reader:
            key = row[primary_key]
            data_dict[key] = row   

    return json.dumps(data_dict,indent=4)


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