import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
    def __init__(self):
        self.host = os.getenv('MONGO_HOST')
        self.port = os.getenv('MONGO_PORT')
        self.username = os.getenv('MONGO_USERNAME')
        self.password = os.getenv('MONGO_PASSWORD')
        self.database = os.getenv('MONGO_DATABASE')

    def get_database_url(self):
        return f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/"

    def get_database_name(self):
        return self.database

class AppConfiguration:
    def __init__(self):
        self.url_arquivo = os.getenv('BASEURL_ARQUIVO_IMPORTACAO')
        self.url_fallback = os.getenv('BASEURL_ARQUIVO_FALLBACK')