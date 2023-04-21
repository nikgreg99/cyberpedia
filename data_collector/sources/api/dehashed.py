import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

class DeHashed(Collector):

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    