import requests
from requests import HTTPError
import requests
import logging
from data_collector.classes import Collector


logger = logging.getLogger()


class HaveIBeenPwned(Collector):

    base_url : str = "https://haveibeenpwned.com/api/v3"
    have_i_been_pwned = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
    
    def init_collector(self):
        pass

    def make_request_pwned(self,final_url,paramters=None):
        try:
            response = self.have_i_been_pwned.get(final_url,params=paramters)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def collect(self):
        final_url = self.base_url + "/breaches"
        return self.make_request_pwned(final_url)

    def collect_target(self, target):
        final_url = self.base_url  + "/breach/{}".format(target)
        return self.make_request_pwned(final_url)

        
