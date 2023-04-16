import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class Koodous(Collector):

    base_url: str = "https://developer.koodous.com"
    koodous = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.headers = {
            "Authorization": api_key
        }

    def make_request_koodous(self,final_url):
        try:
            response = self.koodous.get(final_url,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()
    

    def feed_apks(self)
        final_url = self.base_url + "feed/apks"
        return self.make_request_koodous(final_url)
    
    def feed_analyses(self):
        final_url = self.base_url + "feed/analyses"
        return self.make_request_koodous(final_url)
    
    def feed_detected(self):
        final_url = self.base_url + "feed/detected"
        return self.make_request_koodous(final_url)