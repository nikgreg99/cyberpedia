import os
import json
from pymisp import PyMISP
from .connector import Connector
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

class MISPConnector(object):
    

    def __init__(self) -> None:
        url = settings.MISP_URL
        auth_key = settings.MISP_KEY
        verify_cert = settings.MISP_VERIFY_CERT
        self.misp = PyMISP(url,auth_key,verify_cert,'json',debug=True)
        self.headers = {
            "Authorization": settings.MISP_AUTH_KEY,
            "Accept": "application/json",
            "Content-type": "application/json"
        }
        
    def get_misp_feed(self,feed_name):
        return self.misp.get_feed(feed_name)



        