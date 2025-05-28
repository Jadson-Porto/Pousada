from sqlalchemy import Column, Integer, String
from modelos.base import Base

class Cliente(Base):
    __tablename__ = "Cliente"
    
    Id = Column(Integer, primary_key=True)
    Nome = Column(String(100), nullable=False)
    Telefone = Column(String(20))
    Cpf = Column(String(14))