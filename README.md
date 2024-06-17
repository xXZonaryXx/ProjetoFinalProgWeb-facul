# Documentação do Projeto

Projeto *Biblioteca Nexus*.

## Descrição

Este projeto é uma aplicação web para gerenciar uma biblioteca de livros e autores. Ela fornece uma API RESTful para realizar operações como registrar novos usuários, fazer login, adicionar livros e autores, e visualizar livros e autores por usuário.

## Funcionalidades

- Registro de novos usuários
- Login de usuários
- Adição de livros por usuários autenticados
- Adição de autores por usuários autenticados
- Visualização de livros por usuário
- Visualização de autores por usuário
- Deletar livros
- Deletar autores
- Editar livros
- Editar autores

## Configuração

uvicorn app.main:app --reload

venv\Scripts\activate

python -m venv venv

fastapi
uvicorn
sqlalchemy 
jinja2

pip install -r requirements.txt

### Pré-requisitos

Antes de executar a aplicação,  e necessario ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python (versão X.X ou superior)
- pip (gerenciador de pacotes do Python)
- SQLite (ou outro banco de dados suportado pelo SQLAlchemy)

## Execução

uvicorn app.main:app --reload

## Licença

Este projeto está licenciado sob a MIT License.