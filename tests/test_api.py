import pytest

from django.test import TestCase
from django.core.management import call_command
from data_collector.sources.api.maldatabase import Maldatabase


class APITest(TestCase):

    fixtures = [
        "api_test.json"
    ]

    #maldatabase = Maldatabase()

    def setUp(self) -> None:
        call_command('loaddata',self.fixtures)
       # self.maldatabase.init_collector()



    
    def test_collect(self):
        print(self.maldatabase.collect())