from enum import Enum

class APIName(Enum):
    IPAPI = 'IPApi'
    IPINFO = 'IPInfo'
    IPAPI_COM = 'IPApiCom'

    @classmethod
    def choices(cls):
        return [(i,i.value) for i in cls]
