# fiap-tech-challenge-embrapa
Tech Challenge do grupo 53 - FIAP

### Instalação

Um passo a passo que informa o que você deve executar para ter um ambiente de desenvolvimento em execução:

```bash
# Clonar o repositório
git clone https://github.com/pedroalbani/fiap-tech-challenge-embrapa
cd fiap-tech-challenge-embrapa

# Instalar as dependências (para execução local sem Docker)
pip install -r requirements.txt

# Executar a aplicação localmente
uvicorn app.main:app --reload

# Comando para executar testes
python -m unittest discover -s tests

# Instruções para execução com Docker
## Construir a imagem Docker
docker build -t embrapa-api .

## Rodar a aplicação em um container Docker
docker run -d -p 8000:8000 --name embrapa-container embrapa-api

## Verificar se o container está rodando
docker ps

## Acessar a aplicação
A aplicação pode ser acessada em `http://localhost:8000`

## Ver logs do container (opcional)
docker logs embrapa-container

## Parar e remover o container (quando necessário)
docker stop embrapa-container
docker rm embrapa-container
