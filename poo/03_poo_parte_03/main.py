# classe
class Pessoa:
    def __init__(self, nome, idade, email, profissao):

        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao

    def apresentar(self):   
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade}, trabalho como {self.profissao}, e meu email é {self.email}.")    

if __name__ == "__main__":
    usuario = Pessoa("", 0, "", "")

    try:
        usuario.nome = input("Informe o nome de usuário: ").title().strip()
        usuario.idade = int(input("Informe a idade: "))
        usuario.email = input("Informe o email: ").lower().strip()
        usuario.profissao = input("Informe sua profissão: ").strip()

        usuario.apresentar()
    except Exception as e:
        print(f"Não foi possível executar o programa. {e}.")             