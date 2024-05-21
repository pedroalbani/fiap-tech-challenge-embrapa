from app.backend import mongodb_connector

class ManufaturaService:

    def __init__(self):
        self.db = mongodb_connector.MongoConnector()
    
    def listar_manufaturas(self):
        manufaturas = self.db.listar("manufatura")

        return manufaturas