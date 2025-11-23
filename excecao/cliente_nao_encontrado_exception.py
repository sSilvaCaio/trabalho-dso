class ClienteNaoEncontradoException(Exception):
    def __init__(self, cpf: str = None):
        if cpf:
            self.cpf = cpf
            super().__init__(f'Cliente com CPF "{cpf}" não foi encontrado.')
        else:
            super().__init__('Cliente não foi encontrado.')
