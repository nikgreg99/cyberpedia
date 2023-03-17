import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logger = logging.getLogger(__name__)

class FraudGard(Collector):
     
     base_url : str= "'https://api.fraudguard.io/v2"
     fraudgard = requests.Session()


     def _ip_information():
          pass

     def init_collector(self):
          return super().init_collector()
     
     def collect(self):
          return super().collect()
     
     def collect_target(self, target):
          return super().collect_target(target)