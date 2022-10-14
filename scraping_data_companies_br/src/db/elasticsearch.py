from datetime import datetime
from elasticsearch7 import Elasticsearch


def connect_db() -> Elasticsearch: 
    return Elasticsearch("http://localhost:9200")
