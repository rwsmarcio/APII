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
            no.anterior = aux

        else:
            self.inicio = no
        self.final = no
        self.tamanho += 1
    
    def adicionar2(self, valor):
        no = No(valor)
        if self.final:
            self.final.proximo = no
            no.anterior = self.final
        else:
            self.inicio = no
        self.final = no
        self.tamanho += 1


        
    
    def imprimir_proximo(self):
        if self.inicio == None:
            print("A lista está vazia")
        else:
            print("Lista crescente: ")
            aux = self.inicio
            print(aux.anterior, "|", aux.dado,"|", aux.proximo.dado)
            while(aux.proximo):
                if (aux.anterior):
                    print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo.dado)
                aux = aux.proximo
            aux = self.final
            print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo)
            print( "Tamanho da lista: ", self.tamanho )
            print( "---------" )
    
    def imprimir_anterior2(self):
        if self.final == None:
            print("A lista está vazia")
        else:
            print("Lista decrescente: ")
            aux = self.final
            print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo)
            while(aux.anterior):
                if (aux.proximo):
                    print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo.dado)
                aux = aux.anterior
            aux = self.final
            print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo)
            print( "Tamanho da lista: ", self.tamanho )
            print( "---------" )
    
    def imprimir_anterior3(self):
        if self.final == None:
            print("A lista está vazia")
        else:
            print("Lista decrescente: ")
            aux = self.final
            print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo)
            while(aux.anterior):
                if (aux.proximo):
                    print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo.dado)
                aux = aux.anterior
            aux = self.final
            print(aux.anterior.dado, "|", aux.dado,"|", aux.proximo)
            print( "Tamanho da lista: ", self.tamanho )
            print( "---------" )
    
    