
# Decisões Arquiteturais

### Framework de Desenvolvimento

Decisão: Será utilizado FastAPI (Python) para o desenvolvimento da API de Vitivinicultura.
Justificativa: FastAPI é conhecido por sua alta performance e facilidade de uso, permitindo o desenvolvimento rápido e eficiente de APIs RESTful.

### Containerização

Decisão: A solução será containerizada utilizando Docker.
Justificativa: Docker facilita a portabilidade e a escalabilidade da aplicação, permitindo que ela seja executada de maneira consistente em diferentes ambientes.

### Banco de Dados

Decisão: Utilizar MongoDB para armazenar os dados coletados e processados.
Justificativa: MongoDB é um banco de dados NoSQL escalável e flexível, adequado para armazenar grandes volumes de dados sem esquema fixo, ideal para os dados variados da vitivinicultura.

### Fallback para Coleta de Dados

Decisão: Implementar uma URL de fallback para coleta de dados caso o site da Embrapa esteja fora do ar.
Justificativa: Garante a continuidade da coleta de dados, aumentando a robustez e a resiliência do sistema.

### Autenticação

Decisão: Utilizar JWT para autenticação.
Justificativa: Proporciona um método seguro e escalável para gerenciar o acesso à API, protegendo os dados sensíveis.

### Documentação

Decisão: Usar Swagger para documentar a API.
Justificativa: Swagger proporciona uma maneira clara e interativa de visualizar e testar os endpoints da API, facilitando o trabalho dos desenvolvedores e a integração com outros sistemas.

### Deploy

Decisão: A solução será publicada em serviços de cloud da Amazon utilizando containers Docker.
Justificativa: (FIAP LIBEROU) As plataformas de cloud oferecem escalabilidade, confiabilidade e ferramentas integradas para gerenciamento e monitoramento da aplicação.

### Bibliotecas Utilizadas
- FastAPI: Framework web para construir APIs.
- uvicorn: Servidor ASGI para rodar a aplicação FastAPI.
- pymongo: Driver para conectar ao MongoDB.
- requests: Biblioteca para fazer requisições HTTP.
- pandas: Biblioteca para manipulação e análise de dados.
- detect-delimiter: Biblioteca para detectar delimitadores em arquivos CSV.
- python-dotenv: Carregar variáveis de ambiente de um arquivo .env.
