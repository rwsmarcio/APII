
class Autor():

    def __init__(self, id_autor, nome_autor):
        self._id = id_autor
        self.nome = nome_autor

    @property
    def id_autor(self):
        return self._id
    
    @id_autor.setter
    def id_autor(self, valor):
        self._id = valor
    
    @property
    def nome_autor(self):
        return self.nome
    
    @nome_autor.setter
    def nome_autor(self, valor):
        self.nome = valor

    def getInformaçõesAutor(self):
        print('ID Autor:', self._id)
        print('Nome: ', self.nome)