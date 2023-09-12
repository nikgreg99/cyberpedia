import base64
import requests
from requests import HTTPError
import logging
from data_collector.classes import  FeedCollector,TargetCollector
from django.conf import settings
from data_collector.utils import validate_cve_format
from data_collector.helpers import get_env_var

logger = logging.getLogger(__name__)


class OpenCVE(FeedCollector,TargetCollector):

    _self = None
    base_url : str = get_env_var('OPENCVE_URL')
    opencve = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        username = self.secrets["username"]
        password = self.secrets["password"] 
        auth_message_bytes= f"{username}:{password}".encode()
        auth_base64 = base64.b64encode(auth_message_bytes).decode("ascii")
        self.opencve.headers = {
            "Authorization": f"Basic {auth_base64}",
            "Accept": "application/json"
        }
        self.opencve.proxies = settings.PROXIES

    def make_requests_open_cve(self,final_url):
        try:
            response = self.opencve.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()
    
    def list_CVE(self):
        final_url = self.base_url + "/cve"
        return self.make_requests_open_cve(final_url)
    
    def get_CVE_by_id(self,CVE):
        if validate_cve_format(CVE):
            final_url = self.base_url + f"/cve/{CVE}"
            return self.make_requests_open_cve(final_url)
        
    def get_CWE_by_id(self,CWE):
        final_url = self.base_url + f"/cwe/{CWE}"
        return self.make_requests_open_cve(final_url)
    
    def list_CWE(self):
        final_url = self.base_url + "/cwe"
        return self.make_requests_open_cve(final_url)
    
    def list_vendors(self):
        final_url = self.base_url + "/vendors"
        return self.make_requests_open_cve(final_url)

    def list_vendors_by_name(self,name):
        final_url = self.base_url + f"/vendors/{name}" 
        return self.make_requests_open_cve(final_url)
    
    def list_vendors_name_by_CVE(self,name):
        final_url = self.base_url + f"/vendors/{name}/CVE"
        return self.make_requests_open_cve(final_url)
    
    def list_products(self,vendor_name):
        final_url = self.base_url + f"/vendors/{vendor_name}/products"
        return self.make_requests_open_cve(final_url)
 
    def collect_target(self, target):
        return super().collect_target(target)
    
    def collect(self):
        return self.list_CVE(),self.list_CWE(),self.list_vendors(),self.list_products()