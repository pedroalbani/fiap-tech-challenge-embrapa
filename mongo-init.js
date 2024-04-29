db = db.getSiblingDB('admin');
if (db.getUser('embrapa') === null) {
  db.createUser({
    user: 'embrapa',
    pwd: 'embrapaPwd',
    roles: [{ role: 'readWrite', db: 'fiap_embrapa' }]
  });
}

db = db.getSiblingDB('fiap_embrapa');
if (!db.getCollectionNames().includes('csv_data')) {
  db.createCollection('csv_data');
  
}

// Adicionar registros com nome e delimitador
var records = [
  { name: 'ExpEspumantes', delimiter: ';' , url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ExpEspumantes.csv'},
  { name: 'ExpSuco', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ExpSuco.csv'},
  { name: 'ExpUva', delimiter: ';' , url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ExpUva.csv'},
  { name: 'ExpVinho', delimiter: ';' , url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ExpVinho.csv'},
  { name: 'ImpEspumantes', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ImpEspumantes.csv'},
  { name: 'ImpFrescas', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ImpFrescas.csv' },
  { name: 'ImpPassas', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ImpPassas.csv'},
  { name: 'ImpSuco', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ImpSuco.csv'},
  { name: 'ImpVinhos', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ImpVinhos.csv'},
  { name: 'ProcessaAmericanas', delimiter: '\t', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ProcessaAmericanas.csv'},
  { name: 'ProcessaMesa', delimiter: '\t', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ProcessaMesa.csv'},
  { name: 'ProcessaSemclass', delimiter: '\t', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ProcessaSemclass.csv'},
  { name: 'ProcessaViniferas', delimiter: '\t', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/ProcessaViniferas.csv'},
  { name: 'Producao', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/Producao.csv'},
  { name: 'Comercio', delimiter: ';', url: 'https://raw.githubusercontent.com/pedroalbani/fiap-tech-challenge-embrapa/main/dados_vitibrasil/Comercio.csv'}
];

db.csv_data.insertMany(records);