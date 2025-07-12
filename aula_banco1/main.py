from typing import List,Annotated
from sqlmodel import SQLModel,Session,create_engine,select
from fastapi import FastAPI,Depends
from models import Aluno
from models import Professor
from contextlib import asynccontextmanager

url = "sqlite:///banco.db"
# PostgreSQL - psycopg2-binary
urlpg = "postgresql://usuario:senha@localhost/banco"
#Mysql - pymysql
urlmysql = "mysql+pymysql://usuario:senha@localhost/banco"
args = {"check_same_thread": False}
engine = create_engine(url,connect_args=args) #Cria a conexão

def get_session(): #Onde eu abro o canal de comunicação, exemplo quando boto a matricula e senha 
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)] 

def get_create_db(): #Verifica se o banco existe 
    SQLModel.metadata.create_all(engine)
    
@asynccontextmanager
async def lifespan(app:FastAPI):
    get_create_db()
    yield #Ele para, a execução tud

app = FastAPI(lifespan=lifespan) #ela cria o banco depois que o fastapi sobe 
 
@app.get("/alunos")
def alunos(session:SessionDep) -> List[Aluno]: #Respose  model  -> List[Aluno]
    alunos = session.exec(select(Aluno)).all()
    return alunos


@app.post("/alunos")
def cadastrar(session:SessionDep, aluno:Aluno) -> Aluno:
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno


@app.delete("/alunos/{id}")
def deletar(session:SessionDep, id:int) -> str:
    consulta = select(Aluno).where(Aluno.id== id)
    aluno = session.exec(consulta).one()
    session.delete(aluno)
    session.commit()
    return "Aluno excluido com sucesso"

@app.put("/alunos/{id}")
def atualizar(session:SessionDep, id:int, nome:str) -> Aluno:
    consulta = select(Aluno).where(Aluno.id== id)
    aluno = session.exec(consulta).one()
    aluno.nome = nome   
    session.add(aluno)
    session.commit()
    return aluno


#Cadastrar professores 
@app.post("/professores")
def cadastrar(session:SessionDep, professor:Professor) -> Professor:
    session.add(professor)
    session.commit()
    session.refresh(professor)
    return professor


@app.get("/professores")
def listar(session:SessionDep) -> List[Professor]:
    professor = session.exec(select(Professor)).all()
    return professor


@app.delete("/professores/{id}")
def deletar(session:SessionDep, id:str) -> str:
    consulta = select(Professor).where(Professor.id== id)
    professor = session.exec(consulta).one()
    session.delete(professor)
    session.commit()
    return "Professor excluido com sucesso"

@app.put("/professores/{id}")
def atualizar(session:SessionDep, id:str, nome:str) -> Professor:
    consulta = select(Professor).where(Professor.id== id)
    professor = session.exec(consulta).one()
    professor.nome = nome   
    session.add(professor)
    session.commit()
    return professor