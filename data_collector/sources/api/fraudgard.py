import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class FraudGard(Collector:
     
     base_url : str= "'https://api.fraudguard.io/v2"
     fraudgard = requests.Session()