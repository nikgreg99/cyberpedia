import logging
import requests
from requests import HTTPError
from data_collector.classes import FileAnalyzer


logger = logging.getLogger(__name__)


class FileScan(FileAnalyzer):
    
  