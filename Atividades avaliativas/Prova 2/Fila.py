from No import No

class Fila:

    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def adicionar(self, valor):
        no = No( valor )
        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1
    
    def imprimir(self):
        texto = ""
        if self.inicio == None:
            texto = "Fila Vazia"
        else:
            aux = self.inicio
            cont = 1
            while( aux ):
                texto = texto + str(cont) + ' - ' + str( aux.dado.titulo ) + " -> "
                aux = aux.proximo
                cont += 1
        print( texto )
        print( "--------------------------------------" )
    
    def remover(self):
        if self.tamanho == 0:
            print( "Fila vazia" )
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

        