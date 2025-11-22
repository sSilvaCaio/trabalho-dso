from .tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaCliente(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Menu Clientes ---", font=("Arial", 14, "bold"))],
            [sg.Button("Cadastrar", size=(15, 2))],
            [sg.Button("Listar", size=(15, 2))],
            [sg.Button("Alterar", size=(15, 2))],
            [sg.Button("Deletar", size=(15, 2))],
            [sg.Button("Voltar", size=(15, 2))],
        ]

        janela = sg.Window("Menu Clientes", layout)

        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return 0
            if evento == "Cadastrar":
                janela.close()
                return 1
            if evento == "Listar":
                janela.close()
                return 2
            if evento == "Alterar":
                janela.close()
                return 3
            if evento == "Deletar":
                janela.close()
                return 4

    def mostra_tela_cadastro(self):
        layout = [
            [sg.Text("--- Cadastrar Cliente ---", font=("Arial", 14, "bold"))],
            [sg.Text("CPF:", size=(10, 1)), sg.Input(key="cpf", size=(20, 1))],
            [sg.Text("Nome:", size=(10, 1)), sg.Input(key="nome", size=(30, 1))],
            [sg.Text("Telefone:", size=(10, 1)), sg.Input(key="telefone", size=(20, 1))],
            [sg.Text("Idade:", size=(10, 1)), sg.Input(key="idade", size=(10, 1))],
            [sg.Text("Sexo:", size=(10, 1)), sg.Input(key="sexo", size=(10, 1))],
            [sg.Button("Cadastrar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Cadastrar Cliente", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None
            if evento == "Cadastrar":
                dados_limpos, erros = self.valida_dados_cliente(valores)
                if erros:
                    mensagem_erro = "\n".join([f"{campo}: {erro}" for campo, erro in erros.items()])
                    sg.popup_error(f"Erros encontrados:\n\n{mensagem_erro}")
                    continue
                janela.close()
                return dados_limpos

    def mostra_tela_lista(self, lista_clientes):
        if not lista_clientes:
            sg.popup_error("Nenhum cliente cadastrado!")
            return

        clientes_str = [c.__str__() for c in lista_clientes]
        layout = [[sg.Text("--- Lista de Clientes ---", font=("Arial", 14, "bold"))], [sg.Listbox(values=clientes_str, size=(80, 12), key="lista")], [sg.Button("Fechar")]]
        janela = sg.Window("Lista de Clientes", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Fechar":
                janela.close()
                break

    def mostra_tela_deletar(self):
        layout = [
            [sg.Text("--- Deletar Cliente ---", font=("Arial", 14, "bold"))],
            [sg.Text("CPF do cliente:", size=(15, 1)), sg.Input(key="cpf", size=(20, 1))],
            [sg.Button("Deletar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Deletar Cliente", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None
            if evento == "Deletar":
                cpf = valores["cpf"].strip()
                if not cpf:
                    sg.popup_error("CPF não pode estar vazio!")
                    continue
                janela.close()
                return cpf

    def mostra_tela_alteracao(self):
        layout_busca = [[sg.Text("CPF do cliente que deseja alterar:"), sg.Input(key="cpf")], [sg.Button("Buscar"), sg.Button("Voltar")]]
        janela_busca = sg.Window("Buscar Cliente", layout_busca)
        while True:
            evento, valores = janela_busca.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela_busca.close()
                return None
            if evento == "Buscar":
                cpf = valores["cpf"].strip()
                if not cpf:
                    sg.popup_error("CPF inválido")
                    continue
                if not self.__controlador.busca_cliente_por_cpf(cpf):
                    sg.popup_error("Não foi encontrado um cliente com este CPF!")
                    continue
                janela_busca.close()
                break

        layout = [
            [sg.Text("--- Alterar Cliente ---", font=("Arial", 14, "bold"))],
            [sg.Text("(Deixe em branco o que não quiser alterar)")],
            [sg.Text("Nome:", size=(10, 1)), sg.Input(key="nome")],
            [sg.Text("Telefone:", size=(10, 1)), sg.Input(key="telefone")],
            [sg.Text("Idade:", size=(10, 1)), sg.Input(key="idade")],
            [sg.Text("Sexo:", size=(10, 1)), sg.Input(key="sexo")],
            [sg.Button("Alterar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Alterar Cliente", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None
            if evento == "Alterar":
                dados = {
                    'cpf': cpf,
                    'nome': valores['nome'].strip() or ' ',
                    'telefone': valores['telefone'].strip() or ' ',
                    'idade': valores['idade'].strip() or ' ',
                    'sexo': valores['sexo'].strip() or ' ',
                }
                dados_limpos, erros = self.valida_dados_cliente(dados)
                if erros:
                    mensagem_erro = "\n".join([f"{campo}: {erro}" for campo, erro in erros.items()])
                    sg.popup_error(f"Erros encontrados:\n\n{mensagem_erro}")
                    continue
                janela.close()
                return dados_limpos

    def valida_dados_cliente(self, dados_str: dict):
        dados_limpos = {}
        erros = {}

        if not dados_str.get('cpf'):
            erros['cpf'] = "O CPF é obrigatório"
        dados_limpos['cpf'] = dados_str.get('cpf')

        if not dados_str.get('nome') and dados_str.get('nome') != ' ':
            erros['nome'] = "O nome é obrigatório"
        dados_limpos['nome'] = dados_str.get('nome')

        if not dados_str.get('telefone') and dados_str.get('telefone') != ' ':
            erros['telefone'] = "O telefone é obrigatório"
        dados_limpos['telefone'] = dados_str.get('telefone')

        self.valida_e_converte_dados_int_cliente(dados_str, 'idade', erros, dados_limpos)

        if not dados_str.get('sexo') and dados_str.get('sexo') != ' ':
            erros['sexo'] = "O sexo é obrigatório"
        dados_limpos['sexo'] = dados_str.get('sexo')

        if erros:
            return None, erros

        return dados_limpos, None

    def valida_e_converte_dados_int_cliente(self, dados_str: dict, nome_campo: str, erros: dict, dados_limpos: dict):
        valor_str = dados_str.get(nome_campo)

        if valor_str == ' ':
            dados_limpos[nome_campo] = valor_str
            return

        if valor_str is None or valor_str == '':
            erros[nome_campo] = f"O campo '{nome_campo}' é obrigatório."
            return

        try:
            valor_int = int(valor_str)
            if nome_campo == 'idade' and not (0 < valor_int < 150):
                erros[nome_campo] = 'A idade deve estar entre 1 e 149.'
            dados_limpos[nome_campo] = valor_int
        except ValueError:
            erros[nome_campo] = f'O valor "{valor_str}" não é válido. Insira um número inteiro'
