from .tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaVenda(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Menu Vendas ---", font=("Arial", 14, "bold"))],
            [sg.Button("Registrar Venda", size=(20, 2))],
            [sg.Button("Listar Vendas", size=(20, 2))],
            [sg.Button("Alterar Venda", size=(20, 2))],
            [sg.Button("Deletar Venda", size=(20, 2))],
            [sg.Button("Voltar", size=(20, 2))],
        ]

        janela = sg.Window("Menu Vendas", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return 0
            if evento == "Registrar Venda":
                janela.close()
                return 1
            if evento == "Listar Vendas":
                janela.close()
                return 2
            if evento == "Alterar Venda":
                janela.close()
                return 3
            if evento == "Deletar Venda":
                janela.close()
                return 4

    def mostra_tela_cadastro(self):
        layout = [
            [sg.Text("--- Registrar Venda ---", font=("Arial", 14, "bold"))],
            [sg.Text("Chassi:", size=(15, 1)), sg.Input(key="chassi")],
            [sg.Text("CPF Cliente:", size=(15, 1)), sg.Input(key="cpf_cliente")],
            [sg.Text("Valor:", size=(15, 1)), sg.Input(key="valor")],
            [sg.Text("Data (dd/mm/aaaa):", size=(15, 1)), sg.Input(key="data")],
            [sg.Button("Registrar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Registrar Venda", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None
            if evento == "Registrar":
                chassi_s = valores.get("chassi", "").strip()
                if not chassi_s:
                    sg.popup_error("Chassi é obrigatório")
                    continue
                try:
                    chassi = int(chassi_s)
                except ValueError:
                    sg.popup_error("Chassi deve ser número inteiro")
                    continue

                cpf = valores.get("cpf_cliente", "").strip()
                if not cpf:
                    sg.popup_error("CPF do cliente é obrigatório")
                    continue

                valor_s = valores.get("valor", "").strip()
                try:
                    valor = float(valor_s)
                except ValueError:
                    sg.popup_error("Valor inválido")
                    continue

                data = valores.get("data", "").strip()
                if not data:
                    sg.popup_error("Data é obrigatória")
                    continue

                janela.close()
                return {"chassi": chassi, "cpf_cliente": cpf, "valor": valor, "data": data}

    def mostra_tela_lista(self, lista_vendas):
        if not lista_vendas:
            sg.popup_ok("Nenhuma venda registrada.")
            return
        vendas_str = [v.__str__() for v in lista_vendas]
        layout = [[sg.Text('--- Lista de Vendas ---', font=('Arial',14,'bold'))], [sg.Listbox(values=vendas_str, size=(90,12), key='lista')], [sg.Button('Fechar')]]
        janela = sg.Window('Lista de Vendas', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Fechar':
                janela.close()
                break

    def mostra_tela_deletar(self):
        layout = [[sg.Text('--- Deletar Venda ---', font=('Arial',14,'bold'))], [sg.Text('ID da venda:', size=(15,1)), sg.Input(key='id')], [sg.Button('Deletar'), sg.Button('Voltar')]]
        janela = sg.Window('Deletar Venda', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela.close()
                return None
            if evento == 'Deletar':
                id_s = valores.get('id','').strip()
                if not id_s:
                    sg.popup_error('ID inválido')
                    continue
                try:
                    idv = int(id_s)
                except ValueError:
                    sg.popup_error('ID deve ser inteiro')
                    continue
                janela.close()
                return idv

    def mostra_tela_alteracao(self):
        layout_id = [[sg.Text('ID da venda que deseja alterar:'), sg.Input(key='id')], [sg.Button('Buscar'), sg.Button('Voltar')]]
        janela_id = sg.Window('Buscar Venda', layout_id)
        while True:
            evento, valores = janela_id.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela_id.close()
                return None
            if evento == 'Buscar':
                id_s = valores.get('id','').strip()
                if not id_s:
                    sg.popup_error('ID inválido')
                    continue
                try:
                    id_venda = int(id_s)
                except ValueError:
                    sg.popup_error('ID deve ser inteiro')
                    continue
                if not self.__controlador.busca_venda_por_id(id_venda):
                    sg.popup_error('Não foi encontrada uma venda com este ID!')
                    continue
                janela_id.close()
                break

        layout = [
            [sg.Text('--- Alterar Venda ---', font=('Arial',14,'bold'))],
            [sg.Text('(Deixe em branco o que não quiser alterar)')],
            [sg.Text('Novo chassi:', size=(15,1)), sg.Input(key='chassi')],
            [sg.Text('Novo CPF cliente:', size=(15,1)), sg.Input(key='cpf_cliente')],
            [sg.Text('Novo valor:', size=(15,1)), sg.Input(key='valor')],
            [sg.Text('Nova data (dd/mm/aaaa):', size=(15,1)), sg.Input(key='data')],
            [sg.Button('Alterar'), sg.Button('Voltar')]
        ]

        janela = sg.Window('Alterar Venda', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela.close()
                return None
            if evento == 'Alterar':
                dados = {
                    'id': id_venda,
                    'chassi': valores.get('chassi','').strip() or ' ',
                    'cpf_cliente': valores.get('cpf_cliente','').strip() or ' ',
                    'valor': valores.get('valor','').strip() or ' ',
                    'data': valores.get('data','').strip() or ' '
                }
                janela.close()
                return dados

    def mostra_tela_busca_cliente(self):
        layout = [[sg.Text('CPF do cliente:'), sg.Input(key='cpf')], [sg.Button('Buscar'), sg.Button('Voltar')]]
        janela = sg.Window('Buscar Vendas por Cliente', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela.close()
                return None
            if evento == 'Buscar':
                cpf = valores.get('cpf','').strip()
                if not cpf:
                    sg.popup_error('CPF inválido')
                    continue
                janela.close()
                return cpf
