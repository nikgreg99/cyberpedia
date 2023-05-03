import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"elastic.env")
load_dotenv(dotenv_path)

ELASTIC_PORT = os.environ.get('ELASTIC_PORT')

ELASTICSEARCH_DSL={
    "default": {
        "hosts": os.environ.get('ELASTIC_HOST')
    },
}