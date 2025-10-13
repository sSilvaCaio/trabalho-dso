from limite.tela_abstrata import TelaAbstrata


class TelaPrincipal(TelaAbstrata):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print("----Sistema Iniciado!----")

    def mostra_tela_finalizar(self):
        print("----Sistema Finalizado!----")

    def mostra_tela_opcoes(self):
        print("\n" + "="*30)
        print("    LOJA DE VEÍCULOS    ")
        print("="*30)
        print("--- MÓDULOS PRINCIPAIS ---")
        print("1 - Gerenciar Veículos")
        print("2 - Gerenciar Clientes")
        print("3 - Gerenciar Fornecedores")
        print("--- MÓDULOS DE REGISTRO ---")
        print("4 - Gerenciar Vendas")
        print("5 - Gerenciar Compras")
        print("6 - Gerenciar Serviços")
        print("--- CADASTROS E RELATÓRIOS ---")
        print("7 - Gerenciar Marcas")
        print("8 - Gerenciar Tipos de Serviço")
        print("9 - Ver Relatórios")
        print("0 - Sair do Sistema")
        
        return self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])