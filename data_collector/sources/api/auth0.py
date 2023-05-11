import requests
from requests import HTTPError
import logging
from django.conf import settings
from data_collector.classes import TargetCollector

logger = logging.getLogger(__name__)

class Auth0(TargetCollector):

    base_url = "https://signals.api.auth0.com/v2.0/ip"
    auth0 = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        pass

    def collect_target(self, target):
        try:
            final_url = self.base_url + f"/{target}"
            response = self.auth0.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()