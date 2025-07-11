from typing import List,Annotated
from sqlmodel import SQLModel,Session,create_engine,select
from fastapi import FastAPI,Depends
from models import Aluno
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

SessionDep = Annotated[Session, Depends(get_session)] #

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