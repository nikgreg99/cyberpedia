from django.db import models

IPV4_REGEX = "^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"
HOST_REGEX = "(?:(?:(?:(?:[a-zA-Z0-9][-a-zA-Z0-9]{0,61})?[a-zA-Z0-9])[.])*(?:[a-zA-Z][-a-zA-Z0-9]{0,61}[a-zA-Z0-9]|[a-zA-Z])[.]?)"
DOMAIN_REGEX = "“^((?!-)[A-Za-z0-9-]{1, 63}(?<!-)\\.)+[A-Za-z]{2, 6}$” "
CVE_REGEX = r"CVE-\d{4}-\d{4,7}"
URL_REGEX = "^(https?:\/\/)?[0-9a-zA-Z]+\.[-_0-9a-zA-Z]+\.[0-9a-zA-Z]+$"

# Hash regex
MD5_HASH_REGEX = "^[a-fA-F0-9]{32}$"
SHA1_HASH_REGEX = "^[a-fA-F0-9]{40}"
SHA_256_REGEX = "^[a-fA-F0-9]{64}$"
SSDEEP_REGEX = "((\d*):(\w*):(\w*)|(\d*):(\w*)\+(\w*):(\w*))"


class HashType(models.TextChoices):
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SSDEEP = "ssdeep"

class ObservableType(models.TextChoices):
    IP = "IP"
    URL = "URL"
    HASH = "Hash"
    DOMANIN = "Domain"
    CVE = "CVE"
    GENERIC = "Generic"



