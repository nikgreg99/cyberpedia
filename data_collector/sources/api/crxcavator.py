import enum
import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class CRXPLatform(enum.Enum):
    CHROME = "Chrome"
    FIREFOX = "Firefox"
    EDGE = "Edge"


class CRXCavator(TargetCollector):

    BASE_URL: str = "https://api.crxcavator.io/v1/version"
    crx_cavator = requests.Session()
    platform: str = CRXPLatform.FIREFOX

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CRXCavator, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.crx_cavator.proxies = settings.PROXIES

    def collect_target(self,target) -> dict:
        final_url = self.BASE_URL + f"/{target}"
        params = {
            "platform": self.platform
        }
        try:
            response = self.crx_cavator.get(final_url,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)

        return response.json()
                                                                                                                                     
