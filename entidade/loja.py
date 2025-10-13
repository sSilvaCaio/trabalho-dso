from .fornecedor import Fornecedor
from .cliente import Cliente
from .veiculo import Veiculo
from .servico import Servico


class Loja:
    def __init__(self, nome: str, cnpj: str, endereco: str):
        self.__nome = None
        self.__cnpj = None
        self.__endereco = None

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
        if isinstance(endereco, str):
            self.__endereco = endereco

        self.__veiculos_cadastrados = []
        self.__veiculos_em_estoque = []
        self.__fornecedores = []
        self.__clientes = []
        self.__servicos_prestados = []
        self.__transacoes = []
        self.__marcas = []
        self.__tipos_servico = []


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def veiculos_cadastrados(self):
        return self.__veiculos_cadastrados

    @property
    def veiculos_em_estoque(self):
        return self.__veiculos_em_estoque

    @veiculos_em_estoque.setter
    def veiculos_em_estoque(self, veiculos: list):
        if isinstance(veiculos, list):
            self.__veiculos_em_estoque = veiculos

    @property
    def fornecedores(self):
        return self.__fornecedores

    @fornecedores.setter
    def fornecedores(self, fornecedores: list):
        if isinstance(fornecedores, list):
            self.__fornecedores = fornecedores

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, clientes: list):
        if isinstance(clientes, list):
            self.__clientes = clientes

    @property
    def servicos_prestados(self):
        return self.__servicos_prestados

    @servicos_prestados.setter
    def servicos_prestados(self, servicos: list):
        if isinstance(servicos, list):
            self.__servicos_prestados = servicos
    
    @property
    def transacoes(self):
        return self.__transacoes
    
    @property
    def marcas(self):
        return self.__marcas
    
    @property
    def tipos_servico(self):
        return self.__tipos_servico
    
