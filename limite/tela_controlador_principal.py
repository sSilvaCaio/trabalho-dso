from controlador.controlador_principal import ControladorPrincipal


class TelaControladorPrincipal():
    def __init__(self, controlador: ControladorPrincipal):
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print("----Controle principal iniciado!!!!----")

    def mostra_tela_opcoes(self):
        print("Escolha o que você quer acessar:")
        print("1: Veículo")
        print("2: Listar")
        print("3: Alterar")
        print("4: Deletar")
        print("0: Voltar")

        opcao_escolhida = self.le_num_inteiro('Número desejado: ', [0, 1, 2, 3, 4, 5])

        return opcao_escolhida