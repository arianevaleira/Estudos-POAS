from sqlmodel import SQLModel, Field

class Pedido(SQLModel, table=True):
    id: int = Field(primary_key=True)
    protocolo_pedido: str = Field(index=False)
    esfera: str = Field(index=False)
