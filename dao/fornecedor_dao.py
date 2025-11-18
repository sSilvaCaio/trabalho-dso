from abstract_dao import BaseDAO 
from entidade.fornecedor import Fornecedor

class FornecedorDAO(BaseDAO):
    def __init__(self):
        super().__init__("fornecedor.pkl")
    
    def add(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.id_fornecedor, str) and (fornecedor is not None):
            super().add(fornecedor.id_fornecedor, fornecedor)        
    
    def update(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.id_fornecedor, str) and (fornecedor is not None):
            super().update(fornecedor.id_fornecedor, fornecedor)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)