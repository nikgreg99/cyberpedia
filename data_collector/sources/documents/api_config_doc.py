from data_collector.models import APIConfig
from django_elasticsearch_dsl import (Document, fields, Index)

api_config_index = Index('api_config')


@api_config_index.doc_type
class APIConfigDocument(Document):
    name = fields.TextField(
        attr = "name"
     )
    type = fields.TextField(attr= "type")
    value = fields.TextField(attr="value")
    required = fields.BooleanField(attr="required")
    creation_date = fields.Date(attr = "creation_date")
    update_date = fields.Date( attr = "update_date")

    class Meta:
        model = APIConfig
        fields = [
            'name',
            'type',
            'required',
            'creation_date',
            'update_date'
        ]

