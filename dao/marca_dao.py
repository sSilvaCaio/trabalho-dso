from .abstract_dao import BaseDAO

from ..entidade.marca import Marca


class MarcaDAO(BaseDAO):
    def __init__(self, datasource: str = "marcas.pkl"):
        super().__init__(datasource)

    def add(self, marca):
        if (
            (marca is not None)
            and isinstance(marca, Marca)
            and isinstance(marca.nome, str)
        ):
            return super().add(marca.nome, marca)
        return False

    def update(self, marca: Marca):
        if (
            (marca is not None)
            and isinstance(marca, Marca)
            and isinstance(marca.nome, str)
        ):
            return super().update(marca.nome, marca)
        return False

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
        return None

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
        return False
