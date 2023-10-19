import requests
from requests import HTTPError
import logging 
from data_collector.classes import TargetCollector
from django.conf import settings


logger = logging.getLogger(__name__)

class InQuest(TargetCollector):

    base_url : str = "https://labs.inquest.net/api"
    inquest = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.headers = {
            'Accept': 'application/json',
            'Authorization': ''
            }
        self.error = {}
        self.inquest.proxies = settings.PROXIES
        

    def make_inquest_request(self,final_url,paramters):
        try:
            response = self.inquest.get(final_url,params=paramters)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['inquest'] = ex
        return response.json()
    
    def collect(self):
        return super().collect()
    

    def search_IOC(self,target):
        final_url = self.base_url + "/repdb"
        parameters = {'search': target}
        return self.make_inquest_request(final_url,parameters)

    def collect_target(self, target):
        return self.collect_target()