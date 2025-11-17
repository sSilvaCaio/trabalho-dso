from .abstract_dao import BaseDAO

from ..entidade.veiculo import Veiculo


class VeiculoDAO(BaseDAO):
    def __init__(self, datasource: str = "veiculos.pkl"):
        super().__init__(datasource)

    def add(self, veiculo):
        if (
            (veiculo is not None)
            and isinstance(veiculo, Veiculo)
            and isinstance(veiculo.chassi, int)
            and veiculo.chassi > 0
        ):
            super().add(veiculo.chassi, veiculo)

    def update(self, veiculo: Veiculo):
        if (
            (veiculo is not None)
            and isinstance(veiculo, Veiculo)
            and isinstance(veiculo.chassi, int)
            and veiculo.chassi > 0
        ):
            super().update(veiculo.chassi, veiculo)

    def get(self, key: int):
        if isinstance(key, int) and key > 0:
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int) and key > 0:
            return super().remove(key)
