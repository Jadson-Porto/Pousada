from sqlalchemy import (
    create_engine, Column, Integer, String, Date, DateTime,
    ForeignKey, DECIMAL, Text, UniqueConstraint, PrimaryKeyConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    
    id_cliente = Column(Integer, primary_key=True, nullable=False)
    nome_cliente = Column(String(100), nullable=True)
    telefone = Column(String(15), nullable=True)
    cpf = Column(String(18), unique=True, nullable=True)
    
    reservas = relationship("Reserva", back_populates="cliente")


class Status(Base):
    __tablename__ = 'status'
    
    nome = Column(String(30), primary_key=True, nullable=False)
    
    disponibilidades = relationship("Disponibilidade", back_populates="status_rel")
    reservas = relationship("Reserva", back_populates="status")


class Quarto(Base):
    __tablename__ = 'quarto'
    
    nro = Column(Integer, primary_key=True, nullable=False)
    preco = Column(DECIMAL(10, 2), nullable=False)
    descricao = Column(Text, nullable=True)
    
    disponibilidades = relationship("Disponibilidade", back_populates="quarto")


class Disponibilidade(Base):
    __tablename__ = 'disponibilidade'
    
    data_reserva = Column(DateTime, primary_key=True)
    nro_quarto = Column(Integer, ForeignKey('quarto.nro'), primary_key=True)
    status = Column(String(30), ForeignKey('status.nome'), nullable=True)
    
    quarto = relationship("Quarto", back_populates="disponibilidades")
    status_rel = relationship("Status", back_populates="disponibilidades")


class Reserva(Base):
    __tablename__ = 'reserva'
    
    nro_reserva = Column(Integer, primary_key=True, nullable=False)
    nome_status = Column(String(30), ForeignKey('status.nome'), nullable=True)  # ajustado para 30
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    nro_quarto_inicio = Column(Integer, nullable=True)
    nro_quarto_fim = Column(Integer, nullable=True)
    data_reserva = Column(DateTime, nullable=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'), nullable=True)
    
    cliente = relationship("Cliente", back_populates="reservas")
    status = relationship("Status", back_populates="reservas")

    __table_args__ = (
        ForeignKeyConstraint(
            ['data_inicio', 'nro_quarto_inicio'],
            ['disponibilidade.data_reserva', 'disponibilidade.nro_quarto']
        ),
        ForeignKeyConstraint(
            ['data_fim', 'nro_quarto_fim'],
            ['disponibilidade.data_reserva', 'disponibilidade.nro_quarto']
        ),
    )
