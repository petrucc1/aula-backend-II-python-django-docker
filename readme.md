# Projeto de Aula da USP: Backend com Python, Django e FastAPI

Este projeto é parte do material didático utilizado nas aulas de Backend II do curso de tecnologia da Universidade de São Paulo (USP). O objetivo principal é fornecer aos estudantes uma experiência prática com o desenvolvimento de aplicações backend utilizando Python, juntamente com dois frameworks populares: Django e FastAPI.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `aula/`: Contém os diretórios principais do projeto, divididos entre Django e FastAPI.
  - `django-produtos/`: Aplicação Django para gerenciamento de produtos.
    - `db.sqlite3`: Banco de dados SQLite para armazenamento de dados dos produtos.
    - `manage.py`: Script de linha de comando do Django para tarefas administrativas.
    - `produto/`: Diretório contendo os modelos, views e templates específicos da aplicação de produtos.
    - `requirements.txt`: Lista de dependências necessárias para a aplicação Django.
    - `setup/`: Configurações adicionais para a aplicação.
    - `venv/`: Ambiente virtual Python para isolamento das dependências.
  - `fastapi-produtos/`: Aplicação FastAPI para gerenciamento de produtos.
    - `app.py`: Arquivo principal da aplicação FastAPI, contendo a definição dos endpoints.
    - `models/`: Diretório contendo os modelos de dados utilizados pela aplicação FastAPI.
    - `requirements.txt`: Lista de dependências necessárias para a aplicação FastAPI.
    - `venv/`: Ambiente virtual Python para isolamento das dependências.
- `docker-compose.yaml`: Arquivo de configuração do Docker Compose para orquestrar contêineres necessários ao projeto.
- `Dockerfile`: Arquivo de configuração para criar uma imagem Docker personalizada para o projeto.
- `readme.md`: Este arquivo, contendo informações sobre o projeto e instruções de uso.
- `referencial/`: Contém estruturas de referência para as aplicações Django e FastAPI, similar à pasta `aula/`.

## Objetivo do Projeto

O projeto visa proporcionar aos alunos uma compreensão prática sobre:

- Desenvolvimento de aplicações web com Django e FastAPI.
- Utilização de bancos de dados com Django ORM e SQLite.
- Criação e gerenciamento de ambientes virtuais Python.
- Uso de Docker e Docker Compose para orquestração de contêineres.
- Práticas de desenvolvimento e organização de código em projetos reais.

## Como Usar

Para utilizar este projeto, siga as instruções de instalação do ambiente Python e do Visual Studio Code disponíveis no arquivo `readme.md`. Após configurar o ambiente, você pode executar as aplicações Django e FastAPI localmente ou dentro de contêineres Docker, conforme preferir.

Para mais detalhes sobre a execução e desenvolvimento das aplicações, consulte os arquivos `readme.md` específicos dentro dos diretórios `aula/django-produtos/` e `aula/fastapi-produtos/`.

---

Este projeto é parte do material didático da Universidade de São Paulo e destina-se exclusivamente a fins educacionais.