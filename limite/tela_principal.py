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
        def abre_submenu(titulo, layout, mapping):
            try:
                janela_sub = sg.Window(titulo, layout)
                while True:
                    ev, vals = janela_sub.read()
                    if ev == sg.WINDOW_CLOSED or ev == 'Voltar':
                        janela_sub.close()
                        return None
                    if ev in mapping:
                        code = mapping[ev]
                        janela_sub.close()
                        return code
            except Exception as e:
                try:
                    sg.popup_error(f"Erro ao abrir submenu '{titulo}': {e}")
                except Exception:
                    pass
                return None

        while True:
            # Cria um layout novo a cada iteração para evitar reuso de elementos
            main_layout = [
                [sg.Text('LOJA DE VEÍCULOS', font=('Arial', 16, 'bold'))],
                [sg.Text('Escolha uma categoria:')],
                [sg.Button('Módulos Principais', size=(25,1))],
                [sg.Button('Módulos de Registro', size=(25,1))],
                [sg.Button('Cadastros e Relatórios', size=(25,1))],
                [sg.Button('Sair do Sistema', size=(25,1))],
            ]

            janela = sg.Window('Menu Principal', main_layout)
            evento, valores = janela.read()
            janela.close()
            if evento == sg.WINDOW_CLOSED or evento == 'Sair do Sistema':
                return 0

            if evento == 'Módulos Principais':
                layout_mp = [
                    [sg.Text('--- Módulos Principais ---', font=('Arial', 14, 'bold'))],
                    [sg.Button('Gerenciar Veículos', size=(25,1))],
                    [sg.Button('Gerenciar Clientes', size=(25,1))],
                    [sg.Button('Gerenciar Fornecedores', size=(25,1))],
                    [sg.Button('Voltar', size=(25,1))],
                ]
                mapping_mp = {
                    'Gerenciar Veículos': 1,
                    'Gerenciar Clientes': 2,
                    'Gerenciar Fornecedores': 3,
                }
                escolha = abre_submenu('Módulos Principais', layout_mp, mapping_mp)
                if escolha:
                    return escolha
                else:
                    continue

            if evento == 'Módulos de Registro':
                layout_mr = [
                    [sg.Text('--- Módulos de Registro ---', font=('Arial', 14, 'bold'))],
                    [sg.Button('Gerenciar Vendas', size=(25,1))],
                    [sg.Button('Gerenciar Compras', size=(25,1))],
                    [sg.Button('Gerenciar Serviços', size=(25,1))],
                    [sg.Button('Voltar', size=(25,1))],
                ]
                mapping_mr = {
                    'Gerenciar Vendas': 4,
                    'Gerenciar Compras': 5,
                    'Gerenciar Serviços': 6,
                }
                escolha = abre_submenu('Módulos de Registro', layout_mr, mapping_mr)
                if escolha:
                    return escolha
                else:
                    continue

            if evento == 'Cadastros e Relatórios':
                layout_cr = [
                    [sg.Text('--- Cadastros e Relatórios ---', font=('Arial', 14, 'bold'))],
                    [sg.Button('Gerenciar Marcas', size=(30,1))],
                    [sg.Button('Gerenciar Tipos de Serviço', size=(30,1))],
                    [sg.Button('Ver Relatórios', size=(30,1))],
                    [sg.Button('Voltar', size=(30,1))],
                ]
                mapping_cr = {
                    'Gerenciar Marcas': 7,
                    'Gerenciar Tipos de Serviço': 8,
                    'Ver Relatórios': 9,
                }
                escolha = abre_submenu('Cadastros e Relatórios', layout_cr, mapping_cr)
                if escolha:
                    return escolha
                else:
                    continue
