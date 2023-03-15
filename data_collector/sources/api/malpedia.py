import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logging = logging.getLogger<(__name__)

class Malpedia(Collector):

    base_url: str = "https://malpedia.caad.fkie.fraunhofer.de/api"
    malpedia = requests.Session()

    def __init__(self):
        api_token = ""
        self.headers = {
            "Authorization": "apitoken {}".format(api_token)
        }

    def get_yara_rules(self):
        final_url = self.base_url + "/list/yara"
        try:
            response = self.malpedia.get(final_url,headers = self.headers)
            response.raise_for_status()
        except HTTPError  as ex:
            logging.exception(ex)
        return response.json()
        