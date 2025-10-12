from .telaAbstrata import TelaAbstrata


class TelaMarca(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print('----Controle de marca iniciado!!!!----')

    def mostra_tela_cadastro(self):
        print('\n--- Cadastro marca ---')
        while True:
            nome = input('Nome da marca: ').strip()
            if nome:
                return nome
            
            self.mostra_mensagem_erro('O nome da marca é obrigatório.')

    def mostra_tela_alteracao(self):
        print('\n--- Alterar marca ---')
        while True:
            nome = input('Nome da marca que deseja alterar: ').strip()
            novo_nome = input('Novo nome da marca: ').strip()

            if nome and novo_nome:
                return nome, novo_nome
            
            self.mostra_mensagem_erro('Todos os campos devem ser preenchidos.')

    def mostra_tela_lista(self, lista_marcas):
        print('\n--- Lista de marcas ---')
        for i in range(len(lista_marcas)):
            print(f'Marca {i+1}: {lista_marcas[i].__str__()}')

    def mostra_tela_deletar(self):
        print('\n--- Deletar marca ---')
        nome = input('Nome da marca para deletar: ')
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