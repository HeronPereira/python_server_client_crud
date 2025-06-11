# python_server_client_crud
Um servidor não bloqueante e um cliente em Python que se comuniquem via API REST para realizar operações CRUD em um cadastro de clientes, com segurança básica e persistência em banco de dados.

## Considerações tomadas no projeto
 - Dados do cliente foram considerados: (nome, email, cpf)
 - O cpf foi utilizado como tag de busca do cliente
 
## Estrutura de desenvolvimento

A ordem de desenvolvimento do projeto foi no seguinte formato:
- realizar o CRUD no mongoDB
- realizar os endpoint do servidor para acessar o CRUD do mongoDB via FastAPI e rodar o servidor via Uvicorn
- realizar login por endpoint da FastAPI, autorização e validação JWT
- realizar um cliente que realize o CRUD consumindo endpoints do FastAPI.
- Desenvolver uma imagem Docker para o servidor e para o cliente.

### Principais Bibliotecas Utilizadas
- Motor
- Beanie
- FastAPI
- Uvicorn
- jose
- pydantic
- passlib
- httpx

## Rodar o Projeto

Baixar o projeto do github:

```bash
git clone https://github.com/HeronPereira/python_server_client_crud.git
```

Na pasta do projeto:
```bash
pip install requirements.txt
```

### Caminho 1
Acessar a pasta server e rodar:
```bash
cd server
uvicorn server:app
```

Você poderá acessar o Swagger do FastAPI do servidor via:
http://127.0.0.1:8000/docs


Em outro terminal na pasta cliente:
```bash
cd client
python cliente.py
```

### Caminho 2

Em um terminal realize o comando:
```bash
cd server
docker compose build server
docker compose up
```
Você poderá acessar o Swagger do FastAPI do servidor via:
http://127.0.0.1:8000/docs

Em um outro terminal realize o comando:
```bash
cd client
docker compose build client
docker compose up
```


Isso irá rodar um conjunto de requisições básicas do cliente validando todo o CRUD da aplicação.
## Descritivo do Projeto: Desafio Python: Cliente-Servidor CRUD 

## Objetivo
Implementar um servidor não bloqueante e um cliente em Python que se comuniquem via API REST para realizar operações CRUD em um cadastro de clientes, com segurança básica e persistência em banco de dados.

## Requisitos do Servidor:
Fornecer endpoints não bloqueantes para:

Criar cliente
Ler cliente
Atualizar cliente
Deletar cliente
Implementar segurança
Persistir dados em banco de dados de sua preferência (desejável MongoDB)
Validar dados de entrada
Fornecer a documentação da API

## Requisitos do Cliente:
Consumir todos os endpoints do servidor
Processar respostas (sucesso/erro) adequadamente

## Diferenciais (opcionais):
Testes automatizados
Dockerização da solução

O desafiante deve elaborar a arquitetura detalhada, escolher as bibliotecas específicas e implementar a solução completa.

