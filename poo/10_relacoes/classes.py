class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.cursos_inscritos = []

    @property
    def nome(self, nome):
        return self.nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self, matricula):
        return self.matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula     

    @property
    def cpf(self, cpf):
        return self.cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf    
        
    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)    

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome_inscritos)
            return lista

    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome_aluno)

    def __del__(self):
        print(f"objeto{self.nome} destruido com sucesso.")

class Curso:
        def __init__(self, nome_curso):
                self.__nome_curso = nome_curso
                self.alunos_escritos = []

        @property
        def nome_curso(self, nome_curso):
            return self.__nome_curso
        
        @nome_curso.setter
        def nome_curso(self, nome_curso):
            self.__nome_curso = nome_curso    

        def adicionar_aluno(self, aluno, matricula, cpf):
            if aluno not in self.alunos_inscritos:
                self.alunos_inscritos.append(aluno) 
                aluno.inscrever_curso(self)           

        def __del__(self):
            print(f"objeto{self.nome_curso} destruido com sucesso.")        

