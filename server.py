from fastapi import FastAPI, status, Depends 
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repository.produto import RepositorioProduto
from src.infra.sqlalchemy.repository.user import RepositorioUser


criar_bd()

app = FastAPI()

@app.delete('/produtos')
def deletar_produto(produto: schemas.ProdutoDelete, session: Session = Depends(get_db)):
    RepositorioProduto(session).Remover(produto)
    return "Produto Deletado"

@app.put('/produtos')
def editar_produto(produto: schemas.Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).Editar(produto)
    return produto
    
@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas.ProdutoSimples)
def criar_produto(produto: schemas.Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).Criar(produto)
    return produto_criado

@app.get('/produtos', response_model=List[schemas.Produto])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).Listar()
    return produtos



@app.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: schemas.User, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUser(session).Criar(usuario)
    return usuario_criado

@app.get('/usuarios', response_model=List[schemas.User])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUser(session).Listar()
    return usuarios