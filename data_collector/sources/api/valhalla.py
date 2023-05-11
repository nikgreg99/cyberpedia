from valhallaAPI.valhalla import ValhallaAPI
from valhallaAPI.valhalla import ApiError
from data_collector.classes import FeedCollector
import logging
from django.conf import settings

logger = logging.getLogger()

class Valhalla(FeedCollector):

    def __init__(self):
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.valhalla = ValhallaAPI(api_key=self.api_key)
        self.valhalla.proxies = settings.PROXIES

    def collect(self):
        try:
            yara_json = self.valhalla.get_rules_json()
            sigma_json = self.valhalla.get_sigma_rules_json()
        except ApiError as ex:
            logger.exception(ex)
        return yara_json ,sigma_json
    
    def download_public_yara_rules(self):
        try:
            return self.valhalla.get_sigma_rules_zip()
        except ApiError as ex:
            logger.exception(ex)
    
    def download_public_sigma_rules(self):
        try:
            return self.valhalla.get_sigma_rules_zip()
        except ApiError as ex:
            logger.exception(ex)