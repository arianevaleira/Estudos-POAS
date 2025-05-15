from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, LivroCreate, Biblioteca, Emprestimo
from typing import List
from fastapi.middleware.cors import CORSMiddleware
#import uuid
#from sqlmodel import Field, Session, SQLModel, create_engine, select implementar o banco 
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


usuarios: List[Usuario] = []

@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario:Usuario):
    usuario.id = usuarios[-1] + 1 
    usuarios.append(usuario)
    return usuario

@app.delete("/usuarios/{usu_id}", response_model=Usuario)
def excluir_usuario(usu_id:int):
    for index, usuario in enumerate(usuarios):
        if usu_id == usuario.id:
            del usuarios[index]
            return usuario
    raise HTTPException(status_code=404, detail="Não localizado")

livros: List[Livro] = []

@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

#@app.post('livros')
#def cadastrar_livro(livro:livro):
#    livro.uuid = uuid.uuid4()
#    acervo.append(livro)
#    return livro

#@app.get('/livros', response_model=List[Livro])
#def listar_livros():
#    return acervo
# ir fazendo rota por rota 


#app.post('/emprestimo', response_model=Emprestimo)
#def emprestimo(usuario:str, livro:str, data_emprestimo:str, )
#user = none 
# book = none 
#for u in usuarios:
#    if u.uuid == usuario: 
#       user = u 
# for l in acervo:
#         
#    if l.uuid == livro:
#       book = 1 
# dados = {
#    'usuarios': user, 
#     'livro': book,
#     'emprestimo':data_emprestimo,
#     'devolucao': data_devolucao
# }
#emprestimo=Emprestimo(**dados)
#emprestimos.append(emprestimo)
@app.post("/livros/", response_model=Livro)
def criar_livro(livro:LivroCreate):
    novo_livro = Livro(
        id=len(livros) + 1,
        titulo=livro.titulo,
        ano=livro.ano,
        edicao=livro.edicao
    )
    livros.append(novo_livro)
    return novo_livro
print(livros)

@app.delete("/livros/{liv_id}", response_model=Livro)
def excluir_livro(liv_id:int):
    for index, livro in enumerate(livros):
        if liv_id == livro.id:
            del livros[index]
            return livro
    raise HTTPException(status_code=404, detail="Não localizado")

bibliotecas: List[Biblioteca] = []

@app.get("/biblioteca/", response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.post("/biblioteca/", response_model=Biblioteca)
def criar_biblioteca(biblioteca:Biblioteca):
    biblioteca.id = len(bibliotecas) + 1
    bibliotecas.append(biblioteca)
    return biblioteca

@app.delete("/biblioteca/{biblioteca_id}", response_model=Biblioteca)
def excluir_biblioteca(biblioteca_id:int):
    for index, biblioteca in enumerate(bibliotecas):
        if biblioteca_id == biblioteca.id:
            del bibliotecas[index]
            return biblioteca
    raise HTTPException(status_code=404, detail="Não localizado")

emprestimos: List[Emprestimo] = []

@app.get("/emprestimos/", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.post("/emprestimos/", response_model=Emprestimo)
def criar_emprestimo(emprestimo:Emprestimo):
    emprestimo.id = emprestimos[-1] +1
    emprestimos.append(emprestimo)
    return emprestimo

@app.delete("/emprestimos/{emprestimo_id}", response_model=Emprestimo)
def excluir_emprestimo(emprestimo_id:int):
    for index, emprestimo in enumerate(emprestimos):
        if emprestimo_id == emprestimo.id:
            del emprestimos[index]
            return emprestimo
    raise HTTPException(status_code=404, detail="Não localizado")
