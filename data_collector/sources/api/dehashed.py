import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)

class DeHashed(Collector):

    dehased = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)


    def init_collector(self):
        self.dehased.proxies = settings.PROXIES

    