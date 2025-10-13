from limite.tela_abstrata import TelaAbstrata

class TelaCompra(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador
    
    def mostra_tela_opcoes(self):
        print("\nEscolha o que você quer fazer:")
        print("1: Registrar Compra")
        print("2: Listar Compras")
        print("3: Alterar Compra")
        print("4: Deletar Compra")
        print("0: Voltar")
        return self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3, 4])
    
    def mostra_tela_cadastro(self):
        while True:
            print('\n--- Registrar compra ---')
            print('\n(Deixe o chassi em branco para voltar)')
            
            chassi = self.le_num_inteiro("Chassi do veículo: ")
            if not chassi:
                return None
            
            cnpj_fornecedor = input("CNPJ do fornecedor: ").strip()
            if not cnpj_fornecedor:
                return None
            
            valor = self.le_num_float("Valor da compra: ")
            if not valor:
                return None
            
            data = self.le_data("Data da compra (dd/mm/aaaa): ")
            if not data:
                return None
            
            dados = {
                'chassi': chassi,
                'cnpj_fornecedor': cnpj_fornecedor,
                'valor': valor,
                'data': data
            }
            
            return dados
    
    def mostra_tela_lista(self, lista_compras):
        print('\n--- Lista de compras ---')
        if not lista_compras:
            self.mostra_mensagem("Nenhuma compra registrada.")
            return
        
        for i, compra in enumerate(lista_compras):
            print(compra.__str__())
    
    def mostra_tela_deletar(self):
        print('\n--- Deletar compra ---')
        print('\n(Deixe em branco para voltar)')
        id_compra = self.le_num_inteiro('ID da compra que deseja deletar: ')
        return id_compra if id_compra else None
    
    def mostra_tela_alteracao(self):
        print('\n--- Alterar compra ---')
        print('\n(Deixe o ID em branco para voltar)')
        
        while True:
            id_compra = self.le_num_inteiro('ID da compra que deseja alterar: ')
            if not id_compra:
                return None
            
            if not self.__controlador.busca_compra_por_id(id_compra):
                self.mostra_mensagem_erro("Não foi encontrada uma compra com este ID!")
                continue
            
            while True:
                print('\n(Deixe o valor em branco caso não queira alterar)')
                chassi = self.le_num_inteiro("Novo chassi do veículo: ") or ' '
                cnpj_fornecedor = input("Novo CNPJ do fornecedor: ").strip() or ' '
                valor = self.le_num_float("Novo valor da compra: ") or ' '
                data = self.le_data("Nova data da compra (dd/mm/aaaa): ") or ' '
                
                dados = {
                    'id': id_compra,
                    'chassi': chassi,
                    'cnpj_fornecedor': cnpj_fornecedor,
                    'valor': valor,
                    'data': data
                }
                
                return dados
    
    def mostra_tela_busca_fornecedor(self):
        print('\n--- Buscar compras por fornecedor ---')
        print('\n(Deixe em branco para voltar)')
        cnpj_fornecedor = input('CNPJ do fornecedor: ').strip()
        return cnpj_fornecedor if cnpj_fornecedor else None
    
    def le_num_float(self, mensagem: str):
        while True:
            try:
                entrada = input(mensagem).strip()
                if not entrada:
                    return None
                return float(entrada)
            except ValueError:
                self.mostra_mensagem_erro("Valor inválido. Digite um número decimal.")
