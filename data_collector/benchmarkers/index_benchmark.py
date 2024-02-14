import logging
from datetime import datetime
from .benckmark import Benchmark
from ..models import DailyIndexMetadata,Index
from ..managers.elastic_manager import ElasticManager


logger = logging.getLogger(__name__)

class IndexStorageGrowthBenchmark(Benchmark):

    def __init__(self) -> None:
        name = "IndexStorageGrowthBenckmark"
        self.elasitc = ElasticManager().instance
        super().__init__(name)


    def monitor_benchmark(self):
        indexes = Index.objects.all()
        for index in indexes:
            index_name = index.name
            timestamp = datetime.now()
            index_metadata = self.elasitc.get_index_metadata_stats(index_name)
            statistic_data = DailyIndexMetadata.objects.create()
            statistic_data.index = index
            statistic_data.timestamp = timestamp
            statistic_data.index_size = index_metadata['index']['size_in_gigabytes']
            statistic_data.save()


    

