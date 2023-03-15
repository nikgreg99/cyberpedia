from django.test import TestCase
from data_collector.sources.api.threat_fox import ThreatFox

class ThreatFoxTest(TestCase):

    client_test = ThreatFox()

    def setUp(self):
        pass

    def test_download_IOC(self):
        print(self.client_test._search_IOC_by_target('8.8.8.8'))
        print(self.client_test.get_malware_list())

            
    

