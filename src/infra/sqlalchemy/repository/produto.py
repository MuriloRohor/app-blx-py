from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
class RepositorioProduto():

    def __init__(self, db: Session) -> None:
        self.db = db

    def Criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel
            )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
        

    def Listar(self):
        pass

    def Obter(self):
        pass

    def Remover(self):
        pass