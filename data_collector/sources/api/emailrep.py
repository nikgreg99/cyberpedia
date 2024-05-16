import requests
from requests import HTTPError
import logging
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class EmailRep(TargetCollector):
    """
        Wrapper of EmailRep API
    """
    BASE_URL: str = "'https://emailrep.io"
    emailrep = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(EmailRep, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.emailrep.headers = {
            'Key': self.secrets["api_key"],
            'User-Agent': 'cyberpedia'
        }
        self.emailrep.proxies = settings.PROXIES

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.emailrep.get(final_url,headers=self.emailrep.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def collect_target(self, observable):
        
        final_url = self.BASE_URL + f"email/{observable}"
        return self.make_request(final_url=final_url)
