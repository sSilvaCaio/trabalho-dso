from .abstract_dao import BaseDAO

from ..entidade.marca import Marca


class MarcaDAO(BaseDAO):
    def __init__(self, datasource: str = "marcas.pkl"):
        super().__init__(datasource)

    def add(self, marca):
        if (
            (marca is not None)
            and isinstance(marca, Marca)
            and isinstance(marca.id, int)
            and marca.id > 0
        ):
            return super().add(marca.id, marca)
        return False

    def update(self, marca: Marca):
        if (
            (marca is not None)
            and isinstance(marca, Marca)
            and isinstance(marca.id, int)
            and marca.id > 0
        ):
            return super().update(marca.id, marca)
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
            marcas = self.get_all()
            for marca in marcas:
                if marca.nome == nome:
                    return marca
        return None

    def get_all(self):
        return super().get_all()
