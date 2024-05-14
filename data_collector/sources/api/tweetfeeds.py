import json 
import logging
import os
import requests

from typing import Tuple
from django.conf import settings
from django.utils import timezone
from data_collector.classes import FeedCollector

logger = logging.getLogger(__name__)


class TweetFeeds(FeedCollector):
    """
    Wrapper class for https://tweetfeed.live api
    """

    BASE_URL = "https://api.tweetfeed.live/v1/month"
    tweet_feed = requests.Session()
    filter_tweets: str = ""
    time: str = ""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TweetFeeds, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.tweet_feeds.headers = {
            'Accept': "application/json",
        }
        self.tweet_feed.proxies = settings.PROXIES

    @classmethod
    def location(cls) -> Tuple[str, str]:
        db_name = f"tweetfeed-{str(timezone.now())}.json"
        url = cls.BASE_URL
        return f"{settings.MEDIA_ROOT}/{db_name}", url

    @classmethod
    def update(cls) -> bool:
        db_location, db_url = cls.location()
        logger.info(f"Updating TweetFeeds {db_url}  at db_url {db_location}")
        try:
            response = cls.tweet_feed.get(db_url)
            response.raise_for_status()
        except requests.RequestException as ex:
            logger.error(f"TweetFeed failed to update {db_url}: {ex}")
            return False
        with open(db_location, "w", encoding="utf-8") as f:
            try:
                json.dump(response.json(), f)
            except json.JSONDecodeError as ex:
                logger.error(f"TweetFeeds failed to update {db_url} : {ex}")
                return False
            logger.info(f"Tweetfeed updated at {db_url}")
        return True

    def build_url(self) -> str:
        if not self.filter_tweets:
            url = self.BASE_URL + "/" + self.time
        return url

    def collect(self) -> dict:
        db_location, _ = self.location()

        if not os.path.exists(db_location):
            raise Exception("")

        with open(db_location, "r", encoding="utf-8") as f:
            db = json.load(f)
            return db
