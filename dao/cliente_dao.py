from abstract_dao import AbstractDAO
from entidade.cliente import Cliente

class ClienteDAO(AbstractDAO):
    def __init__(self):
        super().__init__("clientes.pkl")
    
    def add(self, cliente: Cliente):
        if isinstance(cliente, Cliente) and isinstance(cliente.cpf, str) and (cliente is not None):
            super().add(cliente.cpf, cliente)        
    
    def update(self, cliente: Cliente):
        if isinstance(cliente, Cliente) and isinstance(cliente.cpf, str) and (cliente is not None):
            super().update(cliente.cpf, cliente)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)