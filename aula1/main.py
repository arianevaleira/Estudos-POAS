#Cria uma variavel, ou dicionario para guardar dados 
# Biblioteca pudantic e flast api
# Uvicorn (Servidor ASI)
#Precisa da virtual env
#pip install fastapi uvicorn pydantic 
#pip freeze > requeriments.txt
#O pydantic com o fast api e o post é feito com uma estrutura  em json, as api convertem ele em um objeto 
#uvicorn main:app ele não recarrega automaticamente
#http://127.0.0.1:8000/docs 

from fastapi import FastAPI, HTTPException
from models import Tarefa
from typing import List

app = FastAPI()

tarefas:List[Tarefa]=[] #Vai ser uma lista tipada, ou seja : -> Significa o tipo da variavel ou seja essa variavel so aceita o tipo tarefa

@app.get("/tarefas/", response_model=List[Tarefa]) #ele vai retorna uma lista de tarefas
def listar_tarefas():
    return tarefas #Retorna a variavel tarefas

@app.get("/tarefas/ {id}", response_model=Tarefa)
def listar_tarefas(id:int):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
    return HTTPException(status_code=404, detail="Não encrontrado")

@app.post("/tarefas/", response_model=Tarefa) #Cadastra tarefa
def criar_tarefa(tarefa:Tarefa):#tem que ser compativel com um que voce passa
    tarefas.append(tarefa)
    return tarefa


