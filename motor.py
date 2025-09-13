class Motor():
    def __init__(self, potencia: str, quilometragem: int):
        self.__potencia = None
        self.__quilometragem = None

        if isinstance(potencia, str):
            self.__potencia = potencia
        
        if isinstance(quilometragem, int):
            self.__quilometragem = quilometragem
    
    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, potencia):
        if isinstance(potencia, str):
            self.__potencia = potencia
    
    @property
    def quilometragem(self):
        return self.__quilometragem

    @quilometragem.setter
    def quilometragem(self, quilometragem):
        if isinstance(quilometragem, int):
            self.__quilometragem = quilometragem