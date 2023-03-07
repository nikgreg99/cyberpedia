import shodan
from data_collector.exceptions import ErrorRequestException

class Shodan():

    shodan = None
    api_key = None

    def set_paramaters(self):
         self.api_key = ""
         self.shodan = shodan.Shodan(self.api_key)


    def _host_details(self,ip):
        try:
            host = self.shodan.host(ip)
        except ErrorRequestException as ex:
            pass
        return host

    #Premium API
    def _list_datasets(self):
        try:
            dataset_list = self.shodan.data.list_datasets()
        except ErrorRequestException as ex:
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
                except ErrorRequestException as ex:
                    pass
    
    def _dns_domain(self,domain):
        try:
            domain = self.shodan.dns.domain_info(domain=domain, history=True, type=None)
        except  as ex:
            pass
        return domain
    

   