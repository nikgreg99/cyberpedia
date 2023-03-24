import logging
import shodan
from shodan.exception import APIError
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logger = logging.getLogger(__name__)

class Shodan(Collector):


    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)

    def init_collector(self):
         self.api_key = self.secrets["api_key"]
         self.shodan = shodan.Shodan(self.api_key)


    def _host_details(self,ip):
        if validate_ip_address(ip):
            try:
                host = self.shodan.host(ip)
            except APIError as ex:
             pass
        return host

    #Premium API
    def _list_datasets(self):
        try:
            dataset_list = self.shodan.data.list_datasets()
        except APIError as ex:
            pass
        return dataset_list
    
    #Premium API
    def _list_dataset_file(self,dataset_name):
        dataset_list = self._list_datasets()
        for dataset in dataset_list:
            if dataset["name"] ==  dataset_name:
                try:
                    dataset_file = self.shodan.data.list_files(dataset=dataset_name) 
                    return dataset_file
                except APIError  as ex:
                    pass
    
    def _dns_domain(self,domain):
        try:
            domain = self.shodan.dns.domain_info(domain=domain, history=True, type=None)
        except APIError as ex:
            pass
        return domain
    

   