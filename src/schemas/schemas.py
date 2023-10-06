from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    
    class Config:
        orm_mode = True

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

    
class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    descricao: Optional[str] = "Sem observações..."
