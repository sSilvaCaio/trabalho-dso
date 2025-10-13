from .pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome: str, telefone: str, idade: int, sexo: str, cnpj: str):
        super().__init__(nome, telefone, idade, sexo)
        self.__cnpj = None
        if isinstance(cnpj, str):
            self.cnpj = cnpj
    
    def __str__(self):
        return (
            f"--- Fornecedor ---\n"
            f"  Nome: {self.nome}\n"
            f"  CNPJ: {self.cnpj}\n"
            f"  Telefone: {self.telefone}\n"
            f"  Idade: {self.idade}\n"
            f"  Sexo: {self.sexo}\n"
        )
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
