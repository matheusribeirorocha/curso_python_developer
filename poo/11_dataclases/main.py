from classes import Pessoa

if __name__ == "__main__":
    usuario = Pessoa(
    nome="",
    idade=0,
    email="",
    telefone="",
    profissao="",
    peso=0.0,
    altura=0.0
    )

usuario.nome = "Matheus"
usuario.idade = 24
usuario.email = "matheus@gmail.com"
usuario.telefone = "61986022242"
usuario.profissao = "programador"
usuario.peso = 90
usuario.altura = 1.80


print(f"{usuario}, tenho {len(usuario)} anos. Segue meus dados.")
print(f"Nome: {usuario.nome}")
print(f"Idade: {usuario.idade}")
print(f"Email: {usuario.email}")
print(f"Telefone: {usuario.telefone}")
print(f"Profissao: {usuario.profissao}")
print(f"Peso: {usuario.peso}")
print(f"Altura: {usuario.altura}")

del(usuario)

