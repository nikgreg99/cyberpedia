import os
from dotenv import load_dotenv
from .common import CONFIG_DIR


dotenv_path = os.path.join(CONFIG_DIR,"digitalside.env")
load_dotenv(dotenv_path)


DIGITAL_SIDE_OSINT_URL = os.environ.get("DIGITAL_SIDE_OSINT_URL")
DIGITAL_SIDE_URL_COLLECTIONS = os.environ.get("DIGITAL_SIDE_URL_COLLECTIONS")
TAXII_SERVER_USERNAME = os.environ.get("TAXII_SERVER_USERNAME")
TAXII_SERVER_PASSWORD = os.environ.get("TAXII_SERVER_PASSWORD")
TAXII_VERSION = os.environ.get("TAXII_VERSION")
