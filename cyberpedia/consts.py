import re

# IP Regex

IPV4_REGEX = r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
IPV6_REGEX = r"^((([0-9a-fA-F]){1,4})\\:){7}([0-9a-fA-F]){1,4}$"

# Hashing

MD5_REGEX = r"^[a-f\d]{32}$"
SHA1_REGEX = r"^[a-f\d]{40}$"
SHA_256_REGEX = r"^[a-f\d]{64}$"
SHA_512_REGEX = r"^[a-f\d]{128}$"
SSDEEP_REGEX = r"^((\d*):(\w*):(\w*)|(\d*):(\w*)\+(\w*):(\w*))$"


HASH_TYPE_REGEX_MAP = {
    "md5": re.compile(MD5_REGEX, re.IGNORECASE | re.ASCII),
    "sha1": re.compile(SHA1_REGEX, re.IGNORECASE | re.ASCII),
    "sha256": re.compile(SHA_256_REGEX, re.IGNORECASE | re.ASCII),
    "sha512": re.compile(SHA_512_REGEX, re.IGNORECASE | re.ASCII),
    "ssdeep": re.compile(SSDEEP_REGEX, re.IGNORECASE | re.ASCII)
}

# CVE

CVE_REGEX = r"^CVE-\d{4}-\d{4,}$"

# Email

EMAIL_REGEX = r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
