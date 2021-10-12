from abc import ABCMeta, abstractmethod, abstractproperty


class Computador(metaclass=ABCMeta):

    def __init__(self, modelo = 0, cor = 0, preco = 0):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco

    @property
    def modelo(self):
        pass
    
    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        pass
    
    @property
    def cor(self):
        pass
    
    @cor.setter
    @abstractmethod
    def cor(self, valor):
        pass

    @property
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, valor):
        pass

    def getInformacoes(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preço: ", self.preco)

    @abstractmethod
    def cadastrar(self):
        pass
