from sqlalchemy import Column, Integer, String, Date, ForeignKey
from modelos.base import Base

class Reserva(Base):
    __tablename__ = "Reserva"
    
    Nro = Column(Integer, primary_key=True)
    Nome_status = Column(String(20), ForeignKey('Status.Nome'))
    Data_inicio_data = Column(Date, ForeignKey('Data.Data'))
    Numero_quarto_data_inicio = Column(Integer, ForeignKey('Data.Nro_quarto'))
    Data_fim_data = Column(Date)
    Nro_quarto_data_fim = Column(Integer)
    Data = Column(Date)
    Id_cliente = Column(Integer, ForeignKey('Cliente.Id'))