from classes import PessoaFisica, PessoaJuridica
import os

def Limpar():
    os.system("cls" if os.name == "nt" else "clear")

    

    if __name__ == "__main__":
        usuario = PessoaFisica(nome="", cpf="", profissao="", email="", telefone="")
        empresa =PessoaJuridica(razao_social="", nome_fantasia="", cnpj="", email="", telefone="")


        print(f"{'-'*20}Dados do usuário{'-'*20}")
        usuario.nome = input("Informe o nome: ").title().strip()
        usuario.cpf = input("Informe o cpf: ").title().strip()
        usuario.profissao = input("Informe o Profissão: ").title().strip()
        usuario.email = input("Informe o E-mail: ").title().strip()
        usuario.telefone = input("Informe o Telefone: ").title().strip()

        Limpar()
        print(f"{'-'*20}Dados da empresa{'-'*20}")
        empresa.razao_social = input("Informe o nome: ").title().strip()
        empresa.nome_fantasia = input("Informe o cpf: ").title().strip()
        empresa.cnpj = input("Informe o Profissão: ").title().strip()
        empresa.email = input("Informe o E-mail: ").title().strip()
        empresa.telefone = input("Informe o Telefone: ").title().strip()

        Limpar()
        print(f"{'-'*20}Dados do usuário{'-'*20}")
        print(f"Nome: {usuario.nome}")
        print(f"CPF: {usuario.cpf}")
        print(f"Profissão: {usuario.profissao}")
        print(f"Gênero: {usuario.email}")
        print(f"Telefone: {usuario.telefone}")
        super().exibir_dados()

        print(f"{'-'*20}Dados do usuário{'-'*20}")
        print(f"Razão social: {empresa.razao_social}")
        print(f"Nome Fantasia: {empresa.nome_fantasia}")
        print(f"CNPJ: {empresa.cnpj}")
        print(f"E-mail: {empresa.email}")
        print(f"Telefone: {empresa.telefone}")
        super().exibir_dados()

    