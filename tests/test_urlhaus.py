from unittest import skip
from django.test import TestCase
from data_collector.sources.api.urlhaus import UrlHaus

class UrlScanTest(TestCase):

    test_client = UrlHaus()

    
    @skip
    def test(self):
        print(self.test_client.query_recent_URL())