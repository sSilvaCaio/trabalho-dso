class FornecedorNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Fornecedor não encontrado!")
