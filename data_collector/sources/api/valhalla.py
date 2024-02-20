from valhallaAPI.valhalla import ValhallaAPI
from valhallaAPI.valhalla import ApiError
from data_collector.classes import FeedCollector
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

#STATUS: OK
class Valhalla(FeedCollector):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Valhalla, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.valhalla = ValhallaAPI(api_key=self.api_key)
        self.valhalla.proxies = settings.PROXIES
        self.error = {}

    def collect(self):
        try:
            yara_json = self.valhalla.get_rules_json()
            sigma_json = self.valhalla.get_sigma_rules_json()
        except ApiError as ex:
            logger.exception(ex)
            self.error["valhalla"] = ex
        return yara_json ,sigma_json
