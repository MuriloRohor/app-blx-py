from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUser():

    def __init__(self, db: Session) -> None:
        self.db = db

    def Criar(self, usuario: schemas.User,):
        db_usuario = models.User(
            nome = usuario.nome,
            telefone = usuario.telefone
        )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    

    def Listar(self):
        usuarios = self.db.query(models.User).all()
        return usuarios

    def Obter(self):
        pass

    def Remover(self):
        pass