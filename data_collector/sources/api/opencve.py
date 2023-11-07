import base64
import requests
from requests import HTTPError
import logging
import enum
from data_collector.classes import  FeedCollector,TargetCollector
from django.conf import settings
from data_collector.utils import is_cve, process_data
from data_collector.helpers import get_env_var

logger = logging.getLogger(__name__)


class CVSSSeverity(enum.Enum):
    NONE = "NONE"
    LOW = "LOw"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"



class OpenCVE(FeedCollector,TargetCollector):

    base_url : str = get_env_var('OPENCVE_URL')
    opencve = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OpenCVE, cls).__new__(cls)
        return cls.instance


    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        username = self.secrets["username"]
        password = self.secrets["password"] 
        auth_message_bytes= f"{username}:{password}".encode()
        auth_base64 = base64.b64encode(auth_message_bytes).decode("ascii")
        self.opencve.headers = {
            "Authorization": f"Basic {auth_base64}",
            "Accept": "application/json"
        }
        self.err = {}
        self.opencve.proxies = settings.PROXIES

   
    def make_request(self,final_url,params={}):
        try:
            response = self.opencve.get(final_url,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.err["opencve"] = ex
        return response.json()
    
    def list_CVE(self):
        url_paged = []
        for i in range(20):
            final_url = self.base_url + f"/cve?page={str(i+1)}"
            url_paged.append(final_url)
        data = process_data(self.make_request,url_paged)
        
        return data

    
    def list_CWE(self):
        url_paged = []
        for i in range(68):
            final_url = self.base_url + f"/cwe?page={str(i+1)}"
            url_paged.append(final_url)
        data = process_data(self.make_request,url_paged)
        return data
    
    def list_vendors(self):
        url_paged = []
        for i in range(40):
            final_url = self.base_url + f"/vendors?page={str(i+1)}"
            url_paged.append(final_url)
        data = process_data(self.make_request,url_paged)
        return data

    def collect_target(self, target):
        return super().collect_target(target)
    
    def collect(self):
        cve = self.list_CVE()[0]
        cwe = self.list_CWE()[0]
        vendors = self.list_vendors()[0]
        return {
            'cve': cve,
            'cwe': cwe,
            'vendors': vendors
        }