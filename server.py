from fastapi import FastAPI, status, Depends 
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repository.produto import RepositorioProduto
from src.infra.sqlalchemy.repository.user import RepositorioUser

criar_bd()

app = FastAPI()



@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas.ProdutoSimples)
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).Criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).Listar()
    return produtos

@app.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: schemas.User, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUser(db).Criar(usuario)
    return usuario_criado

@app.get('/usuarios', status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUser(db).Listar()
    return usuarios