from veiculo import Veiculo

class Transacao():
    def __init__(self, veiculo: Veiculo, valor: float):
        self.__veiculo = None
        self.__valor = None

        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo
        if isinstance(valor, float):
            self.__valor = valor
    
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
