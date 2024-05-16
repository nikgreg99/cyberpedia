import querycontacts

from data_collector.classes import TargetCollector


class Abusix(TargetCollector):
    """
     Wrapper class to find abuse contacts for a given IP address
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Abusix, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()   

    def init_collector(self):
        self.cf = querycontacts.ContactFinder()

    def collect_target(self,observable) -> dict:
        result = {}
        ip_addr = observable
        abuse_contacts = self.cf.find(ip_addr)
        if not abuse_contacts:
            abuse_contacts = []
        result["abuse_contacts"] = abuse_contacts
        return result
