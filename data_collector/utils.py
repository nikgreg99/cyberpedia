from .exceptions import InvalidIPAddress
from ipaddress import ip_address, IPv4Address,IPv6Address
import hashlib
import pyssdeep
import pefile

def validate_ip_address(ip: str):
    ip_checker = ip_address(ip)
    if type(ip_checker) is IPv4Address or type(ip_checker) is IPv6Address:
        return True
    else:
        raise InvalidIPAddress("IP is not in a valid format")
    

def compute_md5(plaintext):
    return hashlib.md5(plaintext).digest()

def computer_sha1(plaintext):
    return hashlib.sha1(plaintext).digest()

def compute_sha256(plaintext):
    return hashlib.sha256(plaintext).digest()

def compute_ssdeep(plaintext):
    return pyssdeep.get_hash_buffer(plaintext)

def compute_imphash(file_path):
    return pefile.PE(file_path).get_imphash()
  
   





