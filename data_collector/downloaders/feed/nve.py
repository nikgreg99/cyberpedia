import logging
import time
from .feed_downloader import FeedDownloader
from django.conf import settings
from data_collector.sources.api.nist import Nist

logger = logging.getLogger(__name__)

class NVECollector(FeedDownloader):

    SLEEP_TIME_INTERVAL = 6
    START_INDEX_DEFAULT = 0
    RESULTS_PER_PAGE_DEFAULT = 2000

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NVECollector, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__()
        self.nve = Nist()
        self.params = {
            'startIndex': self.START_INDEX_DEFAULT,
            'resultsPerPage': self.RESULTS_PER_PAGE_DEFAULT
        }

    def reset_params(self):
        self.params["startIndex"] = self.SLEEP_TIME_INTERVAL
        self.params["resultsPerPage"] = self.RESULTS_PER_PAGE_DEFAULT

    # This method is reccomended by NVD vulnerability database https://nvd.nist.gov/developers/api-workflows
    def collect_cve_feed(self):
        while True:
            data = self.nve.make_request(params=self.params)
            cve = data['vulnerabilities']
            self.params["startIndex"] +=  self.params['resultsPerPage']
            if settings.DEBUG:
                logger.info(cve)
            self.elastic.insert('nist-cve',cve)
            if self.params["startIndex"] > data["totalResults"]:
                break
            if settings.DEBUG: 
                logger.info("Wait for another request...")
            time.sleep(self.SLEEP_TIME_INTERVAL)

    def append_cve_feed(self,num_cve):
        self.reset_params()
        response = self.nve.make_request(self.params)
        total_cve = response["totalResults"]
        remaining_cve = total_cve - num_cve
        self.params["startIndex"] = num_cve
        self.collect_cve_feed()
        if settings.DEBUG:
            logger.info(f"NVE updated with new {remaining_cve} records")


    def download_feed(self):
        num_cve = self.elastic.count_doc_index('nist-cve')
        if num_cve == 0:
            self.collect_cve_feed()
        else: 
            self.append_cve_feed(num_cve)
        
    
    

