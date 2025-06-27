from classes import Pessoa
import os

def Limpar():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    usuario = Pessoa(nome="", profissao="", idade="")
    while True:
        print("-1 Inserir dados e exibir dados")
        print("-2 Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        Limpar()
        match opcao:
            case "1":
                try:

                    usuario.nome = input("Informe o nome: ").strip().title()
                    usuario.idade = int(input("Informe o idade: "))
                    usuario.profissao = input("Informe sua profissão: ").strip()

                    Limpar()
                    print(usuario)
                    print(f"Idade de {usuario.nome}: {len(usuario)} anos.")
                except Exception as e:
                    print(f"Não foi possível infomrar a idade")

            case"2":
                break

            case _:
                print("Opção inválida.")        
                continue

            

        


