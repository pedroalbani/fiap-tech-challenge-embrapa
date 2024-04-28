import os
import requests
import pandas as pd
from pymongo import MongoClient
from io import StringIO
import logging

class DownloadService:
    def __init__(self, db):
        self.db = db
        self.base_url = "http://vitibrasil.cnpuv.embrapa.br/download/"
        self.csv_file_info = {
            'ExpEspumantes': ';',
            'ExpSuco': ';',
            'ExpUva': ';',
            'ExpVinho': ';',
            'ImpEspumantes': ';',
            'ImpFrescas': ';',
            'ImpPassas': ';',
            'ImpSuco': ';',
            'ImpVinhos': ';',
            'ProcessaAmericanas': '\t',
            'ProcessaMesa': '\t',
            'ProcessaSemclass': '\t',
            'ProcessaViniferas': '\t',
            'Producao': ';',
            'Comercio': ';'
        }
        
    def download_and_save(self):
        results = {}
        for csvFileName, delimiter in self.csv_file_info.items():
            collection_name = csvFileName # O nome da coleção é o mesmo do arquivo 
            logging.info(f"Baixando {csvFileName} e salvando em {collection_name}")
            self.db[collection_name].delete_many({})

            url = f"{self.base_url}{csvFileName}.csv"
            try:
                response = requests.get(url)
                response.raise_for_status()
                df = pd.read_csv(StringIO(response.text), delimiter=delimiter, encoding='utf-8')

                if not df.empty:
                    for col in df.columns:
                        df[col] = df[col].map(lambda x: x.encode('utf-8') if isinstance(x, str) else x)

                    self.db[collection_name].insert_many(df.to_dict('records'))
                    results[csvFileName] = df.head().to_dict('records')
                else:
                    logging.warning(f"Nenhum dado para inserir em {collection_name}")
                    results[csvFileName] = "Nenhum dado disponível"

            except requests.exceptions.HTTPError as e:
                logging.error(f"Erro HTTP ao baixar {csvFileName}: {e}")
                results[csvFileName] = str(e)
            except pd.errors.ParserError as e:
                logging.error(f"Erro ao analisar {csvFileName}: {e}")
                results[csvFileName] = str(e)
            except Exception as e:
                logging.error(f"Erro inesperado com {csvFileName}: {e}")
                results[csvFileName] = str(e)
        return results


def get_download_service():
    mongo_uri = "mongodb://embrapa:embrapaPwd@localhost:27017/"
    db_name = "fiap_embrapa" 
    client = MongoClient(mongo_uri)
    db = client[db_name]
    return DownloadService(db)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    service = get_download_service()
    results = service.download_and_save()
    print(results)