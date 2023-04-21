import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"mongodb.env")
load_dotenv(dotenv_path)



DATABASES = {
    'default': {
        'ENGINE': os.environ.get('MONGODB_ENGINE'),
        'NAME': os.environ.get('MONGODB_NAME'),
        "USER": os.environ.get('MONGODB_USER'),
        "PASSWORD": os.environ.get('MONGODB_PASSWORD'),
        "HOST": os.environ.get('MONGODB_HOST'),
        "PORT": os.environ.get('MONGODB_PORT'),
        'ENFORCE_SCHEMA': os.environ.get('MONGODB_ENFORCE_SCHEMA')
    }
}