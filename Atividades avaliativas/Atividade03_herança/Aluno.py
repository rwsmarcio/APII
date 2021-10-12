
class Aluno():

    def __init__(self, codigoA = None, nomeA = None, matriculaA = None):
        self.codigo = codigoA
        self.nome = nomeA
        self.matricula = matriculaA
    
    def imprime(self):
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Matrícula: ", self.codigo)
