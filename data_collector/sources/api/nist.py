import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector
from django.conf import settings

logger = logging.getLogger(__name__)


# STATUS OK: We keep it
class Nist(FeedCollector):

    START_INDEX_DEFAULT = 0
    RESULT_PER_PAGE_DEFAULT = 2000

    cve_url: str = "https://services.nvd.nist.gov/rest/json/cves/2.0/"
    cve_history_url = "https://services.nvd.nist.gov/rest/json/cvehistory/.2.0"
    nist = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Nist, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
         super().__init__(self.__class__.__name__)
         self.init_collector()

    def init_collector(self):
        self.nist.headers = {
            'apiKey':  self.secrets["api_key"]
        }
        self.error = {}
        self.nist.proxies = settings.PROXIES
  
    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.nist.get(self.cve_url,params=params)
            print(response.status_code)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['nist'] = ex
        return response.json()

def collect(self) -> dict:
       pass 
