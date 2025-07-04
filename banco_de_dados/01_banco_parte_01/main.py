from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

def Limpar():
    os.system("cls" if os.name == "nt" else "clear")

try:
    engine = create_engine("sqlite:///meu_primeiro_banco.db")
    Base = declarative_base()

    # cria a entidade pessoa
    class pessoa(Base):
        # nome da entidade
        __tablename__ = "pessoa"

        # atributos
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        data_nasc = Column(Date, nullable=False)
        email = Column(String, nullable=False, unique=True)
        cpf = Column(String, nullable=False, unique=True)
        genero = Column(String, nullable=True)
        tipo_sanguineo = Column(String, nullable=True)
    
    # cria a tabela
    Base.metadata.create_all(engine)

   
except Exception as e:
    print(f"Erro no sistema. {e}.")


try:
    Session = sessionmaker(bind=engine)
    session = Session()

    # cadastrar usuário no banco
    nome = input("Informe o nome: ").strip().title()
    data_nasc = input("Informe a data de nascimento: (dd/mm/aaaa): ").strip()
    data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y").date()
    email = input("Informe o e-mail: ").strip().lower()
    cpf = input("Informe o CPF: ").strip()
    genero = input("Informe o gênero: ").strip()
    tipo_sanguineo = input("Informe o tipo sanguíneo: ").strip().upper()

    nova_pessoa = pessoa(
        nome=nome,
        data_nasc=data_nasc,
        email=email,
        cpf=cpf,
        genero=genero,
        tipo_sanguineo=tipo_sanguineo
    )

    session.add(nova_pessoa)
    session.commit()

    Limpar()
    print("Pessoa cadastrada com sucesso.")

    
except Exception as e:
    print(f"Não foi possível cadastrar novo usuário. {e}.")


# TODO
pessoas = session.query(pessoa).all()
print(f"\n {'-'*20} PESSOAS CADASTRADAS {'-'*20} ")

for pessoa in pessoas:
    print(f"ID: {pessoa.id_pessoa}")
    print(f"Nome: {pessoa.nome}")
    print(f"Data de nascimento: {pessoa.data_nasc.strftime("%d/%m/%Y")}")
    print(f"Email: {pessoa.email}")
    print(f"CPF: {pessoa.cpf}")
    print(f"Gênero: {pessoa.genero}")
    print(f"Tipo sanguíneo: {pessoa.tipo_sanguineo}")

