class Pessoa():
    def __init__(self,nome: str, telefone: str, idade: int, sexo: str):
        self.__nome = None
        self.__telefone = None
        self.__idade = None
        self.__sexo = None

        if isinstance(nome,str):
            self.__nome = nome
        if isinstance(telefone,str):
            self.__telefone = telefone
        if isinstance(idade,int):
            self.__idade = idade
        if isinstance(sexo,str):
            self.__sexo = sexo
       
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome


    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone


    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade


    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo: str):
        if isinstance(sexo, str):
            self.__sexo = sexo