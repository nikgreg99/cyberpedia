import logging
import requests

from requests import HTTPError
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class WhoIsRipeApi(TargetCollector):

    BASE_URL: str = "https;//rest.db.ripe.net/search.json"
    who_is_ripe = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WhoIsRipeApi, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.who_is_ripe.headers = {
            "Content-Type ": "application/json",
        }
        self.who_is_ripe.proxies = settings.PROXIES

    def collect_target(self,observable) -> dict:
        params = {"query-string": observable}

        try:
            response = self.who_is_ripe.get(self.BASE_URL,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.error(ex)

        return response.json()
