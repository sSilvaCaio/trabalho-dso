from limite.tela_abstrata import TelaAbstrata

class TelaVenda(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
    
    def mostra_tela_opcoes(self):
        print("\nEscolha o que você quer fazer:")
        print("1: Registrar Venda")
        print("2: Listar Vendas")
        print("3: Alterar Venda")
        print("4: Deletar Venda")
        print("0: Voltar")
        return self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3, 4])
    
    def mostra_tela_cadastro(self):
        while True:
            print('\n--- Registrar venda ---')
            print('\n(Deixe o chassi em branco para voltar)')
            
            chassi = self.le_num_inteiro("Chassi do veículo: ")
            if not chassi:
                return None
            
            cpf_cliente = input("CPF do cliente: ").strip()
            if not cpf_cliente:
                return None
            
            valor = self.le_num_float("Valor da venda: ")
            if not valor:
                return None
            
            data = self.le_data("Data da venda (dd/mm/aaaa): ")
            if not data:
                return None
            
            dados = {
                'chassi': chassi,
                'cpf_cliente': cpf_cliente,
                'valor': valor,
                'data': data
            }
            
            return dados
    
    def mostra_tela_lista(self, lista_vendas):
        print('\n--- Lista de vendas ---')
        if not lista_vendas:
            self.mostra_mensagem("Nenhuma venda registrada.")
            return
        
        for i, venda in enumerate(lista_vendas):
            print(venda.__str__())
    
    def mostra_tela_deletar(self):
        print('\n--- Deletar venda ---')
        print('\n(Deixe em branco para voltar)')
        id_venda = self.le_num_inteiro('ID da venda que deseja deletar: ')
        return id_venda if id_venda else None
    
    def mostra_tela_alteracao(self):
        print('\n--- Alterar venda ---')
        print('\n(Deixe o ID em branco para voltar)')
        
        while True:
            id_venda = self.le_num_inteiro('ID da venda que deseja alterar: ')
            if not id_venda:
                return None
            
            if not self.__controlador.busca_venda_por_id(id_venda):
                self.mostra_mensagem_erro("Não foi encontrada uma venda com este ID!")
                continue
            
            while True:
                print('\n(Deixe o valor em branco caso não queira alterar)')
                chassi = self.le_num_inteiro("Novo chassi do veículo: ") or ' '
                cpf_cliente = input("Novo CPF do cliente: ").strip() or ' '
                valor = self.le_num_float("Novo valor da venda: ") or ' '
                data = self.le_data("Nova data da venda (dd/mm/aaaa): ") or ' '
                
                dados = {
                    'id': id_venda,
                    'chassi': chassi,
                    'cpf_cliente': cpf_cliente,
                    'valor': valor,
                    'data': data
                }
                
                return dados
    
    def mostra_tela_busca_cliente(self):
        print('\n--- Buscar vendas por cliente ---')
        print('\n(Deixe em branco para voltar)')
        cpf_cliente = input('CPF do cliente: ').strip()
        return cpf_cliente if cpf_cliente else None
    
    def le_num_float(self, mensagem: str):
        while True:
            try:
                entrada = input(mensagem).strip()
                if not entrada:
                    return None
                return float(entrada)
            except ValueError:
                self.mostra_mensagem_erro("Valor inválido. Digite um número decimal.")
