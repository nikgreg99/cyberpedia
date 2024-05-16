import requests
import logging

from requests import HTTPError
from data_collector.helpers import is_url_or_domain
from data_collector.classes import TargetCollector
from django.conf import settings
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

class Tranco(TargetCollector):

    BASE_URL = "https://tranco-list.eu/api/ranks/domain/"
    tranco = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Tranco, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.tranco.headers = {
            "Accept": "application/json"
        }
        self.tranco.proxies = settings.PROXIES

    def collect_target(self,target) -> dict:
        if is_url_or_domain(target) == "url":
            hostname = urlparse(target).hostname
            final_url = self.BASE_URL + hostname
            try:
                response = self.tranco.get(final_url)
                response.raise_for_status()
            except HTTPError as ex:
                logger.exception(ex)
        return response.json()
