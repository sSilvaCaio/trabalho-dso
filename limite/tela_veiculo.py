import FreeSimpleGUI as sg
from .tela_abstrata import TelaAbstrata


class TelaVeiculo(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Menu Veículos ---", font=("Arial", 14, "bold"))],
            [sg.Button("Cadastrar", size=(15, 2))],
            [sg.Button("Listar Cadastrados", size=(15, 2))],
            [sg.Button("Listar em Estoque", size=(15, 2))],
            [sg.Button("Alterar", size=(15, 2))],
            [sg.Button("Deletar", size=(15, 2))],
            [sg.Button("Voltar", size=(15, 2))],
        ]

        janela = sg.Window("Menu Veículos", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return 0

            if evento == "Cadastrar":
                janela.close()
                return 1
            elif evento == "Listar Cadastrados":
                janela.close()
                return 2
            elif evento == "Listar em Estoque":
                janela.close()
                return 3
            elif evento == "Alterar":
                janela.close()
                return 4
            elif evento == "Deletar":
                janela.close()
                return 5

    def mostra_tela_cadastro(self):
        layout = [
            [sg.Text("--- Cadastrar Veículo ---", font=("Arial", 14, "bold"))],
            [
                sg.Text("Chassi:", size=(20, 1)),
                sg.InputText(key="chassi", size=(20, 1)),
            ],
            [sg.Text("Ano:", size=(20, 1)), sg.InputText(key="ano", size=(20, 1))],
            [sg.Text("Cor:", size=(20, 1)), sg.InputText(key="cor", size=(20, 1))],
            [sg.Text("Placa:", size=(20, 1)), sg.InputText(key="placa", size=(20, 1))],
            [
                sg.Text("Potência:", size=(20, 1)),
                sg.InputText(key="potencia", size=(20, 1)),
            ],
            [
                sg.Text("Quilometragem:", size=(20, 1)),
                sg.InputText(key="quilometragem", size=(20, 1)),
            ],
            [sg.Text("Marca:", size=(20, 1)), sg.InputText(key="marca", size=(20, 1))],
            [sg.Button("Cadastrar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Cadastrar Veículo", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Cadastrar":
                dados_limpos, erros = self.valida_dados_veiculo_cadastro(valores)

                if erros:
                    mensagem_erro = "\n".join(
                        [f"{campo}: {erro}" for campo, erro in erros.items()]
                    )
                    sg.popup_error(f"Erros encontrados:\n\n{mensagem_erro}")
                    continue

                janela.close()
                return dados_limpos

    def mostra_tela_lista_cadastrados(self, lista_veiculos):
        if not lista_veiculos:
            sg.popup_error("Nenhum veículo cadastrado!")
            return

        veiculos_str = [
            f"Chassi: {v['chassi']} | Marca: {v['marca']} | Ano: {v['ano']} | Cor: {v['cor']} | Placa: {v['placa']} | Potência: {v['potencia']} | Km: {v['quilometragem']}"
            for v in lista_veiculos
        ]

        layout = [
            [
                sg.Text(
                    "--- Lista de Veículos Cadastrados ---", font=("Arial", 14, "bold")
                )
            ],
            [sg.Listbox(values=veiculos_str, size=(100, 12), key="lista")],
            [sg.Button("Fechar")],
        ]

        janela = sg.Window("Lista de Veículos Cadastrados", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                janela.close()
                break

    def mostra_tela_lista_em_estoque(self, lista_veiculos):
        if not lista_veiculos:
            sg.popup_error("Nenhum veículo em estoque!")
            return

        veiculos_str = [
            f"Chassi: {v['chassi']} | Marca: {v['marca']} | Ano: {v['ano']} | Cor: {v['cor']} | Placa: {v['placa']} | Potência: {v['potencia']} | Km: {v['quilometragem']}"
            for v in lista_veiculos
        ]

        layout = [
            [
                sg.Text(
                    "--- Lista de Veículos em Estoque ---", font=("Arial", 14, "bold")
                )
            ],
            [sg.Listbox(values=veiculos_str, size=(100, 12), key="lista")],
            [sg.Button("Fechar")],
        ]

        janela = sg.Window("Lista de Veículos em Estoque", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                janela.close()
                break

    def mostra_tela_deletar(self):
        layout = [
            [sg.Text("--- Deletar Veículo ---", font=("Arial", 14, "bold"))],
            [
                sg.Text("Chassi do veículo:", size=(20, 1)),
                sg.InputText(key="chassi", size=(20, 1)),
            ],
            [sg.Button("Deletar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Deletar Veículo", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Deletar":
                chassi_str = valores["chassi"].strip()

                if not chassi_str:
                    sg.popup_error("Chassi não pode estar vazio!")
                    continue

                try:
                    chassi = int(chassi_str)
                    janela.close()
                    return chassi
                except ValueError:
                    sg.popup_error("Chassi deve ser um número inteiro!")

    def mostra_tela_alteracao(self):
        layout = [
            [sg.Text("--- Alterar Veículo ---", font=("Arial", 14, "bold"))],
            [
                sg.Text(
                    "(Deixe em branco o que não quiser alterar)",
                    font=("Arial", 10, "italic"),
                )
            ],
            [
                sg.Text("Chassi do veículo:", size=(20, 1)),
                sg.InputText(key="chassi", size=(20, 1)),
            ],
            [sg.Text("Novo Ano:", size=(20, 1)), sg.InputText(key="ano", size=(20, 1))],
            [sg.Text("Nova Cor:", size=(20, 1)), sg.InputText(key="cor", size=(20, 1))],
            [
                sg.Text("Nova Placa:", size=(20, 1)),
                sg.InputText(key="placa", size=(20, 1)),
            ],
            [
                sg.Text("Nova Potência:", size=(20, 1)),
                sg.InputText(key="potencia", size=(20, 1)),
            ],
            [
                sg.Text("Nova Quilometragem:", size=(20, 1)),
                sg.InputText(key="quilometragem", size=(20, 1)),
            ],
            [
                sg.Text("Nova Marca:", size=(20, 1)),
                sg.InputText(key="marca", size=(20, 1)),
            ],
            [sg.Button("Alterar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Alterar Veículo", layout)

        while True:
            evento, valores = janela.read()

            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None

            if evento == "Alterar":

                dados = {
                    "chassi": valores["chassi"].strip(),
                    "ano": valores["ano"].strip() or " ",
                    "cor": valores["cor"].strip() or " ",
                    "placa": valores["placa"].strip() or " ",
                    "potencia": valores["potencia"].strip() or " ",
                    "quilometragem": valores["quilometragem"].strip() or " ",
                    "marca": valores["marca"].strip() or " ",
                }

                dados_limpos, erros = self.valida_dados_veiculo_alteracao(dados)

                if erros:
                    mensagem_erro = "\n".join(
                        [f"{campo}: {erro}" for campo, erro in erros.items()]
                    )
                    sg.popup_error(f"Erros encontrados:\n\n{mensagem_erro}")
                    continue

                janela.close()
                return dados_limpos

    def valida_dados_veiculo_cadastro(self, dados_str: dict):
        """Valida cadastro - todos os campos obrigatórios"""
        dados_limpos = {}
        erros = {}

        self.valida_e_converte_int(
            dados_str, "chassi", erros, dados_limpos, min_val=1, obrigatorio=True
        )
        self.valida_e_converte_int(
            dados_str,
            "ano",
            erros,
            dados_limpos,
            min_val=1884,
            max_val=2026,
            obrigatorio=True,
        )

        if not dados_str["cor"]:
            erros["cor"] = "A cor é obrigatória"
        else:
            dados_limpos["cor"] = dados_str["cor"]

        if not dados_str["placa"]:
            erros["placa"] = "A placa é obrigatória"
        else:
            dados_limpos["placa"] = dados_str["placa"]

        if not dados_str["potencia"]:
            erros["potencia"] = "A potência é obrigatória"
        else:
            dados_limpos["potencia"] = dados_str["potencia"]

        self.valida_e_converte_int(
            dados_str, "quilometragem", erros, dados_limpos, min_val=0, obrigatorio=True
        )

        if not dados_str["marca"]:
            erros["marca"] = "A marca é obrigatória"
        else:
            dados_limpos["marca"] = dados_str["marca"]

        if erros:
            return None, erros

        return dados_limpos, None

    def valida_dados_veiculo_alteracao(self, dados_str: dict):
        """Valida alteração - campos podem ser vazios (não altera)"""
        dados_limpos = {}
        erros = {}

        self.valida_e_converte_int(
            dados_str, "chassi", erros, dados_limpos, min_val=1, obrigatorio=True
        )
        self.valida_e_converte_int(
            dados_str,
            "ano",
            erros,
            dados_limpos,
            min_val=1884,
            max_val=2026,
            obrigatorio=False,
        )
        self.valida_e_converte_int(
            dados_str,
            "quilometragem",
            erros,
            dados_limpos,
            min_val=0,
            obrigatorio=False,
        )

        # Campos texto podem ficar vazios
        dados_limpos["cor"] = dados_str["cor"].strip() or None
        dados_limpos["placa"] = dados_str["placa"].strip() or None
        dados_limpos["potencia"] = dados_str["potencia"].strip() or None
        dados_limpos["marca"] = dados_str["marca"].strip() or None

        if erros:
            return None, erros

        return dados_limpos, None

    def valida_e_converte_int(
        self,
        dados_str: dict,
        nome_campo: str,
        erros: dict,
        dados_limpos: dict,
        min_val=None,
        max_val=None,
        obrigatorio=True,  # ← Parâmetro novo
    ):
        valor_str = dados_str[nome_campo].strip()

        if not valor_str:
            if obrigatorio:
                erros[nome_campo] = f"O campo '{nome_campo}' é obrigatório."
            else:
                dados_limpos[nome_campo] = (
                    None  # ← Retorna None se vazio e não obrigatório
                )
            return

        try:
            valor_int = int(valor_str)

            if min_val is not None and valor_int < min_val:
                erros[nome_campo] = f"Valor deve ser maior ou igual a {min_val}."
                return

            if max_val is not None and valor_int > max_val:
                erros[nome_campo] = f"Valor deve ser menor ou igual a {max_val}."
                return

            dados_limpos[nome_campo] = valor_int

        except ValueError:
            erros[nome_campo] = f"Deve ser um número inteiro."

    def mostra_mensagem_erro(self, mensagem):
        sg.popup_error(mensagem)

    def mostra_mensagem(self, mensagem):
        sg.popup_ok(mensagem)
