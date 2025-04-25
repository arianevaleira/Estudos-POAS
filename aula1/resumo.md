#  API de Tarefas com FastAPI

Este projeto utiliza **FastAPI**, **Pydantic** e **Uvicorn** para criar uma API simples de gerenciamento de tarefas.
OBS: Para abrir esse resumo no vscode basta apertar ```ctlr``` +```Shift``` + ```V```

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
   pip install fastapi uvicorn pydantic
   ```

3. **(Opcional) Gere o arquivo de requisitos**:
   ```bash
   pip freeze > requeriments.txt
   ```

4. **Execute o servidor**:
   ```bash
   uvicorn main:app 
   ```

5. **Acesse a documentação interativa da API**:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido.
- **Uvicorn**: Servidor ASGI leve e eficiente.
- **Pydantic**: Validação e serialização de dados via modelos.

---

## Conceitos Importantes

- Os dados enviados por POST são estruturados em JSON e convertidos automaticamente para objetos Python usando Pydantic.
- As rotas da API seguem o padrão REST, utilizando métodos HTTP (`GET`, `POST`).
- Tipagem com `List[Tarefa]` ajuda a garantir a integridade dos dados retornados.

---

## Estrutura do Projeto

```
projeto-tarefas/
│
├── main.py            # Arquivo principal da aplicação
├── models.py          # Modelos de dados (Pydantic)
├── requeriments.txt   # Lista de dependências
└── resumo.md          # Documentação do projeto
```

---

##  Exemplo de Código

### `main.py`

```python
from fastapi import FastAPI, HTTPException
from models import Tarefa
from typing import List

app = FastAPI()

tarefas: List[Tarefa] = []

@app.get("/tarefas/", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.get("/tarefas/{id}", response_model=Tarefa)
def listar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
    raise HTTPException(status_code=404, detail="Não encontrado")

@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return tarefa
```

### `models.py`

```python
from pydantic import BaseModel

class Tarefa(BaseModel): #quando vier o json ele vai fazer as conversoes para esse valor 
    id:int #vai ser gerado manual 
    descricao:str
    prioridade:int
    concluida:bool #tipo boleano 
```

### `requeriments.txt`

```text
fastapi
uvicorn
pydantic
```

---


