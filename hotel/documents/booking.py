from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])

class Booking(Document):
    booked_by = Integer()
    room = Integer()
    settle_date = Date()
    leave_date = Date()

    class Index:
        name = 'booking'
        settings = {
          "number_of_shards": 1,
        }