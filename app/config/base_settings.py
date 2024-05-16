class DatabaseConfig:
    def __init__(self):
        self.mongo_uri = "mongodb://embrapa:embrapaPwd@localhost:27017/"
        self.db_name = "fiap_embrapa"

    def getDatabaseURI(self):
        return self.mongo_uri

    def getDatabaseName(self):
        return self.db_name
class AppConfiguration:
    def __init__(self):
        self.url_arquivo = 'http://vitibrasil.cnpuv.embrapa.br/download/'
        self.url_fallback = 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/'