from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

def Limpar():
    os.system("cls" if os.name == "nt" else "clear")

try:
    engine = create_engine("sqlite:///db_atividade_10")
    Base = declarative_base()

    class pessoa(Base):
        __tablename__ = "pessoa"
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=True)
        cpf = Column(String, nullable=False, unique=True)
        email = Column(String, nullable=False, unique=True)
        data_nasc = Column(Date, nullable=False)
        telefone = Column(String, nullable=False, unique=True)
        profissao = Column(String, nullable=False)
        endereco = Column(String, nullable=False)
        altura = Column(Float, nullable=True)
        peso = Column(Float, nullable=True)

    Base.metadata.create_all(engine)

except Exception as e:
    print(f"Erro no sistema. {e}.")

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    nome = input("Informe o nome: ").strip().title()
    data_nasc = input("Informe a data de nascimento: (dd/mm/aaaa): ").strip()
    data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y").date()
    email = input("Informe o e-mail: ").strip().lower()
    cpf = input("Informe o CPF: ").strip()
    telefone = input("Informe o telefone: ").strip()
    profissao = input("Informe sua profissão: ").strip()
    endereco = input("Informe o seu endereço: ").strip()
    altura = float(input("Informe sua altura: ").strip().replace(",", "."))
    peso = float(input("Informe seu peso: ").strip().replace(",", "."))

    nova_pessoa = pessoa(
        nome=nome,
        data_nasc=data_nasc,
        email=email,
        cpf=cpf,
        telefone=telefone,
        profissao=profissao,
        endereco=endereco,
        altura=altura,
        peso=peso
    )

    session.add(nova_pessoa)
    session.commit()

    Limpar()
    print("Pessoa cadastrada com sucesso.")

except Exception as e:
    print(f"Erro no sistema. {e}.")

pessoas = session.query(pessoa).all()
print(f"\n {'-'*20} MEU BANCO {'-'*20} ")    

for pessoa in pessoas:
    print(f"ID: {pessoa.id_pessoa}")
    print(f"Nome: {pessoa.nome}")
    print(f"Data de nascimento: {pessoa.data_nasc}")
    print(f"CPF: {pessoa.cpf}")
    print(f"Email: {pessoa.email}")
    print(f"Telefone: {pessoa.telefone}")
    print(f"Profissão: {pessoa.profissao}")
    print(f"Endereço: {pessoa.endereco}")
    print(f"Altura: {pessoa.altura}")
    print(f"Peso: {pessoa.peso}")