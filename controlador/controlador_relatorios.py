from limite.tela_relatorios import TelaRelatorios
from relatorios.gerador_de_relatorios import GeradorDeRelatorios

class ControladorRelatorios:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__gerador_relatorios = GeradorDeRelatorios(self)
        self.__tela = TelaRelatorios(self)

    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    @property
    def tela(self):
        return self.__tela
    
    @property
    def gerador_relatorios(self):
        return self.__gerador_relatorios

    def abre_tela_opcoes(self):
        switcher = {
            1: self.mostra_relatorio_servicos
        }

        while True:
            opcao = self.tela.mostra_tela_opcoes()

            if opcao == 0:
                break

            funcao = switcher.get(opcao)

            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")
    

    def mostra_relatorio_servicos(self):
        dados = self.gerador_relatorios.processa_dados_servicos_por_mes(self.__controlador_principal.loja)
        self.tela.mostra_relatorio_servicos_por_mes(dados)
    