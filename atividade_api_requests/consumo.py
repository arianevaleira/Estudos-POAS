import requests 

URL = 'http://127.0.0.1:8000/'

def listar_livros(titulo):
    r = requests.get(f'{URL}/livros')
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)


def listar_livros():
    r = requests.get(f'{URL}/livros')
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def cadastrar_livros():
    titulo = input('Digite o titulo: ')
    ano = input('Digite o ano: ')
    edicao = input('Digite a edicao: ')
   
    livro = {
        'titulo': titulo,
        'ano': ano, 
        'edicao': edicao
    }

    r = requests.post(f'{URL}/livros', json=livro)


def editar_livros(titulo):
    titulo = input('Digite o titulo: ')
    ano = input('Digite o ano: ')
    edicao = input('Digite a edicao: ')
   
    livro = {
        'titulo': titulo,
        'ano': ano, 
        'edicao': edicao
    }

    if r.status_code == 200:
        print('Atualizado com sucesso')
    elif r.status_code == 404:
        print(r.text)


    r = requests.put(f'{URL}/livros/{titulo}', json=livro)
    


def excluir_livro(titulo):
    r = requests.delete(f'{URL}/livros/{titulo}')
    if r.status_code == 200:
        print('Excluído com sucesso')
    else:
        print(r.text)

def menu():
    print('1 - Listar Livros')
    print('2 - Pesquisa livro por título: ')
    print('3 - Cadastrar Livro')
    print('4 - Deletar Livro')
    print('5 - Editar Livro')
    print('6 - Sair')
    return int(input('Digite sua opção: '))


opcao = menu()


while opcao != 6: 
    if opcao == 1:
       listar_livros()

    elif opcao == 2:
        titulo = input('Digite o titulo: ')
        listar_livros(titulo)

    elif opcao == 3:
        cadastrar_livros()

    elif opcao == 4:
        titulo = input('Digite o titulo: ')
        excluir_livro(titulo)
    
    elif opcao == 5:
        titulo = input('Digite o titulo: ')
        editar_livros(titulo)

    opcao = menu()