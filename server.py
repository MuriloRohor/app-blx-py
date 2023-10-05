from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repository.produto import RepositorioProduto
from src.infra.sqlalchemy.repository.user import RepositorioUser

criar_bd()

app = FastAPI()



@app.post('/produtos')
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db), status_code=status.HTTP_201_CREATED):
    produto_criado = RepositorioProduto(db).Criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db), status_code=status.HTTP_200_OK):
    produtos = RepositorioProduto(db).Listar()
    return produtos

@app.post('/usuarios')
def criar_usuario(usuario: schemas.User, db: Session = Depends(get_db), status_code=status.HTTP_201_CREATED):
    usuario_criado = RepositorioUser(db).Criar(usuario)
    return usuario_criado

@app.get('/usuarios')
def listar_usuarios(db: Session = Depends(get_db), status_code=status.HTTP_200_OK):
    usuarios = RepositorioUser(db).Listar()
    return usuarios