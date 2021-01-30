from elasticsearch_dsl import Document, Date, Integer
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['elastic:elastic@127.0.0.1'])

class ReservationDocument(Document):
    reserved_by = Integer()
    room = Integer()
    settle_date = Date()
    leave_date = Date()

    class Index:
        name = 'reservation'
        settings = {
          "number_of_shards": 1,
        }

    def save(self, ** kwargs):
        return super(ReservationDocument, self).save(** kwargs)    