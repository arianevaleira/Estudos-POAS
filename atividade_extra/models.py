from pydantic import BaseModel
from typing import Optional

class Pedido(BaseModel):
    IdPedido: int
    ProtocoloPedido: Optional[str]
    Esfera: Optional[str]
    UF: Optional[str]
    Municipio: Optional[str]
    OrgaoDestinatario: Optional[str]
    Situacao: Optional[str]
    DataRegistro: Optional[str]  
    PrazoAtendimento: Optional[str]
    FoiProrrogado: Optional[str]
    FoiReencaminhado: Optional[str]
    FormaResposta: Optional[str]
    OrigemSolicitacao: Optional[str]
    IdSolicitante: Optional[int]
    AssuntoPedido: Optional[str]
    SubAssuntoPedido: Optional[str]
    Tag: Optional[str]
    DataResposta: Optional[str]
    Decisao: Optional[str]
    EspecificacaoDecisao: Optional[str]
