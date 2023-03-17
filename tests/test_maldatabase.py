from unittest import skip
from django.test import TestCase
from data_collector.sources.api.maldatabase import Maldatabase


class MaldatabaseTest(TestCase):

    client_test = Maldatabase()

    def setUp(self) -> None:
        pass

    @skip
    def test_collect(self):
        print(self.client_test.collect())