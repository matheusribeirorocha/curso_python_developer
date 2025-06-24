# Classe
class Pessoa:
    nome = "Matheus Ribeiro"
    idade = 24
    email = "matheus@gmail.com"
    profissao = "programador"

# funções
    def apresentar(self):   
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade}, trabalho como {self.profissao}, e meu email é {self.email}.")    

# algorítimo principal
if __name__ == "__main__":
    
    # instância a classe
    usuario = Pessoa()

    # executar o método
    usuario.apresentar()
