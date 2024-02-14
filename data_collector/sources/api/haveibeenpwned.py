import requests
from requests import HTTPError
import requests
import logging
from data_collector.classes import FeedCollector
from django.conf import settings


logger = logging.getLogger(__name__)

# STATUS: OK
class HaveIBeenPwned(FeedCollector):

    base_url : str = "https://haveibeenpwned.com/api/v3"
    have_i_been_pwned = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HaveIBeenPwned, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
    
    def init_collector(self):
        self.error = {}
        self.have_i_been_pwned.proxies= settings.PROXIES

    def make_request(self,final_url,paramters={},data={}):
        try:
            response = self.have_i_been_pwned.get(final_url,params=paramters)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['havebeenpwned'] = ex
        return response.json()

    def collect(self):
        final_url = self.base_url + "/breaches"
        breaches =  self.make_request(final_url)
        return breaches


        
