import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class Virushee(Collector):

    base_url : str = "https://api.virushee.com"
    virushee = requests.Session()

    def __init__(self) -> None:
        return super().__init__(self.__class__.__name__)

    def init_collector(self):
        #api_key = self.secrets["api_key"]
        pass
        #self.headers = {"X-API-Key" : api_key}

    def collect_target(self, target):
        final_url = self.base_url + f"/file/hash{target}"
        try:
            response = self.virushee.get(final_url,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()
