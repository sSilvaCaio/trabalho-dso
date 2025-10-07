from entidade.veiculo import Veiculo
from limite.tela_veiculo import TelaVeiculo
from excecoes.veiculoNaoEncontradoException import VeiculoNaoEncontradoException


class ControladorVeiculo:
    def __init__(self):
        self.__veiculos = []
        self.__tela_veiculo = TelaVeiculo(self)

    def busca_veiculo_por_chassi(self, chassi):
            for veiculo in self.__veiculos:
                if veiculo.chassi == chassi:
                    return veiculo
            else:
                raise VeiculoNaoEncontradoException


    def inicia(self):
        self.__tela_veiculo.mostra_tela_inicial()

    def cadastra_veiculo(self):
        try:
            dados_veiculo = self.__tela_veiculo.mostra_tela_cadastro()
            self.busca_veiculo_por_chassi(dados_veiculo['chassi'])

            if self.valida_dados_veiculo(dados_veiculo):
                novo_veiculo = Veiculo(
                    dados_veiculo["chassi"],
                    dados_veiculo["ano"],
                    dados_veiculo["cor"],
                    dados_veiculo["placa"],
                    dados_veiculo["potencia"],
                    dados_veiculo["quilometragem"],
                    dados_veiculo["marca"],
                )
                self.__veiculos.append(novo_veiculo)

                return novo_veiculo
        except TypeError as e:
            return self.__tela_veiculo.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_veiculo.mostra_mensagem_Exception(e)

    def lista_veiculos(self):
        return self.__tela_veiculo.mostra_tela_lista()

    def deleta_veiculo(self):
        try:
            chassi = self.__tela_veiculo.mostra_tela_deletar()
            veiculo = self.busca_veiculo_por_chassi(chassi)
            if veiculo:
                self.__veiculos.remove(veiculo)
                return True
        except TypeError as e:
            return self.__tela_veiculo.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_veiculo.mostra_mensagem_Exception(e)

    def altera_veiculo(self):
        try:
            novos_dados = self.__tela_veiculo.mostra_tela_alteracao()
            veiculo = self.busca_veiculo_por_chassi(novos_dados['chassi'])
            if veiculo.chassi == novos_dados["chassi"]:
                veiculo.ano = novos_dados["ano"]
                veiculo.cor = novos_dados["cor"]
                veiculo.placa = novos_dados["placa"]
                veiculo.motor.potencia = novos_dados["potencia"]
                veiculo.motor.quilometragem = novos_dados["quilometragem"]
                veiculo.marca = novos_dados["marca"]

                return self.abre_tela_informacoes_veiculo()

            return None
        except TypeError as e:
            return self.__tela_veiculo.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_veiculo.mostra_mensagem_Exception(e)
    
    def abre_tela_informacoes_veiculo(self):
        return self.__tela_veiculo.mostra_tela_informacoes_veiculo()

    def abre_tela_opcoes(self):
        switcher = {0: 'break', 1: self.cadastra_veiculo(), 2: self.lista_veiculos(), 3: self.altera_veiculo, 4: self.deleta_veiculo, 5: self.abre_tela_informacoes_veiculo()}
        while True:
            opcao = self.__tela_veiculo.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()