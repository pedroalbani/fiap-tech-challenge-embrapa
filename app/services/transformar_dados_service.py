from abc import ABC
from app.models import comercio,manufatura
import pandas as pd

class Strategy(ABC):
    def transformar(self, dataframe, operacao, subcat_operacao):
        pass

class ComercioStrategy(Strategy):
    def transformar(self, dataframe: pd.DataFrame,operacao,subcat_operacao):
        lista_comercio = []
        colunas = dataframe.columns.tolist()
        if "pais" in colunas:
            colunas.remove("pais")
        if "Id" in colunas:
            colunas.remove("Id")
        colunas = sorted(set([x.split("_")[0] for x in colunas]))

        for linha in dataframe.iterrows():
            try:
                dados_atuais= [comercio.Comercio(linha[1]["pais"], x, int(linha[1][x+"_quantidade"]),float(linha[1][x+"_valor"]), operacao,subcat_operacao) for x in colunas]
                lista_comercio +=[x.__dict__ for x in dados_atuais]
            except ValueError:
                pass

        return lista_comercio

class ManufaturaStrategy(Strategy):
    def transformar(self, dataframe: pd.DataFrame, operacao,subcat_operacao):
        lista_manufatura = []
        colunas = dataframe.columns.tolist()
        if "produto" in colunas:
            colunas.remove("produto")
        if "chave" in colunas:
            colunas.remove("chave")
        if "id" in colunas:
            colunas.remove("id")

        for linha in dataframe.iterrows():
            dados_atuais = [manufatura.Manufatura(linha[1]["produto"], linha[1].get("chave",None), int(x), int(linha[1][x]), operacao, subcat_operacao) for x in colunas if str(linha[1][x]).isdecimal()]
            lista_manufatura += [x.__dict__ for x in dados_atuais]

        return lista_manufatura

class TransformarDado():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def transformar(self,dt,operacao,subcat_operacao) -> None:
        return self._strategy.transformar(dt, operacao,subcat_operacao)