from .marca import Marca
from .motor import Motor


class Veiculo:
    def __init__(
        self,
        chassi: int,
        ano: int,
        cor: str,
        placa: str,
        potencia: str,
        quilometragem: int,
        marca: Marca,
    ):
        self.__chassi = None
        self.__ano = None
        self.__cor = None
        self.__placa = None
        self.__motor = None
        self.__marca = None

        if isinstance(chassi, int):
            self.__chassi = chassi

        if isinstance(ano, int):
            self.__ano = ano

        if isinstance(cor, str):
            self.__cor = cor

        if isinstance(placa, str):
            self.__placa = placa

        if isinstance(potencia, str) and isinstance(quilometragem, int):
            self.__motor = Motor(potencia, quilometragem)

        if isinstance(marca, Marca):
            self.__marca = marca

    @property
    def chassi(self):
        return self.__chassi

    @chassi.setter
    def chassi(self, chassi):
        if isinstance(chassi, int):
            self.__chassi = chassi

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        if isinstance(cor, str):
            self.__cor = cor

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        if isinstance(placa, str):
            self.__placa = placa

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, potencia, quilometragem):
        if isinstance(potencia, str) and isinstance(quilometragem, int):
            self.__motor = Motor(potencia, quilometragem)

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        if isinstance(marca, Marca):
            self.__marca = marca
