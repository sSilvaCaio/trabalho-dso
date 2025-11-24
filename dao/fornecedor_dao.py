from dao.abstract_dao import BaseDAO 
from entidade.fornecedor import Fornecedor

class FornecedorDAO(BaseDAO):
    def __init__(self):
        super().__init__("fornecedor.pkl")
    
    def add(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.cnpj, str) and (fornecedor is not None):
            return super().add(fornecedor.cnpj, fornecedor)        
    
    def update(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.cnpj, str) and (fornecedor is not None):
            return super().update(fornecedor.cnpj, fornecedor)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
                
    def get_all(self):
        return super().get_all()
