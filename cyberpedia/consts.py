import re

# Hashing

MD5_REGEX = r"^[a-f\d]{32}$"
SHA1_REGEX = r"^[a-f\d]{40}$"
SHA_256_REGEX = r"^[a-f\d]{64}$"
SHA_512_REGEX = r"^[a-f\d]{128}$"

HASH_TYPE_REGEX_MAP = {
    "md5": re.compile(MD5_REGEX, re.IGNORECASE | re.ASCII),
    "sha1": re.compile(SHA1_REGEX, re.IGNORECASE | re.ASCII),
    "sha256": re.compile(SHA_256_REGEX, re.IGNORECASE | re.ASCII),
    "sha512": re.compile(SHA_512_REGEX, re.IGNORECASE | re.ASCII)
}

# CVE

CVE_REGEX = r"CVE-\d{4}-\d{4,}$"

# Email

EMAIL_REGEX = r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
