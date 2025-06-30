from classes import Aluno, Curso
import os


def Limpar():
    os.system("cls" if os.name == "nt" else "clear" )

if __name__ == "__main__":
    alunos = []
    cursos = []
    matricula = 0


    while True:

        aluno = Aluno(nome="", matricula= 0, cpf="")
        curso = Curso(nome_curso="")


        print(f"{'-'*20} SISTEMA ESCOLAR {'-'*20}")
        print(f" 1 - Cadastra aluno: ")
        print(f" 2 - Cadasrar curso: ")
        print(f" 3 - Listar cursos: ")
        print(f" 4 - Listar alunos: ")
        print(f" 5 - matricular aluno no curso: ")
        print(f" 6 - Sair do programa: ")
        opcao = input("Informe a opção desejada: ").strip()

        Limpar()

        match opcao:

            case "1":
                try:
                    matricula += 1
                    aluno.nome = input("Informe o nome do aluno: ").strip().lower()
                    aluno.cpf = input("Informe seu CPF: ")
                    aluno.matricula = matricula

                    alunos.append(alunos)
                    Limpar()
                    
                    print(f"Aluno {aluno.nome} matriculado com sucesso.")
                    
                except Exception as e:
                    print(f"Não foi possível cadastrar o aluno {e}.")    
                finally:
                    continue

            case "2":
                try:
                    curso.nome_curso = input("Informe o curso: ")

                    cursos.append(curso)
                    Limpar()

                    print(f"Curso {curso.nome_curso} cadastrado com sucesso!")

                except Exception as e:
                    print(f"Não foi possível cadastrar curso. {e}.")
                finally:
                    continue    

            case "3":  
                try:
                    print(f"{'-'*10} LISTA DE ALUNOS {'-'*10}")
                    for aluno in alunos:
                        print(f"Nome: {aluno.nome}")
                        print(f"Matrícula: {aluno.matricula}")
                        print(f"CPF: {aluno.cpf}")
                        print('-'*40)
                    incricao = int(input("Informe matrícula: "))
                    if incricao in alunos.matricula:
                        aluno.nome = alunos.nome
                        aluno.matricula = alunos.matricula
                        aluno.cpf = alunos.cpf

                        Limpar()

                        print(f"{'-'*10} Lista de cursos {'-'*10}")
                        for curso in cursos:
                            print(f" Curso: {curso.nome_curso}")
                        curso_inscricao = input("curso desejado: ").strip().title()    

                        aluno.increver_curso(curso_inscricao)   
                        Limpar()

                        print(f" Aluno {aluno.nome} inscrito no curso {curso.nome_curso} com sucesso")
                    
                    else:
                        print("Não foi possível cadastrar a matrícula")
                except Exception as e:
                    print(f"Não foi possível matricular aluno no curso. {e}.")
                finally:
                    continue          

            case "4":
                    curso.nome_curso.sort()
                    for curso in cursos:
                        print(f"curso {curso.nome_curso}")
                        print(f"Alunos: ")
                        aluno.listar_curso().sort()
                        for aluno in curso.listar_cursos:
                            print(aluno)
                        print('-'*40)

            case "5":
                for aluno in alunos:
                    print(f"Nome: {aluno.nome}")    
                    print(f"Matrícula: {aluno.matricula}")            
                    print(f"CPF: {aluno.cpf}")
                    print("Cursos matriculados: ")
                    for curso in aluno.listar_cursos():
                        print(curso)
            case "6":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue    




































# from classes import Aluno, Curso



# if __name__ == "__main__":
#     aluno01 = Aluno("fulano", 101, "111.111.111-11")
#     aluno02 = Aluno("cicrano", 102, "111.111.111-11")
#     aluno03 = Aluno("beltrano", 103, "111.111.111-11")
#     aluno04 = Aluno("joão", 104, "111.111.111-11")
#     aluno05 = Aluno("maria", 105, "111.111.111-11")
#     aluno06 = Aluno("jose", 106, "111.111.111-11")
        
#     curso01 = Curso("Python Developer")    
#     curso02 = Curso("IA com Python")
#     curso03 = Curso("Desenvolvedor Java")


#     aluno01.inscrever_curso(curso01)
#     aluno02.inscrever_curso(curso01)
#     aluno03.inscrever_curso(curso01)

#     aluno04.inscrever_curso(curso02)
#     aluno05.inscrever_curso(curso02)

#     aluno06.inscrever_curso(curso03)

#     print(f"Curso {curso01.nome_curso} tem os alunos {curso01.listar_alunos}")



