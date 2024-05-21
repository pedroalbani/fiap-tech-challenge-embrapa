from abc import ABC, abstractmethod
from app.models import comercio,manufatura
import pandas as pd

class Strategy(ABC):
    def transform(self, dataframe, operacao):
        pass

class ComercioStrategy(Strategy):
    def transform(self, dataframe: pd.DataFrame,operacao):
        lista_comercio = []
        colunas = dataframe.columns.tolist()
        colunas.remove("pais")
        colunas = set([x.split("_") for x in colunas])

        for linha in dataframe.iterrows():
            lista_comercio += [comercio.Comercio(linha[1]["pais"], x, int(linha[1][x+"_quantidade"]),float(linha[1][x+"_valor"]), operacao) for x in colunas]

        return lista_comercio
class ManufaturaStrategy(Strategy):
    def transform(self, dataframe: pd.DataFrame, operacao):
        lista_manufatura = []
        colunas = dataframe.columns.tolist()
        colunas.remove("produto")
        colunas.remove("chave")

        for linha in dataframe.iterrows():
            lista_manufatura += [manufatura.Manufatura(linha[1]["produto"], linha[1].get("chave",None), int(x),int(linha[1][x]),operacao) for x in colunas]

        return lista_manufatura

class DataTransformation():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def transform(self,dt,operacao) -> None:
        return self._strategy.transform(dt, operacao)