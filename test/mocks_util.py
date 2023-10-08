from dataclasses import dataclass

from django.conf import settings
from unittest.mock import MagicMock,patch

class MockUpResponse():
    @dataclass
    class Request():
        def _init_(self):
            self.url = None

    