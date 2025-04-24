from pydantic import BaseModel

class Tarefa(BaseModel): #quando vier o json ele vai fazer as conversoes para esse valor 
    id:int #vai ser gerado manual 
    descricao:str
    prioridade:int
    concluida:bool #tipo boleano 

