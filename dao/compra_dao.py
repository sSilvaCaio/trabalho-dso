from dao.abstract_dao import BaseDAO 
from entidade.compra import Compra

class CompraDAO(BaseDAO):
    def __init__(self):
        super().__init__("compras.pkl")
    
    def add(self, compra: Compra):
        if isinstance(compra, Compra) and isinstance(compra.id, int) and (compra is not None):
            return super().add(compra.id, compra)        
    
    def update(self, compra: Compra):
        if isinstance(compra, Compra) and isinstance(compra.id, int) and (compra is not None):
            return super().update(compra.id, compra)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
