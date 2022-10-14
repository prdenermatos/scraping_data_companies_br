from pydoc import doc
from unittest import result
from src.db.elasticsearch import connect_db


class ElasticsearchRepository:

    def __init__(self) -> None:
        self._elasticsearch = connect_db()

    def insert_document(self, index:str, id:str, document:dict) -> None:
        self._elasticsearch.create(index=index, id=id, document=document)

    def find_document_by_id(self, index:str, id:str) -> dict:
        return self._elasticsearch.get(index=index, id=id)["_source"]
    
    def find_all(self, index:str, filter:dict) -> list:
        result = []
        result_db = self._elasticsearch.search(index=index)
        for hit in result_db['hits']['hits']:
            doc = {"id": hit["_id"]} 
            doc.update(hit["_source"])
            result.append(doc)
        return result
    
    def delete(self, index:str, id:str) -> None:
        self._elasticsearch.delete(index=index, id=id)