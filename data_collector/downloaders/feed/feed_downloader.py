from abc import abstractmethod
from ..downloader import Downloader

class FeedDownloader(Downloader):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def download_feed(self):
        raise NotImplementedError()

    