from exceptions import InvalidIPAddress
from ipaddress import ip_address, IPv4Address,IPv6Address


def validate_ip_address(ip: str):
    ip_checker = ip_address(ip)
    if type(ip_checker) is IPv4Address or type(ip_checker) is IPv6Address:
        return True
    else:
        raise InvalidIPAddress("IP is not in a valid format")





