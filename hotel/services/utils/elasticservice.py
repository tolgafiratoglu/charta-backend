from elasticsearch import Elasticsearch

class ElasticService():

    @classmethod
    def isServiceUp(self):
        elastic_service = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
        if elastic_service.ping():
            return True
        return False    