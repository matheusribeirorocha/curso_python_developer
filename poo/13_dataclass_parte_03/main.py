from classes import PessoaFisica, PessoaJuridica
import os

def Limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(nome="", profissao="", genero="", email="", telefone="", endereco="")

    empresa = PessoaJuridica(nome_fantasia="", cnpj="", website="", email="", telefone="", endereco="")

    Limpar()
    print(f"{'-'*20}Dados do usuário{'-'*20}")   
    usuario.nome = input("Informe o nome: ").title().strip()
    usuario.profissao = input("Informe a profissão: ").strip()
    usuario.genero = input("Informe o gênero: ").strip()
    usuario.email = input("Informe o E-mail: ").strip().lower()
    usuario.telefone = input("Informe o Telefone: ").strip()
    usuario.endereco = input("Informe o Endereço: ").strip().title()


    print(f"{'-'*20}Dados do Empresa{'-'*20}")   
    empresa.nome_fantasia = input("Informe o nome fantasia: ").title().strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.website = input("Informe o Website da empresa ").strip().lower()
    empresa.email = input("Informe o E-mail: ").strip().lower()
    empresa.telefone = input("Informe o Telefone: ").strip()
    empresa.endereco = input("Informe o Endereço: ").strip().title()

    Limpar()

    print(f"{usuario}. Segue meus dados.")
    usuario.exibir_dados()
    print(f"{empresa}. Segue os dados da empresa.")

    del(usuario)
    del(empresa)