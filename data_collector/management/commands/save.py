from django.core.management import BaseCommand
from data_collector.downloaders.feed.valhalla_downloader import ValhallaDownloader
from data_collector.apps import sources

class Command(BaseCommand):

    def handle(self, *args, **options):
        bad_ip,twitter_ip = sources["HoneyDB"].collect()      
        print(bad_ip)
        print(twitter_ip) 

        adobe = sources["ExploitAlert"].collect_target('Adobe')
        print(adobe)

        ip_info = sources["Shodan"].collect_target('8.8.8.8')
        print(ip_info)

        yarify = sources["Yarify"].collect()
        print(yarify)

        malwarebazaar = sources["MalwareBazaar"].collect()
        print(malwarebazaar)

        vt = sources["VirusTotal"].collect_target("1.1.1.1")
        print(vt)

        whois = sources["Whois"].collect_target("8.8.8.8")
        print(whois)

        maldatabase = sources["Maldatabase"].collect()
        print(maldatabase)


        abuse = sources["AbuseIPDB"].collect_target('1.1.1.1')
        print(abuse)

        ipinfo = sources["IPInfo"].collect_target("10.246.50.3")
        print(ipinfo)

        shodan = sources["Shodan"].collect_target("8.8.8.8")
        print(shodan)

        