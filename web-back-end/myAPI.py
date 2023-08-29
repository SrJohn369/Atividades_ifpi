from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#--------------------------------------------------

app = FastAPI()

#--------------------------------------------------
class Dispositivo(BaseModel):
    id_dispositivo: int | None
    id_ambiente: int | None
    descricao: str
    icone: str
    estado_conexao: str
    on_off: bool

class Ambiente(BaseModel):
    id_ambiente: int | None
    descricao: str
    icone: str
    itens: list 

#--------------------------------------------------
# Func auxiliar -----------------------------------
def separ_objct(objecto: list, ambiente: int):
    lista_intens = []
    for dispositivo in objecto:
        if dispositivo.id_ambiente == ambiente:
            lista_intens.append(dispositivo)
        else:
            pass
    return lista_intens


def get_one_ambiente(id: int):
    for ambiente in list_ambientes:
        if id == ambiente.id_ambiente:
            return ambiente
    return None


lista_dispo = [
    Dispositivo(id_dispositivo=1, id_ambiente=1, descricao="Tevelisão", icone="TV", estado_conexao="30ms", on_off=True), 
    Dispositivo(id_dispositivo=2, id_ambiente=1, descricao="Homethi", icone="som", estado_conexao="650ms", on_off=False),
    Dispositivo(id_dispositivo=1, id_ambiente=2, descricao="Geladeira", icone="Gelo", estado_conexao="50ms", on_off=True)
]
list_ambientes = [
    Ambiente(id_ambiente=1, descricao="Sala de estar", icone="Sala", itens=separ_objct(lista_dispo, 1)), 
    Ambiente(id_ambiente=2, descricao="Cozinha", icone="Sala", itens=separ_objct(lista_dispo, 2))
]


#--------------------------------------------------
# GET ---------------------------------------------
# GET todos os ambientes
@app.get('/ambientes', status_code=200)
async def ambiente():
    return list_ambientes

# GET lista de dispositivos
@app.get('/ambientes/{id}/dispositivo', status_code=200)
async def dispositivos(id_ambiente: int):
    ambiente = get_one_ambiente(id_ambiente)
    if ambiente == None:
        raise HTTPException(
            status_code=404,
            detail="ERROR 404,  ambiente NOT FOUND!"
        )
    else:
        return ambiente.itens


# GET-ONE -----------------------------------------
# GET um ambiente por id
@app.get('/ambiente/{id}', status_code=200)
async def ambiente_id(id: int):
    ambiente = get_one_ambiente(id)
    if ambiente == None:
        raise HTTPException(
            status_code=404,
            detail="ERROR 404, ambiente NOT FOUND!"
        )
    else:
        return ambiente


# POST --------------------------------------------
proximo_id = 2

# POST criar um ambiente 
@app.post('/ambientes/criar_ambi', status_code=201)
async def criar_ambiente(ambiente: Ambiente):
    global proximo_id
    proximo_id += 1
    ambiente.id_ambiente = proximo_id
    ambiente.itens = separ_objct(lista_dispo, proximo_id)
    list_ambientes.append(ambiente)
    return ambiente


# POST criar um dispositivo
@app.post("/ambientes/{id}/criar_disp", status_code=201)
async def criar_dispositivo(id: int,dispositivo: Dispositivo):
    ambiente = get_one_ambiente(id)
    qnt_dispo = len(ambiente.itens)
    id_dispositivo = qnt_dispo + 1
    dispositivo.id_dispositivo = id_dispositivo
    dispositivo.id_ambiente = ambiente.id_ambiente
    lista_dispo.append(dispositivo)
    print(lista_dispo)
    return dispositivo