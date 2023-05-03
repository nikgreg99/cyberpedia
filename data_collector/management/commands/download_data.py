import os
import json
import logging
from django.conf import settings
from data_collector.sources.apps import sources
from django.core.management.base import BaseCommand
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager

logger = logging.getLogger(__name__)
mongo = MongoManager()
elastic = ElasticManager()

class Command(BaseCommand):

    def write_bulk_data(self,name,data):
        with open(os.path.join(settings.DATA_DIR,"{}.json").format(name),"w") as f:
            json.dump(data,f)

    def write_data_exploit_alert(self):
      oracle_info = sources["ExploitAlert"].collect_target('Oracle')
      adobe_info = sources["ExploitAlert"].collect_target('Adobe')
      apache_info = sources["ExploitAlert"].collect_target('Apache')  
      metasploit_info = sources["ExploitAlert"].collect_target('Metasploit')
    

      mongo.save_data('ExploitAlert',oracle_info)
      mongo.save_data('ExploitAlert',adobe_info)
      mongo.save_data('ExploitAlert',apache_info)
      mongo.save_data('ExploitAlert',metasploit_info)
      elastic.insert_data_bulk('exploit_alert',oracle_info)
      elastic.insert_data_bulk('exploit_alert',adobe_info)
      elastic.insert_data_bulk('exploit_alert',apache_info)
      elastic.insert_data_bulk('exploit_info',metasploit_info)

    def write_data_maldatabase(self):
        data = sources["Maldatabase"].collect()

    def write_data_yarify(self):
        data = sources["Yarify"].list_recent_deployed_rules()
        elastic.insert_data_bulk('yarify',data)
        mongo.save_data_one('Yarify',data)


    def honeydb_collect_twitter_feed(self):
        data = sources["HoneyDB"].collect_twitter_feed()
        elastic.insert_data_bulk("honeydb-bad-ip",data)
        mongo.save_data('HoneyDB_twitter_feed',data)

    def honeydb_collect_bad_ip(self):
         data = sources["HoneyDB"].collect_bad_ip()
         elastic.insert_data_bulk("honey-db-twitter-feed",data)
         mongo.save_data('HoneyDB_bad_ip',data)
      

    def write_data_ip(self):
        data = sources["HoneyDB"].collect_twitter_feed()
        ip_infos = []
        shodan = []
        whois = []
        for bad_ip in data:
            remote_host = bad_ip["remote_host"]
            shodan.append(sources["Shodan"].host_details(remote_host))
        elastic.insert_data_bulk('shodan',shodan)
        mongo.save_data('shodan',shodan)

    def have_i_been_pwned(self):
        data = sources["HaveIBeenPwned"].collect()
        print(data)
        elastic.insert_data_bulk('have_i_been_pwned',data)
        mongo.save_data('HaveIBeenPwned',data)
       

    def threat_fox_ioc(self):
        data = sources["ThreatFox"].query_recent_IOC()
        print(data)
        elastic.insert_data_bulk('threat_fox_ioc',data)
        mongo.save_data_one("threat_fox_ioc",data)
      

    def threat_fox_malware_list(self):
        data = sources["ThreatFox"].get_malware_list()
        print(data)
        elastic.insert_data_bulk("threat_fox_malware_list",data)
        mongo.save_data_one("threat_fox_malware_list",data)

    def urlhaus_payloads(self):
        data = sources['UrlHaus'].query_recent_urls()
        print(data)
        elastic.insert_data_bulk("urlahus_payloads",data)
        mongo.save_data_one('urlahus_payloads,data',data)
        
    def urlahus_url(self):
        data = sources['UrlHaus'].query_recent_urls()
        print(data)
        elastic.insert_data_bulk("urlaus_urls",data)
        mongo.save_data_one("urlahus_urls",data)
        
    
    def opencve_cve(self):
        data = sources["OpenCVE"].list_CVE()
       
    
    def opencve_cwe(self):
        data = sources["OpenCVE"].list_CWE()
    
    
    def koodous_feed_apk(self):
        feed_apks = sources['Koodous'].apks()
        mongo.save_data_one('Koodous_apks',feed_apks)
       
    
    def download_valhalla_feed(self):
        yara_rules,sigma_rules = sources["Valhalla"].collect()
        elastic.insert_data_bulk("valhalla_yara",yara_rules)
        elastic.insert_data_bulk("valhalla_sigma",sigma_rules)
        mongo.save_data_one('Valhalla_Yara',yara_rules)
        mongo.save_data_one('Valhalla_Sigma',sigma_rules)

    def threat_jammer_feed(self):
        data = sources["ThreatJammer"].collect()
        print(data)
        elastic.insert_data_bulk('threat_jammer',data)
        mongo.save_data_one('threat_jammer',data)
        

    def handle(self, *args, **options):
      #self.write_data_exploit_alert()
      #self.write_data_ip()
      self.koodous_feed_apk()
      self.threat_jammer_feed()
     
        
