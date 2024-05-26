from app.backend import mongodb_connector,query_builder

class ManufaturaService:

    def __init__(self):
        self.db = mongodb_connector.MongoConnector()
        self.query_builder = query_builder.QueryBuilder()
    def listar_manufaturas(self,filtro):
        manufaturas = self.db.listar("manufatura",filtro)

        return manufaturas