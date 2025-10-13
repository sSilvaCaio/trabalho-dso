from entidade.loja import Loja

from limite.tela_principal import TelaPrincipal

from controlador.controlador_veiculo import ControladorVeiculo
from controlador.controlador_marca import ControladorMarca
from controlador.controlador_cliente import ControladorCliente
from controlador.controlador_fornecedor import ControladorFornecedor
from controlador.controlador_servico import ControladorServico
from controlador.controlador_tipo_servico import ControladorTipoServico
from controlador.controlador_venda import ControladorVenda
from controlador.controlador_compra import ControladorCompra
from controlador.controlador_relatorios import ControladorRelatorios

from relatorios.gerador_de_relatorios import GeradorDeRelatorios


class ControladorPrincipal:
    def __init__(self):
        self.__tela = TelaPrincipal(self)

        self.__loja = Loja("Concessionária Padrão", "11.222.333/0001-44", "Rua Principal, 123")

        self.__controlador_relatorios = ControladorRelatorios(self)
        self.__controlador_veiculo = ControladorVeiculo(self)
        self.__controlador_marca = ControladorMarca(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_fornecedor = ControladorFornecedor(self)
        self.__controlador_servico = ControladorServico(self)
        self.__controlador_tipo_servico = ControladorTipoServico(self)
        self.__controlador_venda = ControladorVenda(self)
        self.__controlador_compra = ControladorCompra(self)

    @property
    def tela(self):
        return self.__tela

    @property
    def loja(self):
        return self.__loja

    @property
    def controlador_veiculo(self):
        return self.__controlador_veiculo

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente
        
    @property
    def controlador_fornecedor(self):
        return self.__controlador_fornecedor
    
    @property
    def controlador_servico(self):
        return self.__controlador_servico
    
    @property
    def controlador_tipo_servico(self):
        return self.__controlador_tipo_servico
    
    @property
    def controlador_marca(self):
        return self.__controlador_marca
    
    @property
    def controlador_venda(self):
        return self.__controlador_venda
    
    @property
    def controlador_compra(self):
        return self.__controlador_compra
    
    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios
    
    def inicia_sistema(self):
        self.abre_tela_opcoes()

    def finaliza_sistema(self):
        self.__tela.mostra_tela_finalizar()
        exit()

    def abre_tela_opcoes(self):
        switcher = {
            1: self.controlador_veiculo.abre_tela_opcoes,
            2: self.controlador_cliente.abre_tela_opcoes,
            3: self.controlador_fornecedor.abre_tela_opcoes,
            4: self.controlador_venda.abre_tela_opcoes,
            5: self.controlador_compra.abre_tela_opcoes,
            6: self.controlador_servico.abre_tela_opcoes,
            7: self.controlador_marca.abre_tela_opcoes,
            8: self.controlador_tipo_servico.abre_tela_opcoes,
            9: self.controlador_relatorios.abre_tela_opcoes,   
            0: self.finaliza_sistema
        }

        while True:
            opcao_escolhida = self.__tela.mostra_tela_opcoes()
            funcao_a_ser_executada = switcher.get(opcao_escolhida)

            if funcao_a_ser_executada:
                if opcao_escolhida == 0:
                    funcao_a_ser_executada()
                    break
                else:
                    funcao_a_ser_executada()
            else:
                self.__tela.mostra_mensagem_erro("Opção inválida, tente novamente.")