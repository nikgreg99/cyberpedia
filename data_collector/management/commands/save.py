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


       



        