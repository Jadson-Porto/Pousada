from sqlalchemy import Column, Integer, String, ForeignKey, Date
from modelos.base import Base

class Data(Base):
    __tablename__ = "Data"
    
    Data = Column(Date, primary_key=True)
    Nro_quarto = Column(Integer, ForeignKey('Quarto.Nro'), primary_key=True)
    Status = Column(String(20), ForeignKey('Status.Nome'))