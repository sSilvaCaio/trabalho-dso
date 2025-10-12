class Marca():
    def __init__(self, nome:str):
        self.__nome = None

        if isinstance(nome, str):
            self.__nome = nome
        
    def __str__(self):
        return self.nome
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome