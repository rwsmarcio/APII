
from Aluno import Aluno


class AlunoGraduacao(Aluno):

    def __init__(self, codigoA, nomeA, matriculaA, semestreAG = None):
        super().__init__(codigoA, nomeA, matriculaA)
        self.semestre = semestreAG

    def imprime(self):
        super().imprime()
        print("Semestre: ", self.semestre)