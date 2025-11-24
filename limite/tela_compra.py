from .tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg
from datetime import datetime


class TelaCompra(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Menu Compras ---", font=("Arial", 14, "bold"))],
            [sg.Button("Registrar Compra", size=(20, 2))],
            [sg.Button("Listar Compras", size=(20, 2))],
            [sg.Button("Alterar Compra", size=(20, 2))],
            [sg.Button("Deletar Compra", size=(20, 2))],
            [sg.Button("Voltar", size=(20, 2))],
        ]

        janela = sg.Window("Menu Compras", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return 0
            if evento == "Registrar Compra":
                janela.close()
                return 1
            if evento == "Listar Compras":
                janela.close()
                return 2
            if evento == "Alterar Compra":
                janela.close()
                return 3
            if evento == "Deletar Compra":
                janela.close()
                return 4

    def mostra_tela_cadastro(self):
        layout = [
            [sg.Text("--- Registrar Compra ---", font=("Arial", 14, "bold"))],
            [sg.Text("Chassi:", size=(15, 1)), sg.Input(key="chassi")],
            [sg.Text("CNPJ Fornecedor:", size=(15, 1)), sg.Input(key="cnpj_fornecedor")],
            [sg.Text("Valor:", size=(15, 1)), sg.Input(key="valor")],
            [sg.Text("Data (dd/mm/aaaa):", size=(15, 1)), sg.Input(key="data")],
            [sg.Button("Registrar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Registrar Compra", layout)
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

                cnpj = valores.get("cnpj_fornecedor", "").strip()
                if not cnpj:
                    sg.popup_error("CNPJ do fornecedor é obrigatório")
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
                
                try:
                    data_obj = datetime.strptime(data, "%d/%m/%Y")
                except ValueError:
                    sg.popup_error("Data inválida. Use o formato dd/mm/aaaa")
                    continue

                janela.close()
                return {"chassi": chassi, "cnpj_fornecedor": cnpj, "valor": valor, "data": data_obj}

    def mostra_tela_lista(self, lista_compras):
        if not lista_compras:
            sg.popup_ok("Nenhuma compra registrada.")
            return

        compras_str = [c.__str__() for c in lista_compras]
        layout = [[sg.Text("--- Lista de Compras ---", font=("Arial", 14, "bold"))], [sg.Listbox(values=compras_str, size=(90, 12), key="lista")], [sg.Button("Fechar")]]
        janela = sg.Window("Lista de Compras", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                janela.close()
                break

    def mostra_tela_deletar(self):
        layout = [[sg.Text("--- Deletar Compra ---", font=("Arial", 14, "bold"))], [sg.Text("ID da compra:", size=(15, 1)), sg.Input(key="id")], [sg.Button("Deletar"), sg.Button("Voltar")]]
        janela = sg.Window("Deletar Compra", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None
            if evento == "Deletar":
                id_s = valores.get("id", "").strip()
                if not id_s:
                    sg.popup_error("ID inválido")
                    continue
                try:
                    idc = int(id_s)
                except ValueError:
                    sg.popup_error("ID deve ser inteiro")
                    continue
                janela.close()
                return idc

    def mostra_tela_alteracao(self):
        layout_id = [[sg.Text('ID da compra que deseja alterar:'), sg.Input(key='id')], [sg.Button('Buscar'), sg.Button('Voltar')]]
        janela_id = sg.Window('Buscar Compra', layout_id)
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
                    id_compra = int(id_s)
                except ValueError:
                    sg.popup_error('ID deve ser inteiro')
                    continue
                if not self.__controlador.busca_compra_por_id(id_compra):
                    sg.popup_error('Não foi encontrada uma compra com este ID!')
                    continue
                janela_id.close()
                break

        layout = [
            [sg.Text('--- Alterar Compra ---', font=('Arial',14,'bold'))],
            [sg.Text('Novo chassi:', size=(15,1)), sg.Input(key='chassi')],
            [sg.Text('Novo CNPJ fornecedor:', size=(15,1)), sg.Input(key='cnpj_fornecedor')],
            [sg.Text('Novo valor:', size=(15,1)), sg.Input(key='valor')],
            [sg.Text('Nova data (dd/mm/aaaa):', size=(15,1)), sg.Input(key='data')],
            [sg.Button('Alterar'), sg.Button('Voltar')]
        ]

        janela = sg.Window('Alterar Compra', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela.close()
                return None
            if evento == 'Alterar':
                chassi_s = valores.get('chassi','').strip()
                chassi = ' '
                if chassi_s:
                    try:
                        chassi = int(chassi_s)
                    except ValueError:
                        sg.popup_error('Chassi deve ser número inteiro')
                        continue
                
                valor_s = valores.get('valor','').strip()
                valor = ' '
                if valor_s:
                    try:
                        valor = float(valor_s)
                    except ValueError:
                        sg.popup_error('Valor deve ser numérico')
                        continue
                
                data_s = valores.get('data','').strip()
                data = ' '
                if data_s:
                    try:
                        data = datetime.strptime(data_s, "%d/%m/%Y")
                    except ValueError:
                        sg.popup_error('Data inválida. Use o formato dd/mm/aaaa')
                        continue
                
                dados = {
                    'id': id_compra,
                    'chassi': chassi,
                    'cnpj_fornecedor': valores.get('cnpj_fornecedor','').strip() or ' ',
                    'valor': valor,
                    'data': data
                }
                janela.close()
                return dados

