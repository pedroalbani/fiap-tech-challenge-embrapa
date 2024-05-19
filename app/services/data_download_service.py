from app.services import configuration_service, data_transformation_service
from app.config.base_settings import AppConfiguration
import pandas as pd
from urllib import error


class DataDownloadService:
    def __init__(self):
        self.settings = configuration_service.ConfigurationService()
        self.app_setting = AppConfiguration()

    def downloadData(self, tipo_operacao, sub_categoria= None):
        configuracao = self.settings.getConfiguration(tipo_operacao, sub_categoria)
        if 'sub_tipos' not in configuracao.keys():
            sub_categorias = [""]
        elif sub_categoria != None:
            sub_categorias = [x["label_arquivo"] for x in configuracao["sub_tipos"] if x["sub_tipo_operacao"] == sub_categoria]
        else:
            sub_categorias = [x["label_arquivo"] for x in configuracao["sub_tipos"]]

        modelos = []

        for subcat_atual in sub_categorias:

            nomeArquivo = configuracao["label_arquivo"] + subcat_atual + ".csv"
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

            modelos+=transformador.transform(dados, tipo_operacao)

        return modelos