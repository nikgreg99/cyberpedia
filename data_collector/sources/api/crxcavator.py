import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_cve
from django.conf import settings

logger = logging.getLogger(__name__)


class CRXavator(TargetCollector):

    crx_cavator = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
         cls.instance = super(CRXavator, cls).__new__(cls)
        return cls.instancE