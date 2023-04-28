import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"mongodb.env")
load_dotenv(dotenv_path)



DATABASES = {
    'default': {
        'ENGINE': os.environ.get('MONGODB_ENGINE'),
        'NAME': os.environ.get('MONGODB_NAME'),
    'CLIENT':{
        'host': 'mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb'

    }
    }
}