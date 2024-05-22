# fiap-tech-challenge-embrapa
Tech Challenge do grupo 53 - FIAP

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

Se tudo rodou corretamente e nenhum erro foi lançado, abra o seu navegador clicando [aqui](http://localhost:8000).

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
A aplicação poderá ser acessada clicando [aqui](http://localhost:8000)

### Comandos utéis

```sh
# mostrar logs do container
docker logs embrapa-container

# para o container
docker stop embrapa-container

# excluir o container
docker rm embrapa-container
```
