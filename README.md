# Projeto da Nexus Library

Este é um projeto exemplo para um sistema de biblioteca utilizando FastAPI e SQLAlchemy.

## Pre-requisitos

[Python](https://www.python.org/downloads/) -
[HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5) -
[CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) -
[SQlite](https://www.sqlite.org/index.html) -
[FastAPI](https://fastapi.tiangolo.com/)

### Bibliotecas necessárias
Para instalar as dependências, use o seguinte comando depois de fazer o clone desse repositorio para sua máquina

```bash
pip install -r requirements.txt
```

## Como executar o meu projeto

1. Clone o repositório:

 ```bash
git clone git@github.com:xXZonaryXx/ProjetoFinalProgWeb-facul.git
```

2.  Entre na pasta correta (app):
```bash
cd app
```

**Acesso ao app:**

O servidor FastAPI será iniciado e a aplicação sera aberta no seu navegador.

## Configuração passo a passo
- pip install -r requirements.txt

- python -m venv venv

- venv\Scripts\activate

- cd app

- uvicorn main:app --reload

## Funcionalidades

- Registro de novos usuários;
- Login de usuários;
- Adição de livros por usuários autenticados;
- Adição de autores por usuários autenticados;
- Visualização de livros por usuário;
- Visualização de autores por usuário;
- Deletar livros;
- Deletar autores;
- Editar livros;
- Editar autores.

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

- **main.py**: Configuração do FastAPI, definição de rotas e inicialização do servidor, contendo todos os CRUDs e as necessecidades do servidor.
  
- **models/**: Definição dos modelos de dados utilizando SQLAlchemy.

- **Templates/**: Templates HTML usando Jinja2 para melhor renderização.

- **static/**: Arquivos estáticos como CSS e imagens.

- **requirements.txt**: Lista de dependências Python necessárias para o projeto.

- **README.md**: Documentação do projeto, incluindo instruções de uso e configuração.

## Tecnologias usadas

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
