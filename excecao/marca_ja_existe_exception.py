class MarcaJaExisteException(Exception):
    def __init__(self, nome_marca: str):
        self.nome_marca = nome_marca
        super().__init__(f'Já existe uma marca com o nome "{nome_marca}" cadastrada.')