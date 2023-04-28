from data_collector.models import DataFeed
from django_elasticsearch_dsl import (Document, fields, Index)

feed_index =  Index('feeds')

@feed_index.doc_type
class FeedDocument(Document):

    name = fields.TextField(attr= "name")
    creation_date = fields.Date(attr= "creation_date")
    update_date = fields.DateTimeField(attr="update_date")
    data = fields.TextField(attr= "data")

    class Meta:
        model = DataFeed
        fields = [
            "name",
            "creation_date",
            "update_date",
            "data"
        ]
    