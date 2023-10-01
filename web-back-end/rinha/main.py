from fastapi import FastAPI, Request
from pessoa_controlador import router, prefix
from modelos import *
from database_utils import criar_tabelas
from pessoa_repositorio import PessoaRepository

app = FastAPI()
criar_tabelas()


@app.get('/ping')
def ping():
    return 'Pong'


@app.get('/contagem-pessoas', response_model=int)
def contagem_pessoas():
    return PessoaRepository().contagem_pessoas()


# registrar roteadores
app.include_router(router, prefix=prefix)