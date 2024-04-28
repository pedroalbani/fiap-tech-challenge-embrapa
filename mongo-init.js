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
  { name: 'ExpEspumantes', delimiter: ';' },
  { name: 'ExpSuco', delimiter: ';' },
  { name: 'ExpUva', delimiter: ';' },
  { name: 'ExpVinho', delimiter: ';' },
  { name: 'ImpEspumantes', delimiter: ';' },
  { name: 'ImpFrescas', delimiter: ';' },
  { name: 'ImpPassas', delimiter: ';' },
  { name: 'ImpSuco', delimiter: ';' },
  { name: 'ImpVinhos', delimiter: ';' },
  { name: 'ProcessaAmericanas', delimiter: '\t' },
  { name: 'ProcessaMesa', delimiter: '\t' },
  { name: 'ProcessaSemclass', delimiter: '\t' },
  { name: 'ProcessaViniferas', delimiter: '\t' },
  { name: 'Producao', delimiter: ';' },
  { name: 'Comercio', delimiter: ';' }
];

db.csv_data.insertMany(records);