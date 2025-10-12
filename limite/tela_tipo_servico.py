from .telaAbstrata import TelaAbstrata


class TelaTipoServico(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print('----Controle de tipo de serviço iniciado!!!!----')

    def mostra_tela_cadastro(self):
        print('\n--- Cadastro tipo de serviço ---')
        while True:
            nome = input('Nome do tipo de serviço: ').strip()
            if nome:
                return nome
            
            self.mostra_mensagem_erro('O nome do tipo de serviço é obrigatório.')

    def mostra_tela_alteracao(self):
        print('\n--- Alterar tipo de serviço ---')
        while True:
            nome = input('Nome do tipo de serviço que deseja alterar: ').strip()
            novo_nome = input('Novo nome do tipo de serviço: ').strip()

            if nome and novo_nome:
                return nome, novo_nome
            
            self.mostra_mensagem_erro('Todos os campos devem ser preenchidos.')

    def mostra_tela_lista(self, lista_tipos_servico):
        print('\n--- Lista de tipos de serviço ---')
        for i in range(len(lista_tipos_servico)):
            print(f'Tipo de serviço {i+1}: {lista_tipos_servico[i].__str__()}')

    def mostra_tela_deletar(self):
        print('\n--- Deletar tipo de serviço ---')
        nome = input('Nome do tipo de serviço para deletar: ')
        return nome


    def mostra_tela_opcoes(self):
        print("Escolha o que você quer fazer:")
        print("1: Cadastrar")
        print("2: Listar")
        print("3: Alterar")
        print("4: Deletar")
        print("0: Voltar")

        opcao_escolhida = self.le_num_inteiro('Número desejado: ', [0, 1, 2, 3, 4, 5])

        return opcao_escolhida