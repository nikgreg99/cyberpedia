import ipaddress

from logging import getLogger

from django.db import models
from data_collector.helpers import is_url_or_domain, get_hash_type, is_CVE

logger = getLogger(__name__)                                                                                                                                                                                                                                                               


class TypeChoices(models.TextChoices):
     FILE = "File"
     IOC = "IOC"

class HashChoices(models.TextChoices):
    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"
    SSDEEP = "ssdeep"


class IOCTypes(models.TextChoices):
    IP = "ip"
    DOMAIN = "domain"
    URL = "url"
    HASH = "hash"
    CVE = "cve"
    GENERIC = "generic"

    @classmethod
    def classify_value(cls,value: str) -> str:
        """
            Return ioc classification given a particular value.
            Possibile values are: ip, domain, url, hash and generic

            Arg:
                value (str)
            Returns:
                ip,domain,url,hash or generic
        """
        try:
            ipaddress.ip_address(value)
            classification = cls.IP
        except ValueError:
            outcome = is_url_or_domain(value)
            if outcome == "url":
                classification = cls.URL
            elif outcome == "domain":
                classification == cls.DOMAIN
            elif get_hash_type(value) is not None:
                 classification = cls.HASH
            elif is_CVE(value):
                    classification = cls.CVE
            else:
                classification = cls.GENERIC
                logger.info(f"Couldn't classify {value} as a particular ioc,
                            setting it as generic")
        return classification

class AllIOCTypes(models.TextChoices):
     
     IP = "ip"
     DOMAIN = "domain"
     URL = "url"
     HASH = "hash"
     CVE = "cve"
     FILE = "file"