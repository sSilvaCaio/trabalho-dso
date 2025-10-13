from abc import ABC
from .veiculo import Veiculo
from datetime import datetime

class Transacao(ABC):
    __contador_id = 0
    
    def __init__(self, veiculo: Veiculo, valor: float, data=None):
        self.__veiculo = None
        self.__valor = None
        self.__data = None
        
        Transacao.__contador_id += 1
        self.__id = Transacao.__contador_id
        
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo
        if isinstance(valor, float):
            self.__valor = valor
        
        if data is None:
            self.__data = datetime.now()
        elif isinstance(data, datetime):
            self.__data = data
    
    @property
    def id(self):
        return self.__id
    
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
    def data(self, data: datetime):
        if isinstance(data, datetime):
            self.__data = data
