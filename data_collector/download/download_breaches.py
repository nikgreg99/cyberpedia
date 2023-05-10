import logging
from data_collector.download.data_download import DataDownloader
from data_collector.sources.apps import sources
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager

logger = logging.getLogger(__name__)


HAVE_I_BEEN_PWNED = "HaveIBeenPwned"
THREAT_JAMMER = "THREAT_JAMMER"

elastic = ElasticManager()
mongo = MongoManager()

class BreachDownloader(DataDownloader):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self


    def download_data(self):
        data = sources[HAVE_I_BEEN_PWNED].collect()
        elastic.insert_data_bulk('have_i_been_pwned',data)
        mongo.save_data(HAVE_I_BEEN_PWNED,data)
        data_threat = sources[THREAT_JAMMER].collect()
        elastic.insert_data_bulk('threat_jammer',data_threat)
        mongo.save_data('threat_jammer',data)


