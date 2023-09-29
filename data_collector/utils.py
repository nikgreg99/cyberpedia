from .exceptions import InvalidCVEFormat, InvalidHashFormat, InvalidIPAddressFormat, InvalidEmailFormat, InvalidURLFormat, InvalidDomainFormat, InvalidHostFormat
from .constants import HashType, CVE_REGEX, MD5_HASH_REGEX, SHA1_HASH_REGEX, SHA_256_REGEX, SSDEEP_REGEX, EMAIL_ADDRESS_REGEX, URL_REGEX, DOMAIN_REGEX, HOST_REGEX
from ipaddress import ip_address, IPv4Address,IPv6Address
import hashlib
import pyssdeep
import pefile
import re

def validate_ip_address(ip: str):
    ip_checker = ip_address(ip)
    if type(ip_checker) is IPv4Address or type(ip_checker) is IPv6Address:
        return True
    raise InvalidIPAddressFormat(f"{ip} is not in a valid format")
    
def validate_hash(content,regexp):
    return re.match(content,regexp)
    
def get_hash_type(hash):
    if validate_hash(hash,MD5_HASH_REGEX):
        return HashType.MD5 

    if validate_hash(hash,SHA1_HASH_REGEX):
        return HashType.SHA1
  
    if validate_hash(hash,SHA_256_REGEX):
        return HashType.SHA256

    if validate_hash(hash,SSDEEP_REGEX):
        return HashType.SSDEEP

    raise InvalidHashFormat(f"{hash} is not of the types available")
  

def validate_cve_format(cve):
    match = re.match(cve,CVE_REGEX)
    if match:
        return True
    raise InvalidCVEFormat(f"{cve} is not in a valid CVE format")


def validate_email_adddress(email):
    match = re.match(email,EMAIL_ADDRESS_REGEX)
    if match:
        return True
    raise InvalidEmailFormat (f"{email} is not a valid email-address")
    
def validate_url(url):
    match = re.match(url,URL_REGEX)
    if match:
        return True
    raise InvalidURLFormat(f"{url} is not a valid url")

def validate_domain(domain):
    match = re.match(domain,DOMAIN_REGEX)
    if match:
        return True
    raise InvalidDomainFormat(f"{domain} is not valid domain")
   
def validate_host(host):
     match = re.match(host,HOST_REGEX)
     if match:
        return True
     raise InvalidHostFormat(f"{host} is not a valid hostname")
   

def compute_md5(plaintext):
     hashlib.md5(plaintext).digest()

def computer_sha1(plaintext):
    return hashlib.sha1(plaintext).digest()

def compute_sha256(plaintext):
    return hashlib.sha256(plaintext).digest()

def compute_ssdeep(plaintext):
    return pyssdeep.get_hash_buffer(plaintext)

def compute_imphash(file_path):
    return pefile.PE(file_path).get_imphash()





