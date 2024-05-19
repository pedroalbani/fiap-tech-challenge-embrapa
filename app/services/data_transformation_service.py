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
        if "pais" in colunas:
            colunas.remove("pais")
        if "Id" in colunas:
            colunas.remove("Id")
        colunas = sorted(set([x.split("_")[0] for x in colunas]))

        for linha in dataframe.iterrows():
            try:
                lista_comercio += [comercio.Comercio(linha[1]["pais"], x, int(linha[1][x+"_quantidade"]),float(linha[1][x+"_valor"]), operacao) for x in colunas]
            except ValueError:
                pass

        return lista_comercio
class ManufaturaStrategy(Strategy):
    def transform(self, dataframe: pd.DataFrame, operacao):
        lista_manufatura = []
        colunas = dataframe.columns.tolist()
        if "produto" in colunas:
            colunas.remove("produto")
        if "chave" in colunas:
            colunas.remove("chave")
        if "id" in colunas:
            colunas.remove("id")

        for linha in dataframe.iterrows():
            lista_manufatura += [manufatura.Manufatura(linha[1]["produto"], linha[1].get("chave",None), int(x),int(linha[1][x]),operacao) for x in colunas if str(linha[1][x]).isdecimal()]


        return lista_manufatura

class DataTransformation():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def transform(self,dt,operacao) -> None:
        return self._strategy.transform(dt, operacao)

