class MarcaNaoEncontradaException(Exception):
    def __init__(self, nome_marca: str = None, id_marca: int = None):
        if nome_marca:
            self.nome_marca = nome_marca
            super().__init__(f'Marca com nome "{nome_marca}" não foi encontrada.')
        elif id_marca:
            self.id_marca = id_marca
            super().__init__(f'Marca com ID {id_marca} não foi encontrada.')
        else:
            super().__init__('Marca não foi encontrada.')