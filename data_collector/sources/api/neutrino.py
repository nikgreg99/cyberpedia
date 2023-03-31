import requests
import logging
from data_collector.classes import Collector

logger = logging.getLogger()

class Neutrino(Collector):

    base_url: str = "https://neutrinoapi.net/ip-blocklist-download"
    neutrino = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    
    
