from .abstract_dao import BaseDAO

from entidade.veiculo import Veiculo


class VeiculoEmEstoqueDAO(BaseDAO):
    def __init__(self, datasource: str = "veiculos_em_estoque.pkl"):
        super().__init__(datasource)

    def add(self, veiculo):
        if (
            (veiculo is not None)
            and isinstance(veiculo, Veiculo)
            and isinstance(veiculo.chassi, int)
            and veiculo.chassi > 0
        ):
            return super().add(veiculo.chassi, veiculo)
        return False

    def update(self, veiculo: Veiculo):
        if (
            (veiculo is not None)
            and isinstance(veiculo, Veiculo)
            and isinstance(veiculo.chassi, int)
            and veiculo.chassi > 0
        ):
            return super().update(veiculo.chassi, veiculo)
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
