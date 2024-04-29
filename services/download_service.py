import os
import requests
import pandas as pd
from pymongo import MongoClient
from io import StringIO
import logging

class DownloadService:
    def __init__(self, db):
        self.db = db
        self.csv_file_info = self.fetch_csv_info()
      
    def fetch_csv_info(self):
        csv_info = {}
        for doc in self.db.csv_data.find():
            csv_info[doc['name']] = doc
        return csv_info  
    
    def download_and_save(self):
        results = {}
        for csvFileName, doc in self.csv_file_info.items():
            df = pd.DataFrame()
            collection_name = csvFileName # O nome da coleção é o mesmo do arquivo 
            logging.info(f"Baixando {csvFileName} e salvando em {collection_name}")
            self.db[collection_name].delete_many({})
            url = doc['url']
            try:
                response = requests.get(url)
                response.raise_for_status()
                df = pd.read_csv(StringIO(response.text), delimiter=doc['delimiter'], encoding='utf-8')
                
                if not df.empty:
                    self.db[collection_name].insert_many(df.to_dict('records'))                    
                    results[csvFileName] =  self.make_response(url, df, True, 'Dados inseridos com sucesso.')
                else:
                    logging.warning(f"Nenhum dado para inserir em {collection_name}")
                    results[csvFileName] = self.make_response(url, df, True, "Sem dados para inserir.")

            except requests.exceptions.HTTPError as e:
                logging.error(f"Erro HTTP ao baixar {csvFileName}: {e}")
                results[csvFileName] = self.make_response(url, df, False, str(e))
            except pd.errors.ParserError as e:
                logging.error(f"Erro ao analisar {csvFileName}: {e}")
                results[csvFileName] = self.make_response(url, df, False, str(e))
            except Exception as e:
                logging.error(f"Erro inesperado com {csvFileName}: {e}")
                results[csvFileName] = self.make_response(url, df, False, str(e))
        return results

    def make_response(self, url, df, success, message):
        csvResponseDetails = {
                        "count": len(df),
                        "url": url,
                        "success": success,
                        "msg": message
                    }
            
        return csvResponseDetails

def get_download_service():
    mongo_uri = "mongodb://embrapa:embrapaPwd@localhost:27017/"
    db_name = "fiap_embrapa" 
    client = MongoClient(mongo_uri)
    db = client[db_name]
    db.teste.insert_one({"teste": "teste"})
    db.teste.delete_one({"teste": "teste"})
    return DownloadService(db)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    service = get_download_service()
    results = service.download_and_save()
    print(results)