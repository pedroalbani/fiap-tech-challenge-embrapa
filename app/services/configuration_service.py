from pymongo import MongoClient
from app.config import base_settings

class ConfigurationService:
    def __init__(self):
        settings = base_settings.DatabaseConfig()
        self.db = MongoClient(settings.getDatabaseURI())[settings.getDatabaseName()]

    def getConfiguration(self,tipoOperacao):
        configuracao = self.db["configuracao"].find_one({"tipoOperacao": tipoOperacao})
        configuracao.pandas = {"delimiter": configuracao["delimitador"],"encoding":"UTF-8"}
        configuracao.renomear_colunas = {}
        match str(tipoOperacao).lower():
            case "comercio":
                nomesColuna = ["chave", "produto"] + [str(x) for x in range(1970, 2023)]
                colunasUsadas = range(1, len(nomesColuna) + 1)
                configuracao.pandas['header'] = None
                configuracao.pandas['usecols'] = colunasUsadas
                configuracao.pandas['names'] = nomesColuna
            case "producao":
                configuracao.renomear_colunas["control"] = "chave"
                configuracao.renomear_colunas["cultivar"] = "produto"
            case "importacao"|"exportacao":
                configuracao.renomear_colunas["País"] = "pais"

        return configuracao
