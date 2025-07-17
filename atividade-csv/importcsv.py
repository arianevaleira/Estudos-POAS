import csv
from sqlmodel import Session
from models import Pedido
from main import engine

def importar_csv():
    with open("pedidos.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        pedidos = []

        for row in reader:
            pedido = Pedido(
                id=int(row["Pedido"]),
                protocolo_pedido=row["ProtocoloPedido"],
                esfera=row["Esfera"]
            )
            pedidos.append(pedido)

    with Session(engine) as session:
        session.add_all(pedidos)
        session.commit()
        
importar_csv()