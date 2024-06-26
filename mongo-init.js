db = db.getSiblingDB('admin');
if (db.getUser(process.env.MONGO_INITDB_ROOT_USERNAME) === null) {
  db.createUser({
    user: process.env.MONGO_INITDB_ROOT_USERNAME,
    pwd: process.env.MONGO_INITDB_ROOT_PASSWORD,
    roles: [{ role: 'readWrite', db: process.env.MONGO_INITDB_DATABASE }]
  });
}

db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);
if (!db.getCollectionNames().includes('configuracao')) {
  db.createCollection('configuracao');
}

if (!db.getCollectionNames().includes('comercio')) {
  db.createCollection('comercio');
}

if (!db.getCollectionNames().includes('manufatura')) {
  db.createCollection('manufatura');
}

// Adicionar registros com nome e delimitador
var records = [{
  "tipo_operacao": "Comercializacao",
  "label_arquivo": "Comercio",
  "delimitador": ";",
  "tipo_objeto": "manufatura"
},
{
  "tipo_operacao": "Exportacao",
  "label_arquivo": "Exp",
  "delimitador": ";",
  "tipo_objeto": "comercio",
  "sub_tipos": [
    {
      "sub_tipo_operacao": "Espumante",
      "label_arquivo": "Espumantes"
    },
    {
      "sub_tipo_operacao": "Suco",
      "label_arquivo": "Suco"
    },
    {
      "sub_tipo_operacao": "Uva",
      "label_arquivo": "Uva"
    },
    {
      "sub_tipo_operacao": "Vinho",
      "label_arquivo": "Vinho"
    }
  ]
},
{
  "tipo_operacao": "Processamento",
  "label_arquivo": "Processa",
  "delimitador": "\t",
  "tipo_objeto": "manufatura",
  "sub_tipos": [
    {
      "sub_tipo_operacao": "Americana",
      "label_arquivo": "Americanas"
    },
    {
      "sub_tipo_operacao": "Mesa",
      "label_arquivo": "Mesa"
    },
    {
      "sub_tipo_operacao": "SemClassificacao",
      "label_arquivo": "Semclass"
    },
    {
      "sub_tipo_operacao": "Vinifera",
      "label_arquivo": "Viniferas"
    }
  ]
},
{
  "tipo_operacao": "Producao",
  "label_arquivo": "Producao",
  "delimitador": ";",
  "tipo_objeto": "manufatura"
},
{
  "tipo_operacao": "Importacao",
  "label_arquivo": "Imp",
  "delimitador": ";",
  "tipo_objeto": "comercio",
  "sub_tipos": [
    {
      "sub_tipo_operacao": "Espumante",
      "label_arquivo": "Espumantes"
    },
    {
      "sub_tipo_operacao": "Suco",
      "label_arquivo": "Suco"
    },
    {
      "sub_tipo_operacao": "Fresca",
      "label_arquivo": "Frescas"
    },
    {
      "sub_tipo_operacao": "Passa",
      "label_arquivo": "Passas"
    }
  ]
}];

db.configuracao.insertMany(records);
