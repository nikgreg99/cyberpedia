import enum

class HashType(enum):
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SSDEEP = "ssdeep"


class TargetType(enum):
    IP = "IP"
    URL = "URL"
    HASH = "Hash"
    DOMANIN = "Domain"
    GENERIC = "Generic"