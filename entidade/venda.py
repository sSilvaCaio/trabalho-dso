from .transacao import Transacao
from .cliente import Cliente
from .veiculo import Veiculo


class Venda(Transacao):
    def __init__(self, veiculo: Veiculo, valor: float, cliente: Cliente):
        super().__init__(veiculo, valor)
        self.__cliente = None
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
