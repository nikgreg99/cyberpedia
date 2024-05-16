import requests
import logging
import OTXv2
import urllib

from ipaddress import AddressValueError,IPv4Address
from typing import List
from data_collector.helpers import get_hash_type 
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)

class Otx(TargetCollector):


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Otx, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.malware_bazaar.headers = {
            'API-KEY': ''
        }
        self.error = {}
        self.malware_bazaar.proxies = settings.PROXIES