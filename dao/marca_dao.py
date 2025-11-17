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
            super().add(marca.nome, marca)

    def update(self, marca: Marca):
        if (
            (marca is not None)
            and isinstance(marca, Marca)
            and isinstance(marca.nome, str)
        ):
            super().update(marca.nome, marca)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key: str):
        if isinstance(key, str):
            return super().remove(key)
