import FreeSimpleGUI as sg
from .tela_abstrata import TelaAbstrata
from datetime import datetime, date


class TelaServico(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Menu Serviços ---", font=("Arial", 14, "bold"))],
            [sg.Button("Registrar", size=(15, 2))],
            [sg.Button("Listar", size=(15, 2))],
            [sg.Button("Alterar", size=(15, 2))],
            [sg.Button("Deletar", size=(15, 2))],
            [sg.Button("Voltar", size=(15, 2))],
        ]

        janela = sg.Window("Menu Serviços", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return 0

            if evento == "Registrar":
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

    def mostra_tela_cadastro(self):
        layout = [
            [sg.Text("--- Cadastrar Serviço ---", font=("Arial", 14, "bold"))],
            [
                sg.Text("Tipo de Serviço:", size=(20, 1)),
                sg.InputText(key="tipo_servico", size=(20, 1)),
            ],
            [
                sg.Text("Chassi do Veículo:", size=(20, 1)),
                sg.InputText(key="chassi_veiculo", size=(20, 1)),
            ],
            [
                sg.Text("Valor do Serviço:", size=(20, 1)),
                sg.InputText(key="valor", size=(20, 1)),
            ],
            [
                sg.Text("Data (dd/mm/aaaa):", size=(20, 1)),
                sg.InputText(key="data", size=(20, 1)),
            ],
            [sg.Button("Cadastrar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Cadastrar Serviço", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Cadastrar":
                tipo_servico = valores["tipo_servico"].strip()
                chassi_str = valores["chassi_veiculo"].strip()
                valor_str = valores["valor"].strip()
                data_str = valores["data"].strip()

                if not tipo_servico:
                    sg.popup_error("Tipo de serviço não pode estar vazio!")
                    continue

                try:
                    chassi_veiculo = int(chassi_str)
                except ValueError:
                    sg.popup_error("Chassi deve ser um número inteiro!")
                    continue

                try:
                    valor = float(valor_str)
                    if valor <= 0:
                        sg.popup_error("Valor deve ser maior que 0!")
                        continue
                except ValueError:
                    sg.popup_error('Valor inválido. Use "." como separador decimal!')
                    continue

                try:
                    data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
                except ValueError:
                    sg.popup_error("Data inválida. Use formato dd/mm/aaaa!")
                    continue

                janela.close()
                return {
                    "tipo_servico": tipo_servico,
                    "chassi_veiculo": chassi_veiculo,
                    "valor": valor,
                    "data": data_obj,
                }

    def mostra_tela_lista(self, lista_servicos):
        if not lista_servicos:
            sg.popup_error("Nenhum serviço cadastrado!")
            return

        servicos_str = [
            f"ID: {s['id']} | Tipo: {s['tipo_servico']} | Veículo: {s['veiculo']} | Valor: R$ {s['valor']:.2f} | Data: {s['data']}"
            for s in lista_servicos
        ]

        layout = [
            [sg.Text("--- Lista de Serviços ---", font=("Arial", 14, "bold"))],
            [sg.Listbox(values=servicos_str, size=(80, 12), key="lista")],
            [sg.Button("Fechar")],
        ]

        janela = sg.Window("Lista de Serviços", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                janela.close()
                break

    def mostra_tela_alteracao(self):
        layout = [
            [sg.Text("--- Alterar Serviço ---", font=("Arial", 14, "bold"))],
            [
                sg.Text(
                    "(Deixe em branco o que não quiser alterar)",
                    font=("Arial", 10, "italic"),
                )
            ],
            [
                sg.Text("ID do Serviço:", size=(20, 1)),
                sg.InputText(key="id", size=(20, 1)),
            ],
            [
                sg.Text("Novo Tipo de Serviço:", size=(20, 1)),
                sg.InputText(key="tipo_servico", size=(20, 1)),
            ],
            [
                sg.Text("Novo Chassi do Veículo:", size=(20, 1)),
                sg.InputText(key="chassi", size=(20, 1)),
            ],
            [
                sg.Text("Novo Valor:", size=(20, 1)),
                sg.InputText(key="valor", size=(20, 1)),
            ],
            [
                sg.Text("Nova Data (dd/mm/aaaa):", size=(20, 1)),
                sg.InputText(key="data", size=(20, 1)),
            ],
            [sg.Button("Alterar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Alterar Serviço", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Alterar":
                id_str = valores["id"].strip()

                if not id_str:
                    sg.popup_error("ID é obrigatório!")
                    continue

                try:
                    id_servico = int(id_str)
                except ValueError:
                    sg.popup_error("ID deve ser um número inteiro!")
                    continue

                tipo_servico = valores["tipo_servico"].strip() or " "
                chassi_str = valores["chassi"].strip()
                valor_str = valores["valor"].strip()
                data_str = valores["data"].strip()

                chassi = " "
                if chassi_str:
                    try:
                        chassi = int(chassi_str)
                    except ValueError:
                        sg.popup_error("Chassi deve ser um número inteiro!")
                        continue

                valor = " "
                if valor_str:
                    try:
                        valor = float(valor_str)
                        if valor <= 0:
                            sg.popup_error("Valor deve ser maior que 0!")
                            continue
                    except ValueError:
                        sg.popup_error(
                            'Valor inválido. Use "." como separador decimal!'
                        )
                        continue

                data = " "
                if data_str:
                    try:
                        data = datetime.strptime(data_str, "%d/%m/%Y").date()
                    except ValueError:
                        sg.popup_error("Data inválida. Use formato dd/mm/aaaa!")
                        continue

                janela.close()
                return {
                    "id": id_servico,
                    "tipo_servico": tipo_servico,
                    "chassi": chassi,
                    "valor": valor,
                    "data": data,
                }

    def mostra_tela_deletar(self):
        layout = [
            [sg.Text("--- Deletar Serviço ---", font=("Arial", 14, "bold"))],
            [
                sg.Text("ID do Serviço:", size=(20, 1)),
                sg.InputText(key="id", size=(20, 1)),
            ],
            [sg.Button("Deletar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Deletar Serviço", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Deletar":
                id_str = valores["id"].strip()

                if not id_str:
                    sg.popup_error("ID não pode estar vazio!")
                    continue

                try:
                    id_servico = int(id_str)
                    janela.close()
                    return id_servico
                except ValueError:
                    sg.popup_error("ID deve ser um número inteiro!")

    def mostra_mensagem_erro(self, mensagem):
        sg.popup_error(mensagem)

    def mostra_mensagem(self, mensagem):
        sg.popup_ok(mensagem)
