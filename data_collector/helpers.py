import io
import csv
import json

def csv_to_json(csv_content):
    reader = csv.DictReader(io.StringIO(csv_content))
    return json.dumps(list(reader))


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