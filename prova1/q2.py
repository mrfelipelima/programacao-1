class Aluno:
    def __init__(self, nome_aluno, matricula, curso, disciplina, nota):
        self.nome_aluno = nome_aluno
        self.matricula = matricula
        self.curso = curso
        self.disciplina = disciplina
        self.nota = nota

    def get_nome(self):
        return self.nome_aluno
    def set_nome(self, nome):
        self.nome_aluno = nome

    def get_matricula(self):
        return self.matricula
    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_curso(self):
        return self.curso
    def set_curso(self, curso):
        self.curso = curso

    def get_disciplina(self):
        return self.disciplina
    def set_disciplina(self, disciplina):
        self.disciplina = disciplina

    def get_nota(self):
        return self.nota
    def set_nota(self, nota):
        self.nota = nota

    def resultado(self):
        if(self.nota <= 7):
            return "Aluno reprovado com nota {}".format(self.nota)
        else:
            return "Aluno aprovado com nota {}".format(self.nota)
        
vitor = Aluno('Vitor', 123456, 'SI', 'POO', 10)

print(vitor.get_curso())
print(vitor.resultado())