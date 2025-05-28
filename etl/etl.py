import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from modelos.cliente import Cliente
from modelos.data import Data
from modelos.quarto import Quarto
from modelos.status import Status
from modelos.reserva import Reserva
from etl.abstract_etl import AbstractETL

class ETL(AbstractETL):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)
        engine = create_engine(destino)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self._dados_extraidos = {}

    def extract(self):
        try:
            print("Extraindo dados do Excel...")
            planilhas = ["cliente", "data", "quarto", "reserva", "status"]
            for nome_planilha in planilhas:
                self._dados_extraidos[nome_planilha] = pd.read_excel(self.origem, sheet_name=nome_planilha)
            print("Extração concluída!")
        except FileNotFoundError as e:
            print(f"Erro: Arquivo não encontrado - {e}")
            raise
        except Exception as e:
            print(f"Erro inesperado na extração: {e}")
            raise

    def transform(self):
        try:
            print("Transformando dados...")
            self.transformed_data = {}
            for sheet, df in self._dados_extraidos.items():
                self.transformed_data[sheet] = df.fillna('')
            print("Transformação concluída!")
        except Exception as e:
            print(f"Erro na transformação: {e}")
            raise

    def load(self):
        try:
            print("Carregando dados no banco de dados...")
            for sheet, df in self.transformed_data.items():
                for _, row in df.iterrows():
                    if sheet == 'cliente':
                        obj = Cliente(**row.to_dict())
                    elif sheet == 'data':
                        obj = Data(**row.to_dict())
                    elif sheet == 'quarto':
                        obj = Quarto(**row.to_dict())
                    elif sheet == 'reserva':
                        obj = Reserva(**row.to_dict())
                    elif sheet == 'status':
                        obj = Status(**row.to_dict())
                    else:
                        continue
                    self.session.add(obj)
            self.session.commit()
            print("Carga concluída!")
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Erro ao carregar no banco: {e}")
            raise
        except Exception as e:
            print(f"Erro inesperado na carga: {e}")
            raise
        finally:
            self.session.close()