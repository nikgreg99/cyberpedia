import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logging = logging.getLogger(__name__)

class Pulsdive(Collector):

    base_url = "https://pulsedive.com/api"
    pulsidive = requests.Session()

    def __init__(self) -> None:
        super().__init__()

    