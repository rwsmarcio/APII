from Computador import Computador

class Desktop( Computador ):

    def __init__(self, modelo=0, cor=0, preco=0, potenciaDaFonte = 0):
        super().__init__(modelo=modelo, cor=cor, preco=preco)
        self._potencia = potenciaDaFonte
    
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
    
    def getInformacoes(self):
        super().getInformacoes()
        print("Potência da Fonte: ", self._potencia)
    
    def cadastrar(self):
        pass
