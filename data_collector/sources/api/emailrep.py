import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class EmailRep(Collector):

    base_url: str = "'https://emailrep.io"
    emailrep = requests.Session()

    def __init__(self) -> None:
        super().__init__(__class__.__name__)

    def init_collector(self):
        pass

    def collect_target(self, target):
        final_url = self.base_url + "/{}".format(target)
        try:
            response = self.emailrep.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()