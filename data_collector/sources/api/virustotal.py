import requests
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__ )

class VirusTotal(Collector):

    base_url: str = "https://www.virustotal.com/vtapi/v3"

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.headers = {
            "Accept": "application/json",
            "x-apikey": api_key
        }

    def collect(self):
        pass

    def collect_target(self):
        pass