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

def on_startup():
    SQLModel.metadata.create_all(engine)

# Endpoint para retornar pedidos
@app.get("/pedidos", response_model=List[Pedido])
def listar_pedidos(session: Session = Depends(get_session)):
    pedidos = session.exec(select(Pedido)).all()
    return pedidos
