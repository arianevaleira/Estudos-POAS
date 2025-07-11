# API de Alunos com FastAPI e SQLModel

Este projeto utiliza **FastAPI**, **SQLModel** e **Uvicorn** para criar uma API simples de gerenciamento de alunos com persistência em banco de dados SQLite.

OBS: Para abrir esse resumo no VS Code basta apertar `Ctrl` + `Shift` + `V`

---

## Como executar 

1. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

2. **Instale as dependências**:
   ```bash
   pip install fastapi uvicorn sqlmodel
   ```

3. **(Opcional) Gere o arquivo de requisitos**:
   ```bash
   pip freeze > requeriments.txt
   ```

4. **Execute o servidor**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação interativa da API**:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e assíncrono para criação de APIs.
- **Uvicorn**: Servidor ASGI leve e rápido.
- **SQLModel**: ORM baseado em SQLAlchemy + Pydantic.
- **SQLite**: Banco de dados local leve e fácil de configurar.

---

## Conceitos Importantes

- O modelo `Aluno` usa `SQLModel` para mapear uma tabela do banco de dados.
- A função `lifespan` inicializa o banco quando a API é iniciada.
- A dependência `Session` permite interações com o banco de forma segura.
- A rota `GET /alunos` retorna todos os registros da tabela `aluno`.

---

## Estrutura do Projeto

```
api-alunos/
│
├── main.py            # Arquivo principal da aplicação com rotas e configuração do app
├── models.py          # Modelos de dados baseados em SQLModel
├── banco.db           # Banco de dados SQLite gerado automaticamente
├── requeriments.txt   # Lista de dependências
└── resumo.md          # Documentação do projeto
```

---

## Exemplo de Código

### `models.py`

```python
from sqlmodel import SQLModel, Field

class Aluno(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str = Field(index=False)
    matricula: str = Field(index=False)
```

---

### `main.py`

```python
from typing import List, Annotated
from sqlmodel import SQLModel, Session, create_engine, select
from fastapi import FastAPI, Depends
from models import Aluno
from contextlib import asynccontextmanager

url = "sqlite:///banco.db"
args = {"check_same_thread": False}
engine = create_engine(url, connect_args=args)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def get_create_db():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_create_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/alunos")
def alunos(session: SessionDep) -> List[Aluno]:
    alunos = session.exec(select(Aluno)).all()
    return alunos
```

---

### `requeriments.txt`

```
fastapi
uvicorn
sqlmodel
```
