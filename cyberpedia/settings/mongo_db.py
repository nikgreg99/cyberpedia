import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"mongodb.env")
load_dotenv(dotenv_path)



DATABASES = {
    'default': {
        'ENGINE': os.environ.get('MONGO_ENGINE'),
        'NAME': os.environ.get('MONGO_NAME'),
        'ENFORCE_SCHEMA': os.environ.get('MONGO_ENFORCE_SCHEMA'),
    'CLIENT':{
        'host': os.environ.get('MONGO_URL')

    }
    }
}