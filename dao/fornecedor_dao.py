from dao.abstract_dao import BaseDAO 
from entidade.venda import Venda

class VendaDAO(BaseDAO):
    def __init__(self):
        super().__init__("vendas.pkl")
    
    def add(self, venda: Venda):
        if isinstance(venda, Venda) and isinstance(venda.id, int) and (venda is not None):
            return super().add(venda.id, venda)        
    
    def update(self, venda: Venda):
        if isinstance(venda, Venda) and isinstance(venda.id, int) and (venda is not None):
            return super().update(venda.id, venda)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
