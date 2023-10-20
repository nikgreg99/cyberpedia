import logging
import shodan
from shodan.exception import APIError
from data_collector.classes import TargetCollector
from data_collector.utils import is_ip, validate_domain

logger = logging.getLogger(__name__)


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
        self.shodan = shodan.Shodan(self.api_key)

    def make_request(self, method="GET", final_url="", params={}, data={}):
        host = None
        target = data["target"]
        if is_ip(target):
            try:
                host = self.shodan.host(target)
            except APIError as ex:
                logger.exception(ex)
                host = {'error': 'No IP information available'}
        return host

    def collect_target(self, target):
        data = {'target': target}
        return self.make_request(data=data)
