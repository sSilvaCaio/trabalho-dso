from .tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaFornecedor(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
        sg.theme("DarkBlue3")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Menu Fornecedores ---", font=("Arial", 14, "bold"))],
            [sg.Button("Cadastrar", size=(15, 2))],
            [sg.Button("Listar", size=(15, 2))],
            [sg.Button("Alterar", size=(15, 2))],
            [sg.Button("Deletar", size=(15, 2))],
            [sg.Button("Voltar", size=(15, 2))],
        ]

        janela = sg.Window("Menu Fornecedores", layout)
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
            [sg.Text("--- Cadastrar Fornecedor ---", font=("Arial", 14, "bold"))],
            [sg.Text("CNPJ:", size=(12, 1)), sg.Input(key="cnpj")],
            [sg.Text("Nome:", size=(12, 1)), sg.Input(key="nome")],
            [sg.Text("Telefone:", size=(12, 1)), sg.Input(key="telefone")],
            [sg.Text("Idade:", size=(12, 1)), sg.Input(key="idade")],
            [sg.Text("Sexo:", size=(12, 1)), sg.Input(key="sexo")],
            [sg.Button("Cadastrar"), sg.Button("Voltar")],
        ]

        janela = sg.Window("Cadastrar Fornecedor", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return None
            if evento == "Cadastrar":
                dados_limpos, erros = self.valida_dados_fornecedor(valores)
                if erros:
                    mensagem_erro = "\n".join([f"{campo}: {erro}" for campo, erro in erros.items()])
                    sg.popup_error(f"Erros encontrados:\n\n{mensagem_erro}")
                    continue
                janela.close()
                return dados_limpos

    def mostra_tela_lista(self, lista_fornecedores):
        if not lista_fornecedores:
            sg.popup_ok("Nenhum fornecedor cadastrado.")
            return
        fornecedores_str = [f.__str__() for f in lista_fornecedores]
        layout = [[sg.Text("--- Lista de Fornecedores ---", font=("Arial",14,'bold'))], [sg.Listbox(values=fornecedores_str, size=(80,12), key='lista')], [sg.Button('Fechar')]]
        janela = sg.Window('Lista de Fornecedores', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Fechar':
                janela.close()
                break

    def mostra_tela_deletar(self):
        layout = [[sg.Text('--- Deletar Fornecedor ---', font=('Arial',14,'bold'))], [sg.Text('CNPJ:', size=(12,1)), sg.Input(key='cnpj')], [sg.Button('Deletar'), sg.Button('Voltar')]]
        janela = sg.Window('Deletar Fornecedor', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela.close()
                return None
            if evento == 'Deletar':
                cnpj = valores.get('cnpj','').strip()
                if not cnpj:
                    sg.popup_error('CNPJ inválido')
                    continue
                janela.close()
                return cnpj

    def mostra_tela_alteracao(self):
        layout_busca = [[sg.Text('CNPJ do fornecedor que deseja alterar:'), sg.Input(key='cnpj')], [sg.Button('Buscar'), sg.Button('Voltar')]]
        janela_busca = sg.Window('Buscar Fornecedor', layout_busca)
        while True:
            evento, valores = janela_busca.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela_busca.close()
                return None
            if evento == 'Buscar':
                cnpj = valores.get('cnpj','').strip()
                if not cnpj:
                    sg.popup_error('CNPJ inválido')
                    continue
                if not self.__controlador.busca_fornecedor_por_cnpj(cnpj):
                    sg.popup_error('Não foi encontrado um fornecedor com este CNPJ!')
                    continue
                janela_busca.close()
                break

        layout = [
            [sg.Text('--- Alterar Fornecedor ---', font=('Arial',14,'bold'))],
            [sg.Text('(Deixe em branco o que não quiser alterar)')],
            [sg.Text('Nome:', size=(12,1)), sg.Input(key='nome')],
            [sg.Text('Telefone:', size=(12,1)), sg.Input(key='telefone')],
            [sg.Text('Idade:', size=(12,1)), sg.Input(key='idade')],
            [sg.Text('Sexo:', size=(12,1)), sg.Input(key='sexo')],
            [sg.Button('Alterar'), sg.Button('Voltar')]
        ]

        janela = sg.Window('Alterar Fornecedor', layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
                janela.close()
                return None
            if evento == 'Alterar':
                dados = {
                    'cnpj': cnpj,
                    'nome': valores.get('nome','').strip() or ' ',
                    'telefone': valores.get('telefone','').strip() or ' ',
                    'idade': valores.get('idade','').strip() or ' ',
                    'sexo': valores.get('sexo','').strip() or ' ',
                }
                dados_limpos, erros = self.valida_dados_fornecedor(dados)
                if erros:
                    mensagem_erro = "\n".join([f"{campo}: {erro}" for campo, erro in erros.items()])
                    sg.popup_error(f"Erros encontrados:\n\n{mensagem_erro}")
                    continue
                janela.close()
                return dados_limpos

    def valida_dados_fornecedor(self, dados_str: dict):
        dados_limpos = {}
        erros = {}

        if not dados_str.get('cnpj'):
            erros['cnpj'] = "O CNPJ é obrigatório"
        dados_limpos['cnpj'] = dados_str.get('cnpj')

        if not dados_str.get('nome') and dados_str.get('nome') != ' ':
            erros['nome'] = "O nome é obrigatório"
        dados_limpos['nome'] = dados_str.get('nome')

        if not dados_str.get('telefone') and dados_str.get('telefone') != ' ':
            erros['telefone'] = "O telefone é obrigatório"
        dados_limpos['telefone'] = dados_str.get('telefone')

        valor_idade = dados_str.get('idade')
        if valor_idade == ' ':
            dados_limpos['idade'] = valor_idade
        elif valor_idade is None or valor_idade == '':
            erros['idade'] = "O campo 'idade' é obrigatório."
        else:
            try:
                vi = int(valor_idade)
                if not (0 < vi < 150):
                    erros['idade'] = 'A idade deve estar entre 1 e 149.'
                dados_limpos['idade'] = vi
            except ValueError:
                erros['idade'] = f'O valor "{valor_idade}" não é válido. Insira um número inteiro'

        if not dados_str.get('sexo') and dados_str.get('sexo') != ' ':
            erros['sexo'] = "O sexo é obrigatório"
        dados_limpos['sexo'] = dados_str.get('sexo')

        if erros:
            return None, erros
        return dados_limpos, None
