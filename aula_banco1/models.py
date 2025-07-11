#pip fastapi uvicorn sqlmodel
from sqlmodel import SQLModel, Field
class Aluno(SQLModel, table=True):
    id:int = Field(primary_key=True) #descreve 
    nome:str = Field(index=False) #O index false, não gera uma chave, diminui o trabalho 
    matricula:str=Field(index=False) 

class Professor(SQLModel, table=True):
    id:int = Field(primary_key=True)
    nome:str = Field(index=False)
    matricula:str = Field(index=False)
