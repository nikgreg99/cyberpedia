import logging
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class Cloudmersive(Collector):

    def __init__(self) -> None:
        
        super().__init_(__class__.__name__)

    def init_collector(self):
        self.api_key = self.secrets["api_key"]

    