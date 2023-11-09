import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector ,TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class NIST(FeedCollector,TargetCollector):

    START_INDEX_DEFAULT = 0
    RESULT_PER_PAGE_DEFAULT = 2000

    cve_url : str = "https://services.nvd.nist.gov/rest/json/cve/.2.0"
    cve_history_url = "https://services.nvd.nist.gov/rest/json/cvehistory/.2.0"
    nist = requests.Session()


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NIST,cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
         super().__init__(self.__class__.__name__)
         self.init_collector()

    def init_collector(self):
        self.nist.headers = {
            'apikey':  self.secrets["api_key"]
        }
        self.error = {}
        self.nist.proxies = settings.PROXIES
        self.nist.params = {
            'startIndex':  self.START_INDEX_DEFAULT,
            'resultsPerPage': self.RESULT_PER_PAGE_DEFAULT
        }

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.nist.get(final_url,params=self.nist.params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['nist'] = ex
        return response.json()
    
    def collect_all_cve(self):
        cve_data = []
        while True:
            data = self.make_request(self.base_url)
            self.nist.params["startIndex"] += self.nist.params['resultsPerIndex']
            if settings.DEBUG:
                logger.info(data)
            cve_data.append(data["vulnerabilities"])
            if  self.nist.params["startIndex"] > data["totalResults"]
                break

            

    def collect(self) -> dict:
        return self.collect_all_cve