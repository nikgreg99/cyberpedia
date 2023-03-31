from valhallaAPI.valhalla import ValhallaAPI
from valhallaAPI.valhalla import ApiError
from data_collector.classes import Collector
import logging

logger = logging.getLogger()

class Valhalla(Collector):

    def __init__(self):
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.valhalla = ValhallaAPI(api_key=self.api_key)

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
    
    def downoad_public_sigma_rules(self):
        try:
            return self.valhalla.get_sigma_rules_zip()
        except ApiError as ex:
            logger.exception(ex)