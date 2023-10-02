from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Produto]
    vendas: List[Pedido]
    compras: List[Pedido]

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario: User
    

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: User
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    descricao: Optional[str] = "Sem observações..."
