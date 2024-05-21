from app.backend import mongodb_connector

class ComercioService:

    def __init__(self):
        self.db = mongodb_connector.MongoConnector()
    
    def listar_comercios(self):
        comercios = self.db.listar("comercio")

        return comercios