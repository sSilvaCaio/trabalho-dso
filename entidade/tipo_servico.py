class TipoServico:
    __proximo_id = 1

    def __init__(self, nome: str):
        self.__id = TipoServico.__proximo_id
        TipoServico.__proximo_id += 1
        self.__nome = None

        if isinstance(nome, str):
            self.__nome = nome

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    def __str__(self):
        return f"{self.__nome}"
