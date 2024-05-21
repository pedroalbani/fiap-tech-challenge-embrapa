from app.services import configuration_service, data_transformation_service
from app.config.base_settings import AppConfiguration
import pandas as pd
from urllib import error


class DataDownloadService:
    def __init__(self):
        self.settings = configuration_service.ConfigurationService()
        self.app_setting = AppConfiguration()

    def downloadData(self, tipoOperacao, subCategoria= None):
        configuracao = self.settings.getConfiguration(tipoOperacao)
        if (subCategoria == None):
            subCategoria = ""
        nomeArquivo = tipoOperacao + subCategoria + ".csv"
        try:
            dados = pd.read_csv(self.app_setting.url_arquivo + nomeArquivo, **configuracao["pandas"])
        except error.HTTPError:
            dados = pd.read_csv(self.app_setting.url_fallback + nomeArquivo, **configuracao["pandas"])

        if len(configuracao["renomear_colunas"].keys()) > 0:
            dados.rename(configuracao["renomear_colunas"])

        if str(configuracao["tipo_objeto"]).lower() == "comercio":
            transformador = data_transformation_service.DataTransformation(
                data_transformation_service.ComercioStrategy())
        else:
            transformador = data_transformation_service.DataTransformation(
                data_transformation_service.ManufaturaStrategy())

        modelos = transformador.transform(dados, tipoOperacao)

        return modelos

download = DataDownloadService()
download.downloadData("Comercio")