Requisições POST
Rota: http://127.0.0.1:5000/educando/conquista
Body:

{
    "insignia_id": "6744b7ee554712616074d3a4",
    "educando_id": "6747bc07dccce737fd3f82c8",
    "data_conquista": "2024-11-27",
    "nivel": 3
}
Rota: http://127.0.0.1:5000/educando/criar
Body:

{
    "nome": "Thiago Segundo",
    "trilha": "Design",
    "unidade": "Pedra Branca"
}
Rota: http://127.0.0.1:5000/insignias/criar
Body:

{
    "nome": "Design Gráfico",
    "trilha": "Design",
    "niveis": [
        {
            "id": 1,
            "requisitos": [
                {
                    "descricao": "Defina e apresente no mínimo 2 peças gráficas das suas produções.",
                    "id": 1
                },
                {
                    "descricao": "Apresente o painel de referências.",
                    "id": 2
                },
                {
                    "descricao": "Estudo e definição: paleta de cores; tipografia; elementos gráficos.",
                    "id": 3
                },
                {
                    "descricao": "Apresente a argumentação da utilização de todos os elementos gráficos.",
                    "id": 4
                }
            ]
        },
        {
            "id": 2,
            "requisitos": [
                {
                    "descricao": "Desenvolver 3 peças gráficas que apliquem no mínimo 3 princípios de Gestalt.",
                    "id": 1
                },
                {
                    "descricao": "Utilizar a identidade do nível 1 ou criar uma nova identidade que respeite os mesmos critérios.",
                    "id": 2
                },
                {
                    "descricao": "Referências que apresentem os princípios utilizados.",
                    "id": 3
                },
                {
                    "descricao": "Apresente e explique a utilização dos princípios.",
                    "id": 4
                }
            ]
        },
        {
            "id": 3,
            "requisitos": [
                {
                    "descricao": "Objetivo: Elaborar o redesign de uma peça gráfica já existente (poster de filme, capa de álbum, logo, embalagem).",
                    "id": 1
                },
                {
                    "descricao": "Utilize os fundamentos estudados nos níveis 1 e 2.",
                    "id": 2
                }
            ]
        }
    ]
}
Requisições GET
Rota: http://127.0.0.1:5000/insignias
Rota: http://127.0.0.1:5000/insignia/:id
Parâmetros:

id: 674494b966c8ae0456efbb0c
Rota: http://127.0.0.1:5000/insignia/:id/educandos
Parâmetros: id: 674494b966c8ae0456efbb0c

Rota: http://127.0.0.1:5000/insignias/conquistadas
Lista de Requisições PUT
Rota: http://127.0.0.1:5000/educando/:id/editar
Body:

{
    "nome": "Thiago Cerutti (mentor)"
}
Parâmetros:

id: 6747bc07dccce737fd3f82c8
Rota: http://127.0.0.1:5000/insignia/:id/atualizar
Body:

{
    "nome": "Arduino adulterado",
    "trilha": "programação IOT (iniciante)",
    "niveis": [
        {
            "id": 1,
            "requisitos": [
                {
                    "descricao": "@Compreender o básico de variáveis, funções e escopo.",
                    "id": 1
                },
                {
                    "descricao": "!Manipulação de elementos do DOM com JavaScript puro.",
                    "id": 2
                },
                {
                    "descricao": "#Utilizar eventos como click, submit e outros.",
                    "id": 3
                },
                {
                    "descricao": "Introdução ao uso de Promises e callbacks.",
                    "id": 4
                }
            ]
        },
        {
            "id": 2,
            "requisitos": [
                {
                    "descricao": "Compreender o básico de variáveis, funções e escopo.",
                    "id": 1
                },
                {
                    "descricao": "Manipulação de elementos do DOM com JavaScript puro.",
                    "id": 2
                },
                {
                    "descricao": "Utilizar eventos como click, submit e outros.",
                    "id": 3
                },
                {
                    "descricao": "Introdução ao uso de Promises e callbacks.",
                    "id": 4
                }
            ]
        },
        {
            "id": 3,
            "requisitos": [
                {
                    "descricao": "Compreender o básico de variáveis, funções e escopo.",
                    "id": 1
                },
                {
                    "descricao": "Manipulação de elementos do DOM com JavaScript puro.",
                    "id": 2
                },
                {
                    "descricao": "Utilizar eventos como click, submit e outros.",
                    "id": 3
                },
                {
                    "descricao": "Introdução ao uso de Promises e callbacks.",
                    "id": 4
                }
            ]
        }
    ]
}
Parâmetros:

id: 6747c8a0bf45d7fb4171a3bf
Lista de Requisições DELETE
Rota: http://127.0.0.1:5000/educando/:id/deletar
Parâmetros:

id: 6747c36bcfc9b7df623322a4
Rota: http://127.0.0.1:5000/insignia/:id/deletar
Parâmetros:

id: 6747c8a0bf45d7fb4171a3bf

## Requisitos do projeto

- Python 3

## Setup do projeto

Setup de acordo com a documentação de [Quickstart do Flask](https://flask.palletsprojects.com/en/stable/installation/).

- Cria virtual envirnment com o comando `python3 -m venv .venv`
- Ativa o ambiente virtual com o comando `. .venv/bin/activate`
- Instala as dependências com o comando `pip install -r requirements.txt`
- Inicia o servidor com o comando `flask --app api/index run --debug`
