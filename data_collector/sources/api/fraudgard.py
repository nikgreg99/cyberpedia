import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth
import logging
from data_collector.classes import Collector
from data_collector.utils import is_IP_adress
from django.conf import settings

logger = logging.getLogger(__name__)

class Fraudgard(Collector):
     
     base_url : str= "'https://api.fraudguard.io/v2"
     fraudgard = requests.Session()

     def __init__(self):
       super().__init__(self.__class__.__name__)
       self.init_collector()
       self.error = {}

     def init_collector(self):
          self.fraudgard.verify = True
          username = self.secrets["username"]
          password = self.secrets["password"]
          self.fraudgard.auth = HTTPBasicAuth(username=username,password=password)
          self.fraudgard.proxies = settings.PROXIES


     def make_request_fraudgard(self,final_url):
          try:
               response = self.fraudgard.get(final_url)
               response.raise_for_status()
          except HTTPError as ex:
               logger.exception(ex)
               self.err["fraudgard"] = ex
          return response.json()


     def _ip_information(self,ip):
          if is_IP_adress(ip):
               final_url = self.base_url + "/ip/{}".format(ip)
               return self.make_request_fraudgard(final_url)
          
     def _hostname_information(self,hostname):
          final_url = self.base_url + "/hostname/{}".format(hostname)
          return self.make_request_fraudgard(final_url)

  
     def collect(self):
          return super().collect()
     
     def collect_target(self, target):
          return self._ip_information(target)