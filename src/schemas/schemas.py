from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    class Config:
        orm_mode = True
    

class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    descricao: Optional[str] = "Sem observações..."
