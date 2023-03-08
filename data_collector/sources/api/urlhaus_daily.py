import os
import requests
from data_collector.exceptions import ErrorRequestException

class UrlHausDaily():

    base_misp_daily_url = "https://urlhaus.abuse.ch/downloads/misp/"
    base_suricata_daily_url = "https://urlhaus.abuse.ch/downloads/suricata-ids/"

    def _collect_daily_misp(self):
        try:
            manifest_response = requests.get(self.base_misp_daily_url.join("/manifest.json"))
            manifest_response.raise_for_status()
        except ErrorRequestException as ex:
            raise ErrorRequestException
        
        manifest = manifest_response.json()
        misp_daily_rules = list()

        for misp_uuid in manifest.keys():
            try:
                misp_file_string = "/{}.json".format(misp_uuid)
                misp_rule = requests.get(self.base_misp_daily_url.join(misp_file_string))
                misp_rule.raise_for_status()
                misp_daily_rules.append(misp_rule.json())
            except ErrorRequestException as ex:
                raise ErrorRequestException

        return misp_daily_rules    

    def _collect_daily_suricata(self):   
        try:
            snort_file_response = requests.get(self.base_suricata_daily_url)
            snort_file_response.raise_for_status()
        except ErrorRequestException as ex:
            pass
            
        snort_file = snort_file_response.content
         
         #Use of a dummy file to retrieve rules and parse it correclty
        with open("dummy_snort.txt","w") as dummy_snort_file:
            dummy_snort_file.write(snort_file)
            snort_lines = dummy_snort_file.readlines()
            deletion_range_list = [i for i in range(10)]
            snort_rules_str = [j for i,j in enumerate(snort_lines)
                              if i not in deletion_range_list]
            snort_rules_str.remove(snort_rules_str.count() -1)
            snort_rules = list()
            for i in range (0,snort_rules_str.count(),3):
                snort_rules.append("{}{}{}".format(snort_rules_str[i],snort_rules_str[i+1],snort_rules_str[i+2]))

        
        os.remove("dummy_snort.txt")

        return snort_rules
    
    def collect(self):
        self._collect_daily_misp()
        self._collect_daily_suricata()


