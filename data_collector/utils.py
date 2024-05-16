from .constants import  CVE_REGEX,  URL_REGEX, DOMAIN_REGEX, HOST_REGEX
from ipaddress import ip_address, IPv4Address,IPv6Address
import re
import concurrent

def is_IP_adress(ip: str):
    try:
        ip_checker = ip_address(ip)
   
        if type(ip_checker) is IPv4Address or type(ip_checker) is IPv6Address:
            return True
        return False
    except ValueError as ex:
        pass

def is_cve(cve):
    match = re.match(cve,CVE_REGEX)
    return True if match is not None else False

def is_url(url):
    match = re.match(url,URL_REGEX)
    return True if match is not None else False

def is_domain(domain):
    match = re.match(domain,DOMAIN_REGEX)
    return True if match is not None else False 
   
def is_host(host):
     match = re.match(host,HOST_REGEX)
     return True if match is not None else False
   

def process_data(f,data):
    parallel_data = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(f,url): url for url in data}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                response = future.result()
                parallel_data.append(response)
            except Exception as ex:
                pass
    return parallel_data







