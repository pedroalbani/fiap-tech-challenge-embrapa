from pymongo import MongoClient
from app.config import base_settings
class MongoConnector:
    def __init__(self):
        settings = base_settings.DatabaseConfig()
        self.db = MongoClient(settings.getDatabaseURI())[settings.getDatabaseName()]

    def salvar(self, collection, dados):
        return self.db[collection].insert_many(dados)
    def apagar(self,collection,filtro):
        return self.db[collection].delete_many(filtro)
    def buscar(self,collection, criterio_busca):
        return self.db[collection].find_one(criterio_busca)