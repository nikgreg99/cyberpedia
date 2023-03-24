from django.db import models

CVE_REGEX = r"CVE-\d{4}-\d{4,7}"

MD5_HASH_REGEX = "^[a-fA-F0-9]{32}$"
SHA1_HASH_REGEX = "^[a-fA-F0-9]{40}"
SHA_256_REGEX = "^[a-fA-F0-9]{64}$"
SSDEEP_REGEX = "((\d*):(\w*):(\w*)|(\d*):(\w*)\+(\w*):(\w*))"


class DataFeedFormat(models.TextChoices):
    YARA = "Yara"
    STIX = "STIX"
    SIGMA = "SIGMA"
    SURICATA = "Suricata"
    OPEN_IOC = "Open_IOC"
    MISP = "MISP"
    OTHER = "Other"


class HashType(models.TextChoices):
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SSDEEP = "ssdeep"

class CollectorType(models.TextChoices):
    FILE = "File"
    TARGET = "Target"


class ObservableType(models.TextChoices):
    IP = "IP"
    URL = "URL"
    HASH = "Hash"
    DOMANIN = "Domain"
    CVE = "CVE"
    GENERIC = "Generic"



