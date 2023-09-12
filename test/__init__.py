import logging
from django.test import TestCase
from django.conf import settings


def get_logger():
    logger = logging.getLogger(__name__)
    if settings.DISABLE_LOGGING_TEST:
        logging.disable(logging.CRITICAL)
    return logger

class CustomTestAPICase(TestCase):

    api = None

    def setUp(self) -> None:
         super().setUp()
        