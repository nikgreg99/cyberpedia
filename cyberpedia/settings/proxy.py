import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"mongodb.env")
load_dotenv(dotenv_path)


import os 
HTTP_PROXY_URL = os.environ.get('HTTP_PROXY_URL')
HTTPS_PROXY_URL = os.environ.get('HTTPS_PROXY_URL')

PROXIES = {
    'http': HTTP_PROXY_URL,
    'https': HTTPS_PROXY_URL
}