class LojaNaoEncontradaException(Exception):
    def __init__(self):
        super().__init__('A Loja Não foi Encontrada')