class VeiculoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__('Veículo não foi encontrado')