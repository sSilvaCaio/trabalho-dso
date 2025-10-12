from entidade.veiculo import Veiculo
from limite.tela_veiculo import TelaVeiculo
from .controlador_principal import ControladorPrincipal


class ControladorVeiculo:
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__veiculos = []
        self.__tela = TelaVeiculo(self)
        if isinstance(controlador_principal, ControladorPrincipal):
            self.__controlador_principal = controlador_principal
    
    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal
        
    def busca_veiculo_por_chassi(self, chassi):
            for veiculo in self.__veiculos:
                if veiculo.chassi == chassi:
                    return veiculo
            return None

    def inicia(self):
        self.tela.mostra_tela_inicial

    def cadastra_veiculo(self):
            dados_veiculo = self.tela.mostra_tela_cadastro()

            if self.busca_veiculo_por_chassi(dados_veiculo['chassi']):
                self.tela.mostra_mensagem_erro("Já existe um veículo com este chassi!")
                return None
            
            marca = self.controlador_principal.controlador_marca.busca_marca_por_nome(dados_veiculo['marca'])
            if not marca:
                self.controlador_principal.controlador_marca.tela.mostra_mensagem_erro('A marca  não foi encontrada.')
            
            novo_veiculo = Veiculo(
                dados_veiculo["chassi"],
                dados_veiculo["ano"],
                dados_veiculo["cor"],
                dados_veiculo["placa"],
                dados_veiculo["potencia"],
                dados_veiculo["quilometragem"],
                marca,
            )
            self.__veiculos.append(novo_veiculo)
            self.tela.mostra_mensagem_sucesso("Veículo cadastrado.")
            return novo_veiculo

    def lista_veiculos(self):
        self.tela.mostra_tela_lista(self.__veiculos)

    def deleta_veiculo(self):
        chassi = self.tela.mostra_tela_deletar()
        veiculo = self.busca_veiculo_por_chassi(chassi)
        if veiculo:
            self.__veiculos.remove(veiculo)
            self.tela.mostra_mensagem_sucesso('Veículo deletado.')
            return True
        self.tela.mostra_mensagem_erro("Não existe veículo com este chassi.")
        return False

    def altera_veiculo(self):
        novos_dados = self.tela.mostra_tela_alteracao()

        veiculo = self.busca_veiculo_por_chassi(novos_dados['chassi'])

        if not veiculo:
            self.tela.mostra_mensagem_erro('Não existe veículo com este chassi.')
            return None
        
        marca = self.controlador_principal.controlador_marca.busca_marca_por_nome(novos_dados['marca'])

        if not marca:
            self.controlador_principal.controlador_marca.tela.mostra_mensagem_erro(f'A marca {novos_dados['marca']} não foi encontrada.')

        veiculo.ano = novos_dados["ano"]
        veiculo.cor = novos_dados["cor"]
        veiculo.placa = novos_dados["placa"]
        veiculo.motor.potencia = novos_dados["potencia"]
        veiculo.motor.quilometragem = novos_dados["quilometragem"]
        veiculo.marca = marca

        self.tela.mostra_mensagem_sucesso('Veículo alterado.')
        return veiculo

    
    def abre_tela_opcoes(self):
        switcher = {0: 'Voltar', 1: self.cadastra_veiculo, 2: self.lista_veiculos, 3: self.altera_veiculo, 4: self.deleta_veiculo}
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()