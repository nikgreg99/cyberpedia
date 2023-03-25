import logging
from celery import app
from data_collector.sources.apps import sources
from data_collector.models import DataFeed

logger = logging.getLogger(__name__)

@app.task
def update_malpedia():
   print("Ok")


    
    



