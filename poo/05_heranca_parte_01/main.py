import classes
import os
if __name__ == "__main__":
    usuario = classes.pessoafisica("", "", "", "", "", "")
    empresa = classes.pessoajuridica("", "", "", "", "", "")

    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.profissao = input("Informe sua profissão: ").strip()
    usuario.genero = input("Informe seu gênero: ").strip().lower()
    usuario.endereco = input("Informe seu endereço: ").strip().lower()
    usuario.email = input("Informe seu E-mail: ").strip()
    
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}\n")
    
    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").title().strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()                          
    empresa.email = input("Informe E-mail: ").strip().lower()
    empresa.endereco = input("Informe o endereço da empresa: ").title().strip()
    empresa.telefone = input("Informe o telefone : ").strip()

    os.system("cls" if os.name == "nt" else "clear")







    usuario.exibir_dados()

