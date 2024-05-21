from app.backend import mongodb_connector

class ConfiguracaoService:

    def __init__(self):
        self.db = mongodb_connector.MongoConnector()

    def obter_configuracao_extracao(self, tipo_operacao, sub_tipo = None):

        configuracao = self.obter_configuracao(tipo_operacao, sub_tipo)
        configuracao["pandas"] = {"delimiter": configuracao["delimitador"], "encoding":"UTF-8"}
        configuracao["renomear_colunas"] = {}
        tipo_operacao = str(tipo_operacao).lower()

        if tipo_operacao == "comercio":
            nomes_coluna = ["chave", "produto"] + [str(x) for x in range(1970, 2024)]
            colunas_usadas = range(1, len(nomes_coluna) + 1)
            configuracao["pandas"]['header'] = None
            configuracao["pandas"]['usecols'] = colunas_usadas
            configuracao["pandas"]['names'] = nomes_coluna
            configuracao["pandas"]['dtype'] = {"chave":"string"}
        elif tipo_operacao == "producao" or tipo_operacao == "processamento":
            configuracao["renomear_colunas"]["control"] = "chave"
            configuracao["renomear_colunas"]["cultivar"] = "produto"
        elif tipo_operacao == "importacao" or tipo_operacao == "exportacao":
            configuracao["renomear_colunas"]["País"] = "pais"
            for x in range(1970,2024):
                ano = str(x)
                configuracao["renomear_colunas"][ano] = ano + "_quantidade"
                configuracao["renomear_colunas"][ano + ".1"] = ano + "_valor"

        return configuracao

    def listar_configuracoes(self):
        configuracoes = self.db.listar("configuracao")

        return configuracoes
    
    def obter_configuracao(self, tipo_operacao, sub_tipo = None):
        config_obj = {}
        config_obj["tipo_operacao"] = tipo_operacao
        if sub_tipo != None:
            config_obj["sub_tipos.sub_tipo_operacao"] = sub_tipo

        configuracao = self.db.buscar("configuracao", config_obj)

        return configuracao