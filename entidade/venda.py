from .transacao import Transacao
from .cliente import Cliente
from .veiculo import Veiculo

class Venda(Transacao):
    def __init__(self, veiculo: Veiculo, valor: float, cliente: Cliente, data=None):
        super().__init__(veiculo, valor, data)
        self.__cliente = None
        
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
    
    def __str__(self):
        valor_formatado = f"{self.valor:.2f}" if self.valor is not None else "0.00"
        data_formatada = self.data.strftime("%d/%m/%Y %H:%M") if self.data else "N/A"
        return (
            f"--- Venda #{self.id} ---\n"
            f"  Data: {data_formatada}\n"
            f"  Veículo: {self.veiculo.marca.nome if self.veiculo and self.veiculo.marca else 'N/A'} - Placa: {self.veiculo.placa if self.veiculo else 'N/A'}\n"
            f"  Chassi: {self.veiculo.chassi if self.veiculo else 'N/A'}\n"
            f"  Valor: R$ {valor_formatado}\n"
            f"  Cliente: {self.cliente.nome if self.cliente else 'N/A'}\n"
            f"  CPF: {self.cliente.cpf if self.cliente else 'N/A'}\n"
        )
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
