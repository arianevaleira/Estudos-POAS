from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

try:
    df = pd.read_csv("pedidos.csv", sep=";", dtype=str, encoding='utf-16')
    df["IdPedido"] = df["IdPedido"].astype(str)
except FileNotFoundError:
    raise RuntimeError("Arquivo 'pedidos.csv' não encontrado.")
except Exception as e:
    raise RuntimeError(f"Erro ao carregar o arquivo CSV: {e}")

@app.get("/pedido/{id_pedido}")
def get_pedido(id_pedido: str):
    pedido = df[df["IdPedido"] == id_pedido]
    if pedido.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido.iloc[0].to_dict()
