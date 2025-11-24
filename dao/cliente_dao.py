from dao.abstract_dao import BaseDAO
from entidade.cliente import Cliente

class ClienteDAO(BaseDAO):
    def __init__(self):
        super().__init__("clientes.pkl")
    
    def add(self, cliente: Cliente):
        if isinstance(cliente, Cliente) and isinstance(cliente.cpf, str) and (cliente is not None):
            return super().add(cliente.cpf, cliente)        
    
    def update(self, cliente: Cliente):
        if isinstance(cliente, Cliente) and isinstance(cliente.cpf, str) and (cliente is not None):
            return super().update(cliente.cpf, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
    
    def get_all(self):
        return super().get_all()
