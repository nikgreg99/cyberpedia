import requests
from requests import HTTPError
from data_collector.classes import Collector
import logging

logger = logging.getLogger(__name__)

class CIRCLHashLookup(Collector):

    base_url : str = "https://hashlookup.circl.lu"
    circl_hash_lookup = requests.Session()

    def __init__(self, name) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        pass