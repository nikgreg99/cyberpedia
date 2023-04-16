import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class EmergingThreats(Collector):

    emerging_threats = requests.Session()

    file_rules = [
        "botcc.rules",
        "ciarmy.rules",
        "compromised.rules",
        "drop.rules",
        "dshield.rules",
        "emerging-activex.rules",
        "emerging-attack_response.rules",
        "emerging-chat.rules",
        "emerging-current_events.rules",
        "emerging-deleted.rules",
        "emerging-dns.rules",
        "emerging-dos.rules",
        "emerging-exploit.rules",
        "emerging-ftp.rules",
        "emerging-games.rules",
        "emerging-icmp.rules",
        "emerging-icmp_info.rules",
        "emerging-imap.rules",
        "emerging-inappropriate.rules",
        "emerging-info.rules",
        "emerging-malware.rules",
        "emerging-misc.rules",	
        "emerging-mobile_malware.rules",
        "emerging-netbios.rules",
        "emerging-p2p.rules	"
        "emerging-policy.rules",
        "emerging-pop3.rules",
        "emerging-rpc.rules	",
        "emerging-scada.rules",
        "emerging-scan.rules",
        "emerging-shellcode.rules",
        "emerging-smtp.rules",
        "emerging-snmp.rules",
        "emerging-sql.rules",
        "emerging-telnet.rules",
        "emerging-tftp.rules",
        "emerging-trojan.rules",
        "emerging-user_agents.rules",
        "emerging-voip.rules",
        "emerging-web_client.rules",
        "emerging-web_server.rules",
        "emerging-web_specific_apps.rules",
        "emerging-worm.rules"
    ]

    file_rules_block_rules = [
        "emerging-botcc.portgrouped.suricata.rules"
        "emerging-botcc.suricata.rules",
        "emerging-ciarmy.suricata.rules",
        "emerging-compromised.suricata.rules"
        "emerging-drop.suricata.rules",
        "emerging-dshield.suricata.rules",
        "emerging-tor.suricata.rules",
        "threatview_CS_c2.suricata.rules",
    ]

	
    base_url_suricata_rules: str = "https://rules.emergingthreats.net/open-nogpl/suricata-5.0/rules"
    base_url_block_rules: str = "https://rules.emergingthreats.net/blockrules"
    emerging_threats = requests.Session()

    def __init__(self) -> None:
        super().__init__(__class__.__name__)

    def init_collector(self):
        self.headers = {
            'Authorization': self.secrets["api_key"]
        }

    def suricata_feed(self,file_rules:dict):
        files = {}
        for file_rule in self.file_rules:
            final_url = self.base_url_suricata_rules + f"/{file_rule}"
            try:
                response = self.emerging_threats.get(final_url)
                response.raise_for_status()
            except HTTPError as ex:
                logger.exception(ex)

            files[file_rule] = response.text
        
        return files
    
    
    def downoload_suricata_feeds(self):
        rules = self.suricata_feed(self.file_rules)
        rules_blocked = self.suricata_feed(self.file_rules_block_rules)
        return rules,rules_blocked

    
    