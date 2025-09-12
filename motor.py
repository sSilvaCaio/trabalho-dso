class Motor():
    def __init__(self, potencia: str, ano: int):
        self.__potencia = None
        self.__ano = None

        if isinstance(potencia, str):
            self.__potencia = potencia
        
        if isinstance(ano, int):
            self.__ano = ano
    
    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, potencia):
        if isinstance(potencia, str):
            self.__potencia = potencia
    
    @property
    def ano(self):
        return self.__ano

    @potencia.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano