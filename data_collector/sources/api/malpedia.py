import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector
from data_collector.helpers import csv_to_json
from django.conf import settings

logger = logging.getLogger(__name__)

class Malpedia(FeedCollector):

    base_url: str = "https://malpedia.caad.fkie.fraunhofer.de/api"
    malpedia = requests.Session()

    
    def __init__(self):
       super().__init__(self.__class__.__name__)
       

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.headers = {
            "Authorization ": "apitoken {}".format(api_key)
        }
        self.malpedia.proxies = settings.PROXIES

   
    def get_yara_rules(self):
        final_url = self.base_url + "/list/yara"
        try:
            response = self.malpedia.get(final_url,headers = self.headers)
            response.raise_for_status()
        except HTTPError  as ex:
            logging.exception(ex)
        return csv_to_json(response.content)
        