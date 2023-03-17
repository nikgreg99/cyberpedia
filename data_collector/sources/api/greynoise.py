import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class GreyNoise(Collector):

    greynoise = requests.Session()