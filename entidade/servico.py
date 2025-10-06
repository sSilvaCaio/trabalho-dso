from .veiculo import Veiculo
from .tipo_servico import TipoServico
from datetime import date


class Servico:
    def __init__(
        self, tipo_servico: TipoServico, veiculo: Veiculo, valor: float, data: date
    ):
        self.__tipo_servico = None
        self.__veiculo = None
        self.__valor = None
        self.__data = None

        if isinstance(tipo_servico, TipoServico):
            self.__tipo_servico = tipo_servico

        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

        if isinstance(valor, float):
            self.__valor = valor

        if isinstance(data, date):
            self.__data = data
