import FreeSimpleGUI as sg
from .tela_abstrata import TelaAbstrata


class TelaMarca(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_cadastro(self):
        layout = [
            [sg.Text("--- Cadastro Marca ---", font=("Arial", 14, "bold"))],
            [
                sg.Text("Nome da marca:", size=(20, 1)),
                sg.InputText(key="nome", size=(20, 1)),
            ],
            [sg.Button("Cadastrar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Cadastro Marca", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Cadastrar":
                nome = valores["nome"].strip()
                if nome:
                    janela.close()
                    return nome
                else:
                    sg.popup_error("Nome não pode estar vazio!")

    def mostra_tela_alteracao(self):

        layout = [
            [sg.Text("--- Alterar Marca ---", font=("Arial", 14, "bold"))],
            [
                sg.Text("Nome da marca a alterar:", size=(25, 1)),
                sg.InputText(key="nome_atual", size=(20, 1)),
            ],
            [
                sg.Text("Novo nome da marca:", size=(25, 1)),
                sg.InputText(key="novo_nome", size=(20, 1)),
            ],
            [sg.Button("Alterar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Alterar Marca", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None, None

            if evento == "Alterar":
                nome = valores["nome_atual"].strip()
                novo_nome = valores["novo_nome"].strip()

                if nome and novo_nome:
                    janela.close()
                    return nome, novo_nome
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")

    def mostra_tela_lista(self, lista_marcas):
        if not lista_marcas:
            sg.popup_info("Nenhuma marca cadastrada!")
            return

        # Converte lista de dicionários em strings para exibição
        marcas_str = [
            f"ID: {marca['id']} - Nome: {marca['nome']}" for marca in lista_marcas
        ]

        layout = [
            [sg.Text("--- Lista de Marcas ---", font=("Arial", 14, "bold"))],
            [sg.Listbox(values=marcas_str, size=(40, 10), key="lista")],
            [sg.Button("Fechar")],
        ]

        janela = sg.Window("Lista de Marcas", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                janela.close()
                break

    def mostra_tela_deletar(self):
        layout = [
            [sg.Text("--- Deletar Marca ---", font=("Arial", 14, "bold"))],
            [
                sg.Text("Nome da marca para deletar:", size=(25, 1)),
                sg.InputText(key="nome", size=(20, 1)),
            ],
            [sg.Button("Deletar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Deletar Marca", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Deletar":
                nome = valores["nome"].strip()
                if nome:
                    janela.close()
                    return nome
                else:
                    sg.popup_error("Nome não pode estar vazio!")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Menu Marcas ---", font=("Arial", 14, "bold"))],
            [sg.Button("Cadastrar", size=(15, 2))],
            [sg.Button("Listar", size=(15, 2))],
            [sg.Button("Alterar", size=(15, 2))],
            [sg.Button("Deletar", size=(15, 2))],
            [sg.Button("Voltar", size=(15, 2))],
        ]

        janela = sg.Window("Menu Marcas", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return 0

            if evento == "Cadastrar":
                janela.close()
                return 1
            elif evento == "Listar":
                janela.close()
                return 2
            elif evento == "Alterar":
                janela.close()
                return 3
            elif evento == "Deletar":
                janela.close()
                return 4

    def mostra_mensagem_erro(self, mensagem):
        sg.popup_error(mensagem)

    def mostra_mensagem(self, mensagem):
        sg.popup_ok(mensagem)
