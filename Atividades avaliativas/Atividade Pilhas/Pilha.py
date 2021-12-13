from No import No

class Pilha:

    def __init__(self) -> None:
        self.inicio = None
        self.topo = None
        self.tamanho = 0
    
    def adicionar(self, valor):
        no = No( valor )
        if self.tamanho == 0:
            self.inicio = no
            self.topo = no
        else:
            self.topo.proximo = no
            self.topo = no
        self.tamanho += 1
    
    def imprimir(self):
        texto = ""
        if self.inicio == None:
            texto = "Fila Vazia"
        else:
            aux = self.inicio
            while( aux ):
                texto = texto + str( aux.dado ) + " - "
                aux = aux.proximo
        print( texto, self.tamanho )
        print( "--------------------------------------" )

    def reduzir(self):
        if self.tamanho == 0:
            print( "Fila vazia" )
        elif self.tamanho == 1:
            self.inicio = None
            self.topo = None
            self.tamanho = 0
        else:
            aux1 = self.inicio
            aux2 = self.topo
            self.topo = None
            while (aux1.proximo != aux2 ):
                aux1 = aux1.proximo
            self.topo = aux1
            self.topo.proximo = None
            self.tamanho -= 1