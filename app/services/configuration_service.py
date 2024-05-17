from pymongo import MongoClient
from app.config import base_settings

class ConfigurationService:
    def __init__(self):
        settings = base_settings.DatabaseConfig()
        self.db = MongoClient(settings.getDatabaseURI())[settings.getDatabaseName()]

    def getConfiguration(self,tipo_operacao):
        configuracao = self.db["configuracao"].find_one({"tipo_operacao": tipo_operacao})
        configuracao["pandas"] = {"delimiter": configuracao["delimitador"],"encoding":"UTF-8"}
        configuracao["renomear_colunas"] = {}
        tipo_operacao = str(tipo_operacao).lower()

        if tipo_operacao == "comercio":
            nomes_coluna = ["chave", "produto"] + [str(x) for x in range(1970, 2023)]
            colunas_usadas = range(1, len(nomes_coluna) + 1)
            configuracao["pandas"]['header'] = None
            configuracao["pandas"]['usecols'] = colunas_usadas
            configuracao["pandas"]['names'] = nomes_coluna
            configuracao["pandas"]['dtype'] = {"chave":"string"}
        elif tipo_operacao == "producao":
            configuracao["renomear_colunas"]["control"] = "chave"
            configuracao["renomear_colunas"]["cultivar"] = "produto"
        elif tipo_operacao == "importacao" or tipo_operacao == "exportacao":
            configuracao["renomear_colunas"]["País"] = "pais"

        return configuracao
