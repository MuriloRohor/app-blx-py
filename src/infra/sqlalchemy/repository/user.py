from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUser():

    def __init__(self, session: Session) -> None:
        self.session = session

    def Criar(self, usuario: schemas.User,):
        db_usuario = models.User(
            nome = usuario.nome,
            senha = usuario.senha,
            telefone = usuario.telefone
        )
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario
    

    def Listar(self):
        stmt = select(models.User)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios

    def Obter(self):
        pass

    def Remover(self):
        pass