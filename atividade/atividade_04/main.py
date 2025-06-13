# importa biblioteca
import os

# lista
nomes = []

while True:
    print(f"{'-'*30} MENU {'-'*30}")
    print("1 - Inserir novo nome na lista")
    print("2 - Exibir lista")
    print("3 - Pesquisar nome na lista")
    print("4 - Sair do programa")

    opcao = input("Opção desejada: ").strip()

    os.system("cls")
    match opcao:
        case "1":
            novo_nome = input("Informe o nome a ser cadastrado: ").strip().title()
            os.system("cls")
            try:
                nomes.append(novo_nome) # type: ignore
                print(f"{novo_nome} inserido com sucesso.")
            except Exception as e:
                print(f"Não foi possível inserir nome na lista. {e}.")
            finally:
                continue
        case "2":
            print("\nLista:\n")
            try:
                for nome in nomes: # type: ignore
                    print(nome) # type: ignore
                print("\n")
            except Exception as e:
                print(f"Não foi possível exibir a lista. {e}.")
            finally:
                continue
        case "3":
            nome_pesquisado = input("Informe o nome a pesquisar: ").title().strip()
            os.system("cls")
            result = nomes.count(nome_pesquisado) # type: ignore
            print(f"{nome_pesquisado} foi encontrado {result} vezes.")
            continue
        case "4":
            print("Programa encerrado! ;) ")
            break
        case _:
            print("Opção inválida.")
            continue
