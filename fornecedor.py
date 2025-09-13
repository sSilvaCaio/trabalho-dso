from pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome: str, telefone: str, idade: int, sexo: str, cnpj: str):
        super().__init__(nome, telefone, idade, sexo)
        self.__cnpj = None

        if isinstance(cnpj, str):
            self.cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
