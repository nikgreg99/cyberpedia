from elasticsearch_dsl import Document,Text,Date,Boolean


class APIConfigDocument(Document):
    name = Text()
    type = Text()
    value = Text()
    required = Boolean()
    creation_date = Date()
    update_date = Date()

    class Index:
        name = 'api_condfig_index'

class FeedDocument(Document):

    name = Text()
    creation_date = Text()
    update_date = Text()


    class Index:
        name = "feed_index"

