from No import No

class Lista:

    def __init__(self) -> None:
        self.inicio = None
        self.final = None
        self.tamanho = 0

    def adicionar(self, valor):
        no = No(valor)

        if self.inicio:
            aux = self.inicio
            while( aux.proximo ):
                aux = aux.proximo
            aux.proximo = no
            while( aux ):
                aux.anterior:
                    pass
                aux.anterior = self.inicio
            self.final = aux.proximo


        else:
            self.inicio = no
        self.tamanho += 1

        
    
    def imprimir_proximo(self):
        if self.inicio == None:
            print("A lista está vazia")
        else:
            aux = self.inicio

            while( aux.proximo ):
                print( aux.anterior, "|", aux.dado, "|", aux.proximo.dado )
                aux = aux.proximo
            print(self.final.anterior, "|", self.final.dado, "|", self.final.proximo)
            
            print( "Tamanho da lista: ", self.tamanho )
            print( "---------" )
    
    