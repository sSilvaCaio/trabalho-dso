from transacao import Transacao
from fornecedor import Fornecedor
from veiculo import Veiculo

class Compra(Transacao):
    def __init__(self, veiculo: Veiculo, valor: float, fornecedor: Fornecedor):
        super().__init__(veiculo, valor)
        self.__fornecedor = None
        if isinstance(fornecedor, Fornecedor):
            self.__fornecedor = fornecedor

    @property
    def fornecedor(self):
        return self.__fornecedor

    @fornecedor.setter
    def fornecedor(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor):
            self.__fornecedor = fornecedor
