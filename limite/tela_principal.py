from .tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaPrincipal(TelaAbstrata):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_inicial(self):
        sg.popup_ok("Sistema Iniciado!")

    def mostra_tela_finalizar(self):
        sg.popup_ok("Sistema Finalizado!")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text('LOJA DE VEÍCULOS', font=('Arial', 16, 'bold'))],
            [sg.Text('--- MÓDULOS PRINCIPAIS ---')],
            [sg.Button('Gerenciar Veículos', size=(25,1))],
            [sg.Button('Gerenciar Clientes', size=(25,1))],
            [sg.Button('Gerenciar Fornecedores', size=(25,1))],
            [sg.Text('--- MÓDULOS DE REGISTRO ---')],
            [sg.Button('Gerenciar Vendas', size=(25,1))],
            [sg.Button('Gerenciar Compras', size=(25,1))],
            [sg.Button('Gerenciar Serviços', size=(25,1))],
            [sg.Text('--- CADASTROS E RELATÓRIOS ---')],
            [sg.Button('Gerenciar Marcas', size=(25,1))],
            [sg.Button('Gerenciar Tipos de Serviço', size=(25,1))],
            [sg.Button('Ver Relatórios', size=(25,1))],
            [sg.Button('Sair do Sistema', size=(25,1))],
        ]

        janela = sg.Window('Menu Principal', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Sair do Sistema':
                janela.close()
                return 0
            mapping = {
                'Gerenciar Veículos': 1,
                'Gerenciar Clientes': 2,
                'Gerenciar Fornecedores': 3,
                'Gerenciar Vendas': 4,
                'Gerenciar Compras': 5,
                'Gerenciar Serviços': 6,
                'Gerenciar Marcas': 7,
                'Gerenciar Tipos de Serviço': 8,
                'Ver Relatórios': 9,
            }
            if evento in mapping:
                janela.close()
                return mapping[evento]
