import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"opencve.env")
load_dotenv(dotenv_path)

OPENCVE_URL = os.environ.get('OPENCVE_URL')
OPENCVE_USER = os.environ.get('OPENCVE_USER')
OPENCVE_PASSWORD = os.environ.get('OPENCVE_PASSWORD')
OPENCVE_PORT = os.environ.get('OPENCVE_PORT')