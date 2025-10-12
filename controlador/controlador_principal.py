from .controlador_veiculo import ControladorVeiculo
from .controlador_marca import ControladorMarca
from .controlador_servico import ControladorServico
from .controlador_tipo_servico import ControladorTipoServico
from limite.tela_controlador_principal import TelaControladorPrincipal


class ControladorPrincipal():
    def __init__(self):
        self.__tela = TelaControladorPrincipal(self)
        self.__controlador_veiculo = ControladorVeiculo(self)
        self.__controlador_servico = ControladorServico(self)
        self.__controlador_marca = ControladorMarca(self)
        self.__controlador_tipo_servico = ControladorTipoServico(self)

    @property
    def controlador_veiculo(self):
        return self.__controlador_veiculo
    
    @property
    def controlador_marca(self):
        return self.__controlador_marca
    
    @property
    def controlador_tipo_servico(self):
        return self.__controlador_tipo_servico

    def inicia(self):
        self.__tela.mostra_tela_inicial()
        self.abre_tela_opcoes()

    def inicia_controlador_veiculo(self):
        self.controlador_veiculo.inicia()

    def inicia_controlador_marca(self):
        self.controlador_marca.inicia()

    def inicia_controlador_tipo_servico(self):
        self.controlador_tipo_servico.inicia()
        
    def finalizar(self):
        print('Fim do programa!')
    
    def abre_tela_opcoes(self):
        switcher = {0: self.finalizar, 1: self.inicia_controlador_veiculo, 2: self.inicia_controlador_marca, 3: self.altera_veiculo, 4: self.deleta_veiculo}
        while True:
            opcao = self.__tela.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
            if opcao == 0:
                break
        exit()