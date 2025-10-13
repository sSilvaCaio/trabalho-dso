from .tela_abstrata import TelaAbstrata
from datetime import datetime, date


class TelaServico(TelaAbstrata):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    def mostra_tela_opcoes(self):
        print("\n---- MÓDULO DE SERVIÇOS ----")
        print("1 - Registrar Novo Serviço")
        print("2 - Listar Todos os Serviços")
        print("3 - Alterar Serviço Existente")
        print("4 - Excluir Serviço")
        print("0 - Retornar ao Menu Principal")
        return self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3, 4])

    def mostra_tela_cadastro(self):
        print("\n---- Cadastrar serviço ----")
        print('\n(Deixe o Tipo de Serviço em branco para voltar)')
        while True:

            tipo_servico = input("Nome do Tipo de Serviço: ").strip()

            if not tipo_servico.strip():
                return None

            chassi_veiculo = self.le_num_inteiro("Chassi do veículo: ")
        
            try:
                valor = float(input("Valor do serviço (ex: 250.50): "))
            except ValueError:
                self.mostra_mensagem_erro("Valor inválido. Use '.' como separador decimal.")
                continue

            data_str = input("Data do serviço (dd/mm/aaaa): ").strip()
            try:
                data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
            except ValueError:
                self.mostra_mensagem_erro(f"A data '{data_str}' não está no formato esperado 'dd/mm/aaaa'.")
                continue

            return {
                "tipo_servico": tipo_servico,
                "chassi_veiculo": chassi_veiculo,
                "valor": valor,
                "data": data_obj
            }
        
    def mostra_tela_lista(self, lista_servicos):
        print('\n--- Lista de serviços ---')
        for servico in lista_servicos:
            print(servico.__str__())

    def mostra_tela_alteracao(self):
        print('\n--- Alterar serviço ---')
        print('\n(Deixe o ID em branco para voltar)')

        while True:
            id = self.le_num_inteiro('ID do serviço que deseja alterar: ')
            if not id:
                return None
            
            tipo_servico = input("Novo Tipo de Serviço: ").strip() or ' '

            chassi_veiculo = self.le_num_inteiro("Chassi do veículo: ") or ' '

            try:
                valor = float(input("Valor do serviço (ex: 250.50): ")) or ' '
            except ValueError:
                self.mostra_mensagem_erro("Valor inválido. Use '.' como separador decimal.")
                continue

            data_str = input("Data do serviço (dd/mm/aaaa): ").strip()
            if not data_str.strip():
                data_obj = ' '
            try:
                data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
            except ValueError:
                self.mostra_mensagem_erro(f"A data '{data_str}' não está no formato esperado 'dd/mm/aaaa'.")
                continue

            dados = {
                'id': id,
                'tipo_servico': tipo_servico,
                'chassi_veiculo': chassi_veiculo,
                'valor': valor,
                'data': data_obj,
            }

            return dados
        
    def mostra_tela_deletar(self):
        print('\n--- Deletar serviço ---')
        print('\n(Deixe em branco para voltar)')
        id_servico_para_deletar = self.le_num_inteiro('ID do serviço que deseja deletar: ')
        return id_servico_para_deletar