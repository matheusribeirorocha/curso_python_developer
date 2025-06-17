"""
# criando um programa que faça as seguintes operações:
- inserir dados do novo usuários
- exibir lista de usuário
- alterar dados do usuário já cadastrado
- excluir usuário da lista
- sair do programa
OS dados a serem cadastrados serão os seguintes:
- nome
- data de nascimento
- email
- profissão
- Gênero

"""
# NOTE - a lista deve começar vazia

import os

usuarios = []

while True:

    print(f"{'-'*20} MENU {'-'*20}\n")
    print("1 - Cadastrar novo usuário")
    print("2 - Exibir lista de usuários")
    print("3 - Alterar dados do usuário")
    print("4 - Excluir usuário")
    print("5 - Sair do programa")
    
    opcao = input("Informe a opção desejada: ")
    os.system("cls")

    match opcao:
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe o nome: ")
            usuario['data_nascimento'] = input("Informe a data de nascimento (DD/MM/AAAA): ")
            usuario['email'] = input("Informe o email: ")
            usuario['profissao'] = input("Informe a profissão: ")
            usuario['genero'] = input("Informe o gênero: ")

            usuarios.append(usuario)
            os.system("cls")
            print(f"Usuário {usuario['nome']} cadastrado com sucesso!")
        
        case "2":
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for i, usuario in enumerate(usuarios, start=1):
                    print(f"Usuário {i}:")
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print("\n")

        case "3":
            nome = input("Informe o nome do usuário que deseja alterar: ").strip()
            encontrado = False
            
            for usuario in usuarios:
                if usuario['nome'].lower() == nome.lower():
                    encontrado = True
                    usuario['data_nascimento'] = input(f"Nova data de nascimento (atual: {usuario['data_nascimento']}): ")
                    usuario['email'] = input(f"Novo email (atual: {usuario['email']}): ")
                    usuario['profissao'] = input(f"Nova profissão (atual: {usuario['profissao']}): ")
                    usuario['genero'] = input(f"Novo gênero (atual: {usuario['genero']}): ")
                    os.system("cls")
                    print(f"Dados do usuário {usuario['nome']} alterados com sucesso!")
                    break
            
            if not encontrado:
                os.system("cls")
                print(f"Usuário {nome} não encontrado.")

        case "4":
            nome = input("Informe o nome do usuário que deseja excluir: ").strip()
            encontrado = False
            
            for i, usuario in enumerate(usuarios):
                if usuario['nome'].lower() == nome.lower():
                    encontrado = True
                    usuarios.pop(i)
                    os.system("cls")
                    print(f"Usuário {nome} excluído com sucesso!")
                    break
            
            if not encontrado:
                os.system("cls")
                print(f"Usuário {nome} não encontrado.")

        case "5":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")

