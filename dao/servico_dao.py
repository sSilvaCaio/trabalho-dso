from .abstract_dao import BaseDAO

from ..entidade.servico import Servico


class ServicoDAO(BaseDAO):
    def __init__(self, datasource: str = "servicos.pkl"):
        super().__init__(datasource)

    def add(self, servico):
        if (
            (servico is not None)
            and isinstance(servico, Servico)
            and isinstance(servico.id, int)
        ):
            super().add(servico.id, Servico)

    def update(self, servico: Servico):
        if (
            (servico is not None)
            and isinstance(servico, Servico)
            and isinstance(servico.id, int)
        ):
            super().update(servico.id, servico)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key: str):
        if isinstance(key, str):
            return super().remove(key)
