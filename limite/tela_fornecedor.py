from limite.tela_abstrata import TelaAbstrata

class TelaFornecedor(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
    
    def mostra_tela_opcoes(self):
        print("\nEscolha o que você quer fazer:")
        print("1: Cadastrar")
        print("2: Listar")
        print("3: Alterar")
        print("4: Deletar")
        print("0: Voltar")
        return self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3, 4])
    
    def mostra_tela_cadastro(self):
        while True:
            print('\n--- Cadastrar fornecedor ---')
            print('\n(Deixe o CNPJ em branco para voltar)')
            
            cnpj = input("CNPJ: ").strip()
            if not cnpj:
                return None
            
            if self.__controlador.busca_fornecedor_por_cnpj(cnpj):
                self.mostra_mensagem_erro("Já existe um fornecedor com este CNPJ!")
                continue
            
            dados = {
                'cnpj': cnpj,
                'nome': input('Nome: ').strip(),
                'telefone': input('Telefone: ').strip(),
                'idade': self.le_num_inteiro("Idade: "),
                'sexo': input('Sexo: ').strip(),
            }
            
            dados_limpos, erros = self.valida_dados_fornecedor(dados)
            if erros:
                for campo, erro in erros.items():
                    self.mostra_mensagem_erro(f'Erro no campo "{campo}": {erro}')
                continue
            
            return dados_limpos
    
    def mostra_tela_lista(self, lista_fornecedores):
        print('\n--- Lista de fornecedores ---')
        for fornecedor in lista_fornecedores:
            print(fornecedor.__str__())
    
    def mostra_tela_deletar(self):
        print('\n--- Deletar fornecedor ---')
        print('\n(Deixe em branco para voltar)')
        cnpj_fornecedor_para_deletar = input('CNPJ do fornecedor que deseja deletar: ').strip()
        return cnpj_fornecedor_para_deletar if cnpj_fornecedor_para_deletar else None
    
    def mostra_tela_alteracao(self):
        print('\n--- Alterar fornecedor ---')
        print('\n(Deixe o CNPJ em branco para voltar)')
        
        while True:
            cnpj = input('CNPJ do fornecedor que deseja alterar: ').strip()
            if not cnpj:
                return None
            
            if not self.__controlador.busca_fornecedor_por_cnpj(cnpj):
                self.mostra_mensagem_erro("Não foi encontrado um fornecedor com este CNPJ!")
                continue
            
            while True:
                print('\n(Deixe o valor em branco caso não queira alterar)')
                dados = {
                    'cnpj': cnpj,
                    'nome': input('Nome: ').strip() or ' ',
                    'telefone': input('Telefone: ').strip() or ' ',
                    'idade': self.le_num_inteiro("Idade: ") or ' ',
                    'sexo': input('Sexo: ').strip() or ' ',
                }
                
                dados_limpos, erros = self.valida_dados_fornecedor(dados)
                if erros:
                    for campo, erro in erros.items():
                        self.mostra_mensagem_erro(f'Erro no campo "{campo}": {erro}')
                    continue
                
                return dados_limpos
    
    def valida_dados_fornecedor(self, dados_str: dict):
        dados_limpos = {}
        erros = {}
        
        if not dados_str['cnpj']:
            erros['cnpj'] = "O CNPJ é obrigatório"
        dados_limpos['cnpj'] = dados_str['cnpj']
        
        if not dados_str['nome'] and dados_str['nome'] != ' ':
            erros['nome'] = "O nome é obrigatório"
        dados_limpos['nome'] = dados_str['nome']
        
        if not dados_str['telefone'] and dados_str['telefone'] != ' ':
            erros['telefone'] = "O telefone é obrigatório"
        dados_limpos['telefone'] = dados_str['telefone']
        
        self.valida_e_converte_dados_int_fornecedor(dados_str, 'idade', erros, dados_limpos)
        
        if not dados_str['sexo'] and dados_str['sexo'] != ' ':
            erros['sexo'] = "O sexo é obrigatório"
        dados_limpos['sexo'] = dados_str['sexo']
        
        if erros:
            return None, erros
        
        return dados_limpos, None
    
    def valida_e_converte_dados_int_fornecedor(self, dados_str: dict, nome_campo: str, erros: dict, dados_limpos: dict):
        valor_str = dados_str[nome_campo]
        
        if valor_str == ' ':
            dados_limpos[nome_campo] = valor_str
            return
        
        if valor_str is None:
            erros[nome_campo] = f"O campo '{nome_campo}' é obrigatório."
            return
        
        try:
            valor_int = int(valor_str)
            if nome_campo == 'idade' and not (0 < valor_int < 150):
                erros[nome_campo] = 'A idade deve estar entre 1 e 149.'
            dados_limpos[nome_campo] = valor_int
        except ValueError:
            erros[nome_campo] = f'O valor "{valor_str}" não é válido. Insira um número inteiro'
