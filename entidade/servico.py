from .veiculo import Veiculo
from .tipo_servico import TipoServico
from datetime import date


class Servico:
    __proximo_id = 1

    def __init__(self, tipo_servico: TipoServico, veiculo: Veiculo, valor: float, data: date):
        self.__id = Servico.__proximo_id
        Servico.__proximo_id += 1

        self.__tipo_servico = None
        self.__veiculo = None
        self.__valor = None
        self.__data = None

        self.tipo_servico = tipo_servico
        self.veiculo = veiculo
        self.valor = valor
        self.data = data

    @property
    def id(self):
        return self.__id

    @property
    def tipo_servico(self):
        return self.__tipo_servico

    @tipo_servico.setter
    def tipo_servico(self, tipo_servico: TipoServico):
        if isinstance(tipo_servico, TipoServico):
            self.__tipo_servico = tipo_servico

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    def __str__(self):
        return (
            f"  ID: {self.id}\n"
            f"  Data: {self.data}\n"
            f"  Veículo: {self.veiculo.chassi}\n"
            f"  Tipo: {self.tipo_servico}\n"
            f"  Valor: R$ {self.valor:.2f}"
        )