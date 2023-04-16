import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)


class Tranco(Collector):

    base_url: str = "https://tranco-list.eu/api"
    tranco = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_key = self.secrets["api_key"]

    
    def collect_target(self,target),:
        final_url = self.base_url + f"/ranks/domain/{target}"
        try:
            response = self.tranco.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()