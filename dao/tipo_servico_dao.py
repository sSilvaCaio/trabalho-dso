from .abstract_dao import BaseDAO

from ..entidade.tipo_servico import TipoServico


class TipoServicoDAO(BaseDAO):
    def __init__(self, datasource: str = "tipos_servico.pkl"):
        super().__init__(datasource)

    def add(self, tipo_servico):
        if (
            (tipo_servico is not None)
            and isinstance(tipo_servico, TipoServico)
            and isinstance(tipo_servico.nome, str)
        ):
            return super().add(tipo_servico.nome, tipo_servico)
        return False

    def update(self, tipo_servico: TipoServico):
        if (
            (tipo_servico is not None)
            and isinstance(tipo_servico, TipoServico)
            and isinstance(tipo_servico.nome, str)
        ):
            return super().update(tipo_servico.nome, tipo_servico)
        return False

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
        return None

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
        return False
