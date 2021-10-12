from Computador import Computador

class Notebook( Computador ):

    def __init__(self, modelo=0, cor=0, preco=0, tempoDeBateria = 0):
        super().__init__(modelo=modelo, cor=cor, preco=preco)
        self.__tempoDeBateria = tempoDeBateria
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        self._preco = valor

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    @tempoDeBateria.setter
    def tempoDeBateria(self, valor):
        self.__tempoDeBateria = valor
    
    def getInformacoes(self):
        super().getInformacoes()
        print("Tempo de Bateria :", self.__tempoDeBateria)
    
    def cadastrar(self):
        pass