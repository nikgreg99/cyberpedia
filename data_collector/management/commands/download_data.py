import os
import json
import logging
from django.conf import settings
from data_collector.sources.apps import sources
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def write_bulk_data(self,name,data):
        with open(os.path.join(settings.DATA_DIR,"{}.json").format(name),"w") as f:
            json.dump(data,f)

    def write_data_exploit_alert(self):
      oracle_info = sources["ExploitAlert"].collect_target('Oracle')
      adobe_info = sources["ExploitAlert"].collect_target('Adobe')
      apache_info = sources["ExploitAlert"].collect_target('Apache')  
      metasploit_info = sources["ExploitAlert"].collect_target('Metasploit')
      joomla_info = sources["ExploitAlert"].collect_target("Joomla")
      drupal_info = sources["ExploitAlert"].collect_target("Drupal")
      data = [oracle_info,adobe_info,apache_info,joomla_info,metasploit_info,drupal_info]
      self.write_bulk_data("exploit",data)

    def write_data_maldatabase(self):
        data = sources["Maldatabase"].collect()
        self.write_bulk_data("maldatabase",data)

    def write_data_yarify(self):
        data = sources["Yarify"].list_recent_deployed_rules()
        self.write_bulk_data("yarify",data)


    def honeydb_collect_twitter_feed(self):
        data = sources["HoneyDB"].collect_twitter_feed()
        self.write_bulk_data("honeydb_twitter_feed",data)

    def honeydb_collect_bad_ip(self):
         data = sources["HoneyDB"].collect_bad_ip()
         self.write_bulk_data("honeydb_bad_ip",data)

    def write_data_ip_info(self):
        data = sources["HoneyDB"].collect_bad_ip()
        ip_infos = []
        for bad_ip in data:
            remote_host = bad_ip["remote_host"]
        ip_infos.append(sources["IPInfo"].ip_info(remote_host))
        self.write_bulk_data("ipinfo",ip_infos)

    def have_i_been_pwned(self):
        data = sources["HaveIBeenPwned"].collect()
        self.write_bulk_data("haveibeenpwened",data)

    def threat_fox_ioc(self):
        data = sources["ThreatFox"].query_recent_IOC()
        self.write_bulk_data("threatfox_ioc",data)

    def threat_fox_malware_list(self):
        data = sources["ThreatFox"].get_malware_list()
        self.write_bulk_data("threatfox_malware_list",data)
    
    def opencve_cve(self):
        data = sources["OpenCVE"].list_CVE()
        self.write_bulk_data("opecve_cve",data)
    
    def opencve_cwe(self):
        data = sources["OpenCVE"].list_CWE()
        self.write_bulk_data("opencve_cwe",data)
        
    def url_feed(self):
        data = sources["UrlHaus"].query_recent_urls()
        self.write_bulk_data("urlhaus_urls",data)

    def payload_feed(self):
        data = sources["UrlHaus"].query_recent_payloads()
        self.write_bulk_data("urlhaus_payloads",data)

    def download_valhalla_feed(self):
        yara_rules,sigma_rules = sources["Valhalla"].collect()
        self.write_bulk_data("valhalla_yara",yara_rules)
        self.write_bulk_data("valhalla_sigma",sigma_rules)

    def handle(self, *args, **options):
      self.write_data_exploit_alert()
      self.write_data_yarify()
      self.honeydb_collect_bad_ip()
      self.honeydb_collect_twitter_feed()
      self.have_i_been_pwned()
     # self.write_data_maldatabase()
      self.threat_fox_ioc()
      self.threat_fox_malware_list()
      self.write_data_ip_info()
      #self.opencve_cve()
      #self.opencve_cwe()
      self.url_feed()
      self.payload_feed()
      self.download_valhalla_feed()
        
