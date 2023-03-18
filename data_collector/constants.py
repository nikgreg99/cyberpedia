import enum

MD5_HASH_REGEX = "^[a-fA-F0-9]{32}$"
SHA1_HASH_REGEX = "^[a-fA-F0-9]{40}"
SHA_256_REGEX = "^[a-fA-F0-9]{64}$"

class HashType(enum):
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SSDEEP = "ssdeep"
    IMPASH = "impash"

class CollectorType(enum):
    FILE = "File"
    TARGET = "Target"


class TargetType(enum):
    IP = "IP"
    URL = "URL"
    HASH = "Hash"
    DOMANIN = "Domain"
    GENERIC = "Generic"