'''
1) Construir código necessário em Python para implementar o seguinte projeto: 
Uma classe abstrata chamada de Computador que contém os atributos/propriedades modelo, cor e preço. 
Esta classe também possui um método getInformacoes() que retorna todos os valores dos atributos. 
Esta classe também possui um método abstrato cadastrar().

2) O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Computador. 
A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. 
Esta classe reimplementa o método getInformacoes() herdado de computador.

3) A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria.
Esta classe reimplementa o método getInformacoes() herdado de computador.

4) Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.
'''

from Desktop import Desktop
from Notebook import Notebook

print("--#--")

dsk1 = Desktop("Pentium", "Azul", "R$ 2.500,00", "Bivolt")
dsk1.getInformacoes()

print("--#--")

ntb1 = Notebook("MacBook", "Cinza", "R$ 4.500,00", "8h")
ntb1.getInformacoes()

print("--#--")
