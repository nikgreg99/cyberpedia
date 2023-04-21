import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"misp.env")
load_dotenv(dotenv_path)

MISP_URL = os.environ.get('MISP_URL')
MISP_PORT = os.environ.get('MISP_PORT')
MISP_API_KEY = os.environ.get('MISP_API_KEY')
MISP_VERIFY_CERT = os.environ.get('MISP_VERIFY_CERT')