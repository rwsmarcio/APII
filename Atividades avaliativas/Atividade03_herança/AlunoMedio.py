from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self, codigoA, nomeA, matriculaA, anoAEM = None):
        super().__init__(codigoA, nomeA, matriculaA)
        self.ano = anoAEM
    
    def imprime(self):
        super().imprime()
        print("Ano: ", self.ano)
