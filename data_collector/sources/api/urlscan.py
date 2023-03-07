import requests
from data_collector.exceptions import ErrorRequestException


class UrlScan():
    base_url : str = "https://urlscan.io/api/v1"
    api_key = None
    urlscan = requests.Session()

    def set_parameters():
        pass

    def _make_request(self,url):
        try:
            response = self.urlscan.get(query_URL)
            response.raise_for_status()
        except ErrorRequestException as ex:
            pass
        return response.json()

    def query_recent_URL(self,limit: int =None):
        basic_url = "/urls/recent"
        query_URL = self.base_url.join(basic_url)
        if limit is not None:
            query_URL.join("/limit/{}".format(str(limit)))
        return self._make_request(query_URL)
      
    
     def query_recent_payloads(self,limit: int =None):
        basic_url = "/payloads/recent"
        query_URL = self.base_url.join(basic_url)
        if limit is not None:
            query_URL.join("/limit/{}".format(str(limit)))
        return self._make_request(query_URL)
