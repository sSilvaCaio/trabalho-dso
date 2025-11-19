from .abstract_dao import BaseDAO

from ..entidade.tipo_servico import TipoServico


class TipoServicoDAO(BaseDAO):
    def __init__(self, datasource: str = "tipos_servico.pkl"):
        super().__init__(datasource)

    def add(self, tipo_servico):
        if (
            (tipo_servico is not None)
            and isinstance(tipo_servico, TipoServico)
            and isinstance(tipo_servico.id, int)
            and tipo_servico.id > 0
        ):
            return super().add(tipo_servico.id, tipo_servico)
        return False

    def update(self, tipo_servico: TipoServico):
        if (
            (tipo_servico is not None)
            and isinstance(tipo_servico, TipoServico)
            and isinstance(tipo_servico.id, int)
            and tipo_servico.id > 0
        ):
            return super().update(tipo_servico.id, tipo_servico)
        return False

    def get(self, key: int):
        if isinstance(key, int) and key > 0:
            return super().get(key)
        return None

    def remove(self, key: int):
        if isinstance(key, int) and key > 0:
            return super().remove(key)
        return False

    def get_by_nome(self, nome: str):
        if isinstance(nome, str):
            tipos = self.get_all()
            for tipo in tipos:
                if tipo.nome == nome:
                    return tipo
        return None

    def get_all(self):
        return super().get_all()
