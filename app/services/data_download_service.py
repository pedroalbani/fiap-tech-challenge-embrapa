from app.services import configuration_service, data_transformation_service
from app.config.base_settings import AppConfiguration
from app.backend.mongodb_connector import MongoConnector
import pandas as pd
from pymongo import MongoClient
from urllib import error


class DataDownloadService:
    def __init__(self):
        self.settings = configuration_service.ConfigurationService()
        self.app_setting = AppConfiguration()
        self.db = MongoConnector()

    def importar(self,tipo_operacao, sub_categoria= None, atualizar_base = True):
        sucesso = True
        try:
            tipo_objeto, dados =self.downloadData(tipo_operacao,sub_categoria)
            mensagem = "Dados importados com sucesso!"
            if atualizar_base:
                self.atualizar_base(dados, tipo_objeto,tipo_operacao,sub_categoria)
                mensagem= " Obs: a base de dados foi atualizada."
        except Exception as ex:
            mensagem = "Não foi possível concluir a requisição. Mensagem técnica: " + str(ex)
        finally:
            return self.criar_response(dados,sucesso,mensagem)

    def downloadData(self, tipo_operacao, sub_categoria):
        configuracao = self.settings.getConfiguration(tipo_operacao, sub_categoria)
        if 'sub_tipos' not in configuracao.keys():
            sub_categorias_lst = [{"label_arquivo":"","categoria":""}]
        elif sub_categoria != None:
            sub_categorias_lst = [{"label_arquivo":x["label_arquivo"],"categoria":x["sub_tipo_operacao"]} for x in configuracao["sub_tipos"] if x["sub_tipo_operacao"] == sub_categoria]
        else:
            sub_categorias_lst = [{"label_arquivo":x["label_arquivo"],"categoria":x["sub_tipo_operacao"]}  for x in configuracao["sub_tipos"]]

        modelos = []

        for subcat_atual in sub_categorias_lst:

            nomeArquivo = configuracao["label_arquivo"] + subcat_atual["label_arquivo"] + ".csv"
            try:
                dados = pd.read_csv(self.app_setting.url_arquivo + nomeArquivo, **configuracao["pandas"])
            except error.HTTPError:
                dados = pd.read_csv(self.app_setting.url_fallback + nomeArquivo, **configuracao["pandas"])

            if len(configuracao["renomear_colunas"].keys()) > 0:
                dados = dados.rename(columns=configuracao["renomear_colunas"])

            if str(configuracao["tipo_objeto"]).lower() == "comercio":
                transformador = data_transformation_service.DataTransformation(
                    data_transformation_service.ComercioStrategy())
            else:
                transformador = data_transformation_service.DataTransformation(
                    data_transformation_service.ManufaturaStrategy())

            modelos+=transformador.transform(dados, tipo_operacao,subcat_atual["categoria"])

        return configuracao["tipo_objeto"],modelos

    def atualizar_base(self,dados,tipo_objeto,tipo_operacao,sub_categoria):
        filtro_apagar = {}
        filtro_apagar["operacao"] = tipo_operacao
        if sub_categoria != None:
            filtro_apagar["sub_categoria_operacao"] = sub_categoria
        self.db.apagar(tipo_objeto,filtro_apagar)

        self.db.salvar(tipo_objeto,dados)

    def criar_response(self, dados, sucesso, mensagem):
        csvResponseDetails = {
            "tamanho": len(dados),
            "sucesso": sucesso,
            "mensagem": mensagem,
            "dados":dados
        }

        return csvResponseDetails
service = DataDownloadService()
service.importar("Importacao","Espumante",True)
