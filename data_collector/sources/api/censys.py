import requests
from requests import HTTPError
from data_collector.classes import Collector
import logging

logger = logging.getLogger()

class Censys(Collector):

    censys = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)


    