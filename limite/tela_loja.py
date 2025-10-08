from telaAbstrata import TelaAbstrata


class TelaLoja(TelaAbstrata):
    def __init__(self, controlador_loja):
        self.__controlador_loja = controlador_loja
    
    def mostra_tela_inicial(self):
        print("----Controle de loja iniciado!!!!----")
    
    def mostra_tela_opcoes(self):
        print("\n" + "="*50)
        print("SISTEMA DE GERENCIAMENTO DE LOJAS")
        print("="*50)
        print("1 - Cadastrar Loja")
        print("2 - Listar Lojas")
        print("3 - Alterar Loja")
        print("4 - Deletar Loja")
        print("5 - Informações da Loja")
        print("6 - Veículos em Estoque")
        print("0 - Retornar")
        print("="*50)
        
        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            print("ERRO: Digite um número válido!")
            return -1
    
    def mostra_tela_cadastro(self):
        print("\n--- CADASTRO DE LOJA ---")
        nome = input("Nome: ")
        cnpj = input("CNPJ: ")
        endereco = input("Endereço: ")
        
        return {
            "nome": nome,
            "cnpj": cnpj,
            "endereco": endereco
        }
    
    def mostra_tela_alteracao(self):
        print("\n--- ALTERAÇÃO DE LOJA ---")
        print("(Deixe em branco para não alterar)")
        nome = input("Novo nome: ")
        cnpj = input("Novo CNPJ: ")
        endereco = input("Novo endereço: ")
        
        return {
            "nome": nome if nome else None,
            "cnpj": cnpj if cnpj else None,
            "endereco": endereco if endereco else None
        }
    
    def seleciona_loja(self):
        print("\n--- SELEÇÃO DE LOJA ---")
        cnpj = input("Digite o CNPJ da loja: ")
        return cnpj
    
    def mostra_dados_loja(self, dados_loja):
        print("\n" + "-"*50)
        print(f"Nome: {dados_loja['nome']}")
        print(f"CNPJ: {dados_loja['cnpj']}")
        print(f"Endereço: {dados_loja['endereco']}")
        print(f"Veículos em estoque: {dados_loja['num_veiculos']}")
        print(f"Clientes: {dados_loja['num_clientes']}")
        print(f"Fornecedores: {dados_loja['num_fornecedores']}")
        print(f"Serviços prestados: {dados_loja['num_servicos']}")
        print("-"*50)
    
    def mostra_informacoes_completas(self, dados_loja):
        print("\n" + "="*50)
        print("INFORMAÇÕES COMPLETAS DA LOJA")
        print("="*50)
        print(f"Nome: {dados_loja['nome']}")
        print(f"CNPJ: {dados_loja['cnpj']}")
        print(f"Endereço: {dados_loja['endereco']}")
        print(f"\nEstatísticas:")
        print(f"  - Veículos em estoque: {dados_loja['num_veiculos']}")
        print(f"  - Clientes cadastrados: {dados_loja['num_clientes']}")
        print(f"  - Fornecedores cadastrados: {dados_loja['num_fornecedores']}")
        print(f"  - Serviços prestados: {dados_loja['num_servicos']}")
        print("="*50)
    
    def mostra_mensagem(self, mensagem):
        print(f"\n>>> {mensagem}")
    
    def mostra_mensagem_TypeError(self, mensagem):
        print(f"\n>>> ERRO DE TIPO: {mensagem}")
    
    def mostra_mensagem_Exception(self, mensagem):
        print(f"\n>>> ERRO: {mensagem}")
    
    def valida_dados_loja(self, dados: dict):
        dados_erro = dict()
        
        if not isinstance(dados['nome'], str) or not dados['nome']:
            dados_erro['dado'] = 'nome'
            dados_erro['tipo'] = 'str (não vazio)'
        
        if not isinstance(dados['cnpj'], str) or not dados['cnpj']:
            dados_erro['dado'] = 'cnpj'
            dados_erro['tipo'] = 'str (não vazio)'
        
        if not isinstance(dados['endereco'], str) or not dados['endereco']:
            dados_erro['dado'] = 'endereco'
            dados_erro['tipo'] = 'str (não vazio)'
        
        if dados_erro.get('dado') or dados_erro.get('tipo'):
            raise TypeError(dados_erro['dado'], dados_erro['tipo'])
        
        return True
