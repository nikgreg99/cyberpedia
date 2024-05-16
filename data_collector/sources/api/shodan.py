import logging
import shodan
import time
from shodan.exception import APIError
from data_collector.classes import TargetCollector
from data_collector.utils import is_IP_adress
from data_collector.exceptions import UnsupportedTarget
from django.conf import settings

logger = logging.getLogger(__name__)

# STATUS: OK


class Shodan(TargetCollector):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Shodan, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.shodan = shodan.Shodan(key=self.api_key,proxies=settings.PROXIES)

    def make_request(self, method="GET", final_url="", params={}, data={}):
        target = data["target"]
        if is_IP_adress(target):
            try:
                host = self.shodan.host(target)
                time.sleep(1)
                return host
            except APIError as ex:
                logger.exception(ex)
        else:
            raise UnsupportedTarget("Target is not supported for analysis")

    def collect_target(self, target):
        data = {'target': target}
        return self.make_request(data=data)
