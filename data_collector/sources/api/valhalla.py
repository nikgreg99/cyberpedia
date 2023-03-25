from valhallaAPI.valhalla import ValhallaAPI
from data_collector.classes import Collector
import logging
import os

logger = logging.getLogger()

class Valhalla(Collector):

    def __init__(self):
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.valhalla = ValhallaAPI()

    def collect(self):
        yara_json = self.valhalla.get_rule_info()
        sigma_json = self.valhalla.get_sigma_rules_json()
        return yara_json ,sigma_json