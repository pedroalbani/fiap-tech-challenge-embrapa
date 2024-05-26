# fiap-tech-challenge-embrapa
Tech Challenge do grupo 53 - FIAP

## Objetivos e Arquitetura

[Acesse o documento sobre o Objetivo](Arquitetura/Objetivo.md)

[Acesse o documento sobre decisoões de Arquitetura](Arquitetura/Arquitetura.md)

## Instalação

Um passo a passo que informa o que você deve executar para ter um ambiente de desenvolvimento em execução localmente:

1. Clone o repositório
```sh
git clone https://github.com/pedroalbani/fiap-tech-challenge-embrapa

cd fiap-tech-challenge-embrapa
```

2. Configure seu arquivo de ambiente `env`

```sh
cp .env.example .env
```

- **MONGO_HOST** (opcional): endereço onde o serviço do mongo estará rodando, se não informado, `localhost` será usado.
- **MONGO_PORT** (opcional): porta onde o mongodb estará respondendo, se não informado, `27017` será usado.
- **MONGO_USERNAME**: informe qual nome de usuário utilizar ao conectar com o mongo. Exemplo: `embrapa`.
- **MONGO_PASSWORD**: informe qual nome de usuário utilizar ao conectar com o mongo. Exemplo: `embrapaPwd`.
- **MONGO_DATABASE**: informe o nome do banco onde os dados serão armazenados. Exemplo: `fiap_embrapa`.
- **MONGO_TIMEOUT_MS** (opcional): qual o tempo em milissegundos a aplicação deverá esperar por uma resposta do mongo. Se não informado, o padrão será de `15000ms`.
- **BASEURL_ARQUIVO_IMPORTACAO**: Qual endereço a aplicação irá olhar para baixar os arquivos a serem importados da Embrapa.
- **BASEURL_ARQUIVO_FALLBACK**: Qual endereço a aplicação irá olhar caso o serviço da Embrapa esteja fora e, portanto, não seja capaz de baixá-los.

> [!NOTE]
> Caso esteja usando o `docker-compose` para provisionamento do ambiente, saiba que as configurações usadas no `.env` serão também utilizadas para criação do container e do usuário do mongo. Sendo assim, para provisionar todo o ambiente, será necessário somente ajustar esse arquivo, nada mais.

3. Instale as bibliotecas necessárias

```sh
pip install -r requirements.txt
```

4. Inicie o MongoDB

```sh
docker-compose up -d
```

5. Rode o servidor web

```sh
uvicorn app.main:app --reload
```

Se tudo rodou corretamente e nenhum erro foi lançado, abra o seu navegador clicando [aqui](http://localhost:8000/docs).

## Testes

Para rodar os testes localmente, execute o comando abaixo no seu terminal.

```sh
python -m unittest discover -s tests
```

## Rodando a aplicação no Docker

```sh
# construir a imagem Docker
docker build -t embrapa-api .

# rodar a imagem recem criada
docker run -d -p 8000:8000 --name embrapa-container embrapa-api

# verificar se o container está rodando
docker ps
```

### Acesse a aplicação
A aplicação poderá ser acessada clicando [aqui](http://localhost:8000/docs)

### Comandos utéis

```sh
# mostrar logs do container
docker logs embrapa-container

# para o container
docker stop embrapa-container

# excluir o container
docker rm embrapa-container
```
