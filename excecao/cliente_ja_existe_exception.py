class ClienteJaExisteException(Exception):
    def __init__(self, cpf: str):
        self.cpf = cpf
        super().__init__(f'Já existe um cliente com o CPF "{cpf}" cadastrado.')
