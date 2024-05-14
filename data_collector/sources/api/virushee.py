import logging
import requests

from data_collector.classes import TargetCollector
from django.conf import settings


logger = logging.getLogger(__name__)


class Virushee(TargetCollector):

    BASE_URL: str = "https://api.virushee.com/file/hash"
    virusshee = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Virushee, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.virusshee.headers = {
            "Content-Type ": "application/json",
            "X-API-Key": self.secrets["api_key"]
        }
        self.virusshee.proxies = settings.PROXIES

    def collect_target(self, observable):
        final_url = self.BASE_URL + f"/{observable}"

        try:
            response = self.virusshee.get(final_url)
            response.raise_for_status()
        except requests.RequestException() as ex:
            raise Exception(ex)
        result = response.json()
        return result
