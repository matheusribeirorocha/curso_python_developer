# classes

class pessoa:
    nome = "Matheus Ribeiro"
    idade = 24
    email = "matheus@gmail.com"
    profissao = "Programador"


# algorítimo principal

if __name__ == "__main__":

    usuario = pessoa()

    print(f"Nome: {usuario.nome}.")
    print(f"Idade: {usuario.idade}.")
    print(f"email: {usuario.email}.")
    print(f"Profissão: {usuario.profissao}.")
    
        