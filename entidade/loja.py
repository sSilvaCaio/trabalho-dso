from ..dao.veiculo_cadastrado_dao import VeiculoCadastradoDAO
from ..dao.veiculo_em_estoque_dao import VeiculoEmEstoqueDAO
from ..dao.marca_dao import MarcaDAO
from ..dao.servico_dao import ServicoDAO
from ..dao.tipo_servico_dao import TipoServicoDAO
from ..dao.cliente_dao import ClienteDAO
from ..dao.fornecedor_dao import FornecedorDAO
from ..dao.compra_dao import CompraDAO
from ..dao.venda_dao import VendaDAO


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

        self.__veiculos_cadastrados_dao = VeiculoCadastradoDAO()
        self.__veiculos_em_estoque_dao = VeiculoEmEstoqueDAO()
        self.__fornecedores_dao = FornecedorDAO()
        self.__clientes_dao = ClienteDAO()
        self.__servicos_dao = ServicoDAO()
        self.__compra_dao = CompraDAO()
        self.__venda_dao = VendaDAO()
        self.__marcas_dao = MarcaDAO()
        self.__tipos_servico_dao = TipoServicoDAO()

    def __str__(self):
        return (
            f"--- Loja ---\n"
            f"  Nome: {self.nome}\n"
            f"  CNPJ: {self.cnpj}\n"
            f"  Endereço: {self.endereco}\n"
            f"  Veículos em estoque: {len(self.veiculos_em_estoque)}\n"
            f"  Clientes cadastrados: {len(self.clientes_cadastrados)}\n"
            f"  Fornecedores cadastrados: {len(self.fornecedores_cadastrados)}\n"
        )

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
    def veiculo_cadastrado_dao(self):
        return self.__veiculo_cadastrado_dao

    @property
    def veiculos_em_estoque_dao(self):
        return self.__veiculos_em_estoque_dao

    @property
    def fornecedores_cadastrados(self):
        return self.__fornecedores_dao

    @property
    def fornecedor_dao(self):
        return self.__fornecedores_dao

    @property
    def clientes_cadastrados(self):
        return self.__clientes_dao

    @property
    def cliente_dao(self):
        return self.__clientes_dao

    @property
    def servico_dao(self):
        return self.__servico_dao

    @property
    def transacoes(self):
        return (self.__compra_dao, self.__venda_dao)

    @property
    def compra_dao(self):
        return self.__compra_dao

    @property
    def venda_dao(self):
        return self.__venda_dao

    @property
    def marca_dao(self):
        return self.__marca_dao

    @property
    def tipo_servico_dao(self):
        return self.__tipo_servico_dao
