## Definição de rotas da API

### Listar educandos

TODO:

- Incluir foto do educando

`GET /educandos`

RESPONSE:

```json
[
  {
    "id": 1,
    "nome_completo": "Maria da Silva",
    "trilha": "Programação",
    "unidade": "SC401"
  },
  {
    "id": 2,
    "nome_completo": "João da Silva",
    "trilha": "Design",
    "unidade": "Pedra Branca"
  },
]
```

### Listar inisignias

`GET /insignias`

RESPONSE:

```json
[
  {
    "id": 1,
    "nome": "Python",
    "trilha": "Programação",
    "niveis": [
      {
        "id": 1,
        "requisitos": [
          {
            "id": 1,
            "descricao": "Leitura de arquivo CSV (Há vários dados no https://www.kaggle.com/datasets)."
          },
          {
            "id": 2,
            "descricao": "Transformar e utilizar do arquivo tipos primitivos: int, string, lista, tuplas e dicionários."
          },
          {
            "id": 3,
            "descricao": "Estruturas condicionais e de repetição (if, else, for, while)"
          },
          {
            "id": 4,
            "descricao": "Criar métodos"
          },
          {
            "id": 5,
            "descricao": "Escrita de um arquivo CSV"
          }
        ]
      },
      {
        "id": 2,
        "requisitos": [
          {
            "id": 1,
            "descricao": "Conexão e manipulação do banco de dados."
          },
          {
            "id": 2,
            "descricao": "Manipulação de strings."
          },
          {
            "id": 3,
            "descricao": "Instalação de módulos externos com PiP."
          },
          {
            "id": 4,
            "descricao": "Aplicação de paradigma funcional com map, reduce, filter e funções lambda."
          }
        ]
      },
      {
        "id": 3,
        "requisitos": [
          {
            "id": 1,
            "descricao": "Criação de API web com Django e Flask."
          },
        ]
      }
    ]
  }
]
```

- insignias de um educando
- Listar níveis de insignias
- Listar os requisitos
- Registar conquista de insignias

### Registrar insignias Novas

`POST /insignias/criar`

PAYLOAD:

```json
{
  "nome": "Python",
  "trilha": "Programação",
  "niveis": [
    {
      "id": 1,
      "requisitos": [
        {
          "id": 1,
          "descricao": "Leitura de arquivo CSV (Há vários dados no https://www.kaggle.com/datasets)."
        },
        {
          "id": 2,
          "descricao": "Transformar e utilizar do arquivo tipos primitivos: int, string, lista, tuplas e dicionários."
        },
        {
          "id": 3,
          "descricao": "Estruturas condicionais e de repetição (if, else, for, while)"
        },
        {
          "id": 4,
          "descricao": "Criar métodos"
        },
        {
          "id": 5,
          "descricao": "Escrita de um arquivo CSV"
        }
      ]
    },
    {
      "id": 2,
      "requisitos": [
        {
          "id": 1,
          "descricao": "Conexão e manipulação do banco de dados."
        },
        {
          "id": 2,
          "descricao": "Manipulação de strings."
        },
        {
          "id": 3,
          "descricao": "Instalação de módulos externos com PiP."
        },
        {
          "id": 4,
          "descricao": "Aplicação de paradigma funcional com map, reduce, filter e funções lambda."
        }
      ]
    },
    {
      "id": 3,
      "requisitos": [
        {
          "id": 1,
          "descricao": "Criação de API web com Django e Flask."
        }
      ]
    }
  ]
}
```

RESPONSE: `HTTP 201` (Created)

```json
{
  "status": "success"
}
```

RESPONSE: `HTTP: 400` (Bad Request)

```json
{
  "status": "error",
  "message": "Erro na criação da insígnia",
  "detalhes": "Descrição técnica do erro"
}
```

- Registrar educando Novo

## Requisitos do projeto

- Python 3

## Setup do projeto

Setup de acordo com a documentação de [Quickstart do Flask](https://flask.palletsprojects.com/en/stable/installation/).

- Cria virtual envirnment com o comando `python3 -m venv .venv`
- Ativa o ambiente virtual com o comando `. .venv/bin/activate`
- Instala as dependências com o comando `pip install -r requirements.txt`
- Inicia o servidor com o comando `flask --app api/index run --debug`
