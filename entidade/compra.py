from .transacao import Transacao
from .fornecedor import Fornecedor
from .veiculo import Veiculo

class Compra(Transacao):
    def __init__(self, veiculo: Veiculo, valor: float, fornecedor: Fornecedor, data=None):
        super().__init__(veiculo, valor, data)
        self.__fornecedor = None
        
        if isinstance(fornecedor, Fornecedor):
            self.__fornecedor = fornecedor
    
    def __str__(self):
        valor_formatado = f"{self.valor:.2f}" if self.valor is not None else "0.00"
        data_formatada = self.data.strftime("%d/%m/%Y %H:%M") if self.data else "N/A"
        return (
            f"--- Compra #{self.id} ---\n"
            f"  Data: {data_formatada}\n"
            f"  Veículo: {self.veiculo.marca.nome if self.veiculo and self.veiculo.marca else 'N/A'} - Placa: {self.veiculo.placa if self.veiculo else 'N/A'}\n"
            f"  Chassi: {self.veiculo.chassi if self.veiculo else 'N/A'}\n"
            f"  Valor: R$ {valor_formatado}\n"
            f"  Fornecedor: {self.fornecedor.nome if self.fornecedor else 'N/A'}\n"
            f"  CNPJ: {self.fornecedor.cnpj if self.fornecedor else 'N/A'}\n"
        )
    
    @property
    def fornecedor(self):
        return self.__fornecedor
    
    @fornecedor.setter
    def fornecedor(self, fornecedor: Fornecedor):
        if isinstance(fornecedor, Fornecedor):
            self.__fornecedor = fornecedor
