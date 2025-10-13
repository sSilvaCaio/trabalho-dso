from .tela_abstrata import TelaAbstrata


class TelaTipoServico(TelaAbstrata):
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
        print('\n--- Cadastro tipo de serviço ---')
        print('\n(Deixe em branco para voltar)')
        while True:
            nome = input('Nome do tipo de serviço: ').strip()
            if nome:
                return nome
            
            return None

    def mostra_tela_alteracao(self):
        print('\n--- Alterar tipo de serviço ---')
        print('\n(Deixe em branco para voltar)')
        while True:
            nome = input('Nome do tipo de serviço que deseja alterar: ').strip()
            novo_nome = input('Novo nome do tipo de serviço: ').strip()

            if nome and novo_nome:
                return nome, novo_nome
            
            if not nome and not novo_nome:
                return None, None
            
            self.mostra_mensagem_erro('Para fazer a alteração, todos os campos devem ser preenchidos.')

    def mostra_tela_lista(self, lista_tipos_servico):
        print('\n--- Lista de tipos de serviço ---')
        for i in range(len(lista_tipos_servico)):
            print(f'Tipo de serviço {i+1}: {lista_tipos_servico[i].__str__()}')

    def mostra_tela_deletar(self):
        print('\n--- Deletar tipo de serviço ---')
        print('\n(Deixe em branco para voltar)')
        nome = input('Nome do tipo de serviço para deletar: ')
        if not nome:
            return None
        return nome

