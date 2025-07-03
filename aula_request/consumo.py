import requests

URL = 'http://127.0.0.1:8000/'
def listar_livros(titulo):
   r = requests.get(f'{URL}/livros') 
   if r.status_code == 200:
       print(r.text)


def cadastrar_livros():
    pass

def excluir_livros():
    pass

def menu():
    print("1 - Listar Livros")
    print('2 - Listar Livros Pelo titulo')
    print('3 - Cadastrar Livros')
    print('4 - Deletar Livros')
    print('5 - Sair')
    return int(input('Digite sua escolha: '))

opcao = menu()


while opcao != 5:
    if opcao == 1:
        listar_livros()
    elif opcao == 2:
        titulo = input('Digite  titulo: ')
        listar_livros(titulo)
    elif opcao == 3:
       cadastrar_livros()
    elif opcao == 4:
        titulo = input("Digit o nome do livro: ")
        excluir_livros(titulo)

