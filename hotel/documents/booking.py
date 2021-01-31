from elasticsearch_dsl import Document, Date, Integer, Text, InnerDoc, Object
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['elastic:elastic@127.0.0.1'])


class BookingDocument(Document):
    visitor_id = Integer()
    visitor_name = Text()
    settle_date = Date()
    leave_date = Date()
    room = Integer()

    class Index:
        name = 'booking'
        settings = {
          "number_of_shards": 1,
        }

    def save(self, ** kwargs):
        return super(BookingDocument, self).save(** kwargs)    