import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import validate_cve_format
from django.conf import settings

logger = logging.getLogger(__name__)


class CRCCavator(TargetCollector):

    crx_cavator = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
         cls.instance = super(CRCCavator, cls).__new__(cls)
        return cls.instance