from .pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: str, idade: int, sexo: str, cpf: str):
        super().__init__(nome, telefone, idade, sexo)
        self.__cpf = None

        if isinstance(cpf, str):
            self.cpf = cpf

    def __str__(self):
        return (
            f"--- Cliente ---\n"
            f"  Nome: {self.nome}\n"
            f"  CPF: {self.cpf}\n"
            f"  Telefone: {self.telefone}\n"
            f"  Idade: {self.idade}\n"
            f"  Sexo: {self.sexo}\n"
        )

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf
