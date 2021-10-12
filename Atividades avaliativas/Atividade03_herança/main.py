from Aluno import Aluno
from AlunoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

aluno1 = Aluno("01", "Maurício", "00182535")
alunomedio1 = AlunoEnsinoMedio("02", "Ana", "00193548", "Terceiro")
alunograd1 = AlunoGraduacao("03", "Carlos", "00184568", "7°")

print("---- Aluno ----")
aluno1.imprime()
print("---- Aluno Ensino Médio ----")
alunomedio1.imprime()
print("---- Aluno Graduação ----")
alunograd1.imprime()