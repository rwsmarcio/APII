from Livro import Livro
from Autor import Autor
from Fila import Fila

a1 = Autor('01', 'Saramago')
a2 = Autor('02', 'Monteiro Lobato')
a3 = Autor('03', 'J.R.R. Tolkien')

l1 = Livro('001', 'Ensaio Sobre a Cegueira', a1)
l2 = Livro('002', 'Sítio do Pica-pau Amarelo', a2)
l3 = Livro('003', 'O Hobbit', a3)


print('----------------------------Autores----------------------------')
a1.getInformaçõesAutor()
print('---------------------')
a2.getInformaçõesAutor()
print('---------------------')
a3.getInformaçõesAutor()

print('----------------------------Livros----------------------------')
l1.getInformacoesLivro()
print('---------------------')
l2.getInformacoesLivro()
print('---------------------')
l3.getInformacoesLivro()

print('----------------------------Fila----------------------------')

f1 = Fila()

print('>>> Adicionando na fila:')
f1.imprimir()
f1.adicionar(l1)
f1.imprimir()
f1.adicionar(l2)
f1.imprimir()
f1.adicionar(l3)
f1.imprimir()

print('>>> Removendo da fila na fila:')
f1.imprimir()
f1.remover()
f1.imprimir()
f1.remover()
f1.imprimir()
f1.remover()
f1.imprimir()




