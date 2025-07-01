from classes import PessoaFisica, PessoaJuridica
import os
def Limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(
        nome="",
        cpf="",
        profissao="",
        email="",
        telefone="",
        endereco=""  
     )
    
    empresa = PessoaJuridica(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        email="",
        telefone="",
        endereco=""
    )

    print("Informe os dados do usuário:\n ")

    usuario.nome = input("Informe o nome do usuario: ").strip().title()
    usuario.cpf = input("Informe o cpf do usuario: ").strip()
    usuario.profissao = input("Informe o profisão do usuario: ").strip()
    usuario.email = input("Informe o email do usuario: ").strip()
    usuario.telefone = input("Informe o endereco do usuario: ").strip()
    usuario.endereco = input("Infomre o endereço do usuario: ").strip()






        
    print("Informe os dados da empreas : \n")

    empresa.razao_social = input("Informe a razão social da empresa: ").strip().title()
    empresa.nome_fantasia = input("Informe o nome fantasia: ").strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o Email da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip()

 


