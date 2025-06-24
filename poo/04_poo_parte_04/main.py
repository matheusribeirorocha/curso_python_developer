
import random

class pessoa:
    def __init__(self, nome, email, profissao, humor):
        self.nome = nome
        self.email = email
        self.profissao = profissao
        self.humor = humor
    
    def dar_boas_vindas(self):  
        return "Olá, boa tarde!"
    
    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}, é um prazer!"
    def perguntar(self):
        return f"Qual o seu nome?"
    def cartao_de_visita(self):
        print(f"Nome:{self.nome}")
        print(f"E-mais: {self.email}")
        print(f"Profissão: {self.profissao}")
    
    def ofender(self):
        return f"Quem liga? Me erra! Vai ver se eu tô na esquina!"
    
if __name__ == "__main__":  
    usuario_masculino = pessoa("", "", "", bool(random.getrandbits(1)))
    usuario_feminino = pessoa("", "", "", bool(random.getrandbits(1)))

    usuario_masculino.nome = input("Informe seu nome: ").title().strip()
    usuario_masculino.email = input("Infomre seu E-mail: ").lower().strip()
    usuario_masculino.profissao = input("Infome sua profissão: ").strip()
    
    usuario_feminino.nome = input("Informe seu nome: ").title().strip()
    usuario_feminino.email = input("Infomre seu E-mail: ").lower().strip()
    usuario_feminino.profissao = input("Infome sua profissão: ").strip()

    print(f"Homem: -{usuario_masculino.dar_boas_vindas()}")
    print(f"Mulher: -{usuario_feminino.dar_boas_vindas()} ")
    print(f"Homem: -{usuario_masculino.perguntar()}")
    if usuario_feminino.humor is True:
        print(f"Mulher: -{usuario_feminino.cumprimentar()}")
        print(f"Mulher -{usuario_feminino.perguntar()}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homem: -{usuario_masculino.cumprimentar()}")
        print(f"Homem: Bom humor = {usuario_masculino.humor}")
        print(f"Segue meu cartão de visitas:")
    else:
        print(f"Mulher: -{usuario_feminino.ofender()}")
        usuario_masculino.humor = usuario_feminino.humor
        print(f"Homem: Bom humor = {usuario_masculino.humor}")    