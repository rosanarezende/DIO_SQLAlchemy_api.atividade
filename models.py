from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#criar um SQLite - e q não tenha probelmas com acentuação
engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
#cria uma sessão de bd - pra conseguirmos fazer consultas, alterações
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine)) #saber em qual banco abrir a sessão

Base = declarative_base()
Base.query = db_session.query_property()

#nesse projeto teremos pessoas e pessoas terão atividades
#agora vamos criar tabelas

class Pessoas(Base):
    __tablename__='pessoas' #mas o nome de classe pode ser diferente da tabela
    id = Column(Integer, primary_key=True) #é nossa chave primária
    nome = Column(String(40), index=True) #cria índice pra essa coluna e deixa a consulta + rápida
    idade = Column(Integer)

    # quando mandar imprimir o objeto ele manda imprimir o q tá nessa função
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    #preciso relacionar atividades com pessoas - criar chave estrangeira
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')

    # quando mandar imprimir o objeto ele manda imprimir o q tá nessa função
    def __repr__(self):
        return '<Atividade {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)
    #create_all é q vai criar meu bd

if __name__ == '__main__':
    init_db()