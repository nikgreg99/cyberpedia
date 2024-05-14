import hashlib
import re
import ipaddress
import logging
import random

from cyberpedia.consts import HASH_TYPE_REGEX_MAP
from  validators import url, domain
from django.utils import timezone


import io
import csv
import json
import os

logger = logging.getLogger(__name__)

def get_current_timestamp():
      return timezone.now()


def get_current_timestamp_str():
      return str(get_current_timestamp())


def is_url_or_domain(input_str: str):
    if url(input_str):
          return "URL"
    elif domain(input_str):
         return "Domain"


def get_random_colorhex() -> str:
    # flake8: noqa
    r = lambda: random.randint(0,255)
    return "#%02X%02X%02X" % (r(),r(),r())

    
def get_ip_version(ip_address_str):
      """
        Returns IP Address Version
      """
      ip_version = None
      try:
        ip = ipaddress.ip_address(ip_address_str)
        ip_version = ip.version
      except ValueError as ex:
           logger.error(ex)
      return ip_version # Returns none if ip address is not valid


def encode_str(value_str: str):
     return value_str.encode('utf-8')


def calculate_md5_hash(value) -> str:
     input_bytes = encode_str(value)
     return hashlib.md5(input_bytes).hexdigest()


def calculate_sha1_hash(value) -> str:
     input_bytes = encode_str(value)
     return hashlib.sha1(input_bytes).hexdigest()


def calculate_sha256_hash(value) -> str:
     input_bytes = encode_str(value)
     return hashlib.sha256(input_bytes).hexdigest()


def calculate_sha512_hash(value) -> str:
     input_bytes = encode_str(value)
     return hashlib.sha512(input_bytes).hexdigest()


def get_hash_type(hash_str):
    """
        Determine a hash type given an hash string value
        Value supported: md5, sha1, sha256, sha512
    """
    detected_hash_type = None
    for hash_type, re_hash in HASH_TYPE_REGEX_MAP.items():
         if re.match(re_hash,hash_str):
              detected_hash_type = hash_type
              break
    return detected_hash_type # None if no match is  not found


def csv_to_json(csv_content):
    reader = csv.DictReader(io.StringIO(csv_content))
    return json.dumps(list(reader))


def read_json_file(file_path)-> dict:
         with open(file_path) as f:
              config_dict = json.load(f)
         return config_dict


def get_env_var(name):
        value = os.getenv(name)
        try:
            return json.loads(name)
        except(json.JSONDecodeError,TypeError):
            return value
 
