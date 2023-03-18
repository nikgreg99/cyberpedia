import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)


class AbuseIPDB(Collector):

    base_url : str = "https://api.abuseipdb.com/api/v2"
    abuseipdbb = requests.Session()

