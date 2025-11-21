from .abstract_dao import BaseDAO

from entidade.servico import Servico


class ServicoDAO(BaseDAO):
    def __init__(self, datasource: str = "servicos.pkl"):
        super().__init__(datasource)

    def add(self, servico):
        if (
            (servico is not None)
            and isinstance(servico, Servico)
            and isinstance(servico.id, int)
            and servico.id > 0
        ):
            return super().add(servico.id, servico)
        return False

    def update(self, servico: Servico):
        if (
            (servico is not None)
            and isinstance(servico, Servico)
            and isinstance(servico.id, int)
            and servico.id > 0
        ):
            return super().update(servico.id, servico)
        return False

    def get(self, key: int):
        if isinstance(key, int) and key > 0:
            return super().get(key)
        return None

    def remove(self, key: int):
        if isinstance(key, int) and key > 0:
            return super().remove(key)
        return False

    def get_all(self):
        return super().get_all()
