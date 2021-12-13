from Autor import Autor

class Livro(Autor):

    def __init__(self, id_livro = 0, titulo_livro = 0, autor = 0):    
        self.id = id_livro
        self.titulo = titulo_livro
        self.autor = autor

    @property
    def id_livro(self):
        return self.id
    
    @id_livro.setter
    def id_livro(self, valor):
        self.id = valor

    @property
    def titulo_livro(self):
        return self.titulo
    
    @titulo_livro.setter
    def titulo_livro(self, valor):
        self.titulo_livro = valor
    
    @property
    def autor_livro(self):
        return self.autor_livro
    
    @autor_livro.setter
    def autor_livro(self, valor):
        self.autor_livro = valor
    
    def getInformacoesLivro(self):
        print("- Livro ID: ", self.id_livro)
        print("- Título: ", self.titulo_livro)
        print("- Autor: ")
        print(self.autor.getInformaçõesAutor())
