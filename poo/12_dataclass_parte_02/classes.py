from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str


@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str

    def __str__(self):
        return f"Olá meu nome é {self.nome}, trabalho com {self.profissao} e meu CPF é {self.cpf}, meu Email é {self.email}, meu telefone é {self.telefone} meu endereço é {self.endereco}."

    def __del__(self):
        print(f"Objeto{self.nome} destruido com sucesso.")

@dataclass 
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str
    
    def __str__(self):
        f"Smos da empresa {self.nome_fantasia}, da razão social {self.razao_social}, nosso CNPJ é {self.cnpj} Pode nos contatar pelo Email {self.email}, ou por telefone {self.telefone}, ou se preferir, vá ao nosso endereço {self.endereco}."    

    def __del__(self):
        print(f"Objeto {self.nome_fantasia} destruído com sucesso.")