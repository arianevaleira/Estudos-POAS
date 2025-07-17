from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select
from typing import List
from models import Pedido

app = FastAPI()

# Conexão com SQLite
url = "sqlite:///banco.db"
engine = create_engine(url, echo=True)

# Criação da sessão
def get_session():
    with Session(engine) as session:
        yield session

# Criação da tabela ao iniciar
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Endpoint com paginação
@app.get("/pedidos", response_model=List[Pedido])
def listar_pedidos(
    limit: int = 100,
    offset: int = 0,
    session: Session = Depends(get_session)
):
    query = select(Pedido).offset(offset).limit(limit)
    pedidos = session.exec(query).all()
    return pedidos
