import requests

def buscar_pedido():
    try:
        id_pedido = int(input("Digite o ID do pedido: "))
        URL = f"http://localhost:8000/pedido/{id_pedido}"
        r = requests.get(URL)

        if r.status_code == 200:
            pedido = r.json()
            print("=== Pedido encontrado ===")
            for chave, valor in pedido.items():
                print(f"{chave}: {valor}")
        elif r.status_code == 404:
            print("Erro 404: Pedido não encontrado.")
        else:
            print(f"Erro: {r.status_code}")
    except ValueError:
        print("ID inválido. Digite um número inteiro.")
    except Exception as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    buscar_pedido()
