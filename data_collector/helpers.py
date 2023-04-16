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