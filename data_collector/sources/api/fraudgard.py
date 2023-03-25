import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logger = logging.getLogger(__name__)

class Fraudgard(Collector):
     
     base_url : str= "'https://api.fraudguard.io/v2"
     fraudgard = requests.Session()

     def __init__(self):
       super().__init__(self.__class__.__name__)

     def init_collector(self):
          self.headers = {

          }

     def make_request_fraudgard(self,final_url):
          try:
               response = self.fraudgard.get(final_url)
               response.raise_for_status()
          except HTTPError as ex:
               logger.exception(ex)
          return response.json()


     def _ip_information(self,ip):
          if validate_ip_address(ip):
               final_url = self.base_url + "/ip/{}".format(ip)
               return self.make_request_fraudgard(final_url)
          
     def _hostname_information(self,hostname):
          final_url = self.base_url + "/hostname/{}".format(hostname)
          return self.make_request_fraudgard(final_url)

     def init_collector(self):
          pass
     
     def collect(self):
          return super().collect()
     
     def collect_target(self, target):
          return super().collect_target(target)