from .tela_abstrata import TelaAbstrata
from datetime import datetime, date


class TelaServico(TelaAbstrata):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    def mostra_tela_opcoes(self):
        print("\n---- MÓDULO DE SERVIÇOS ----")
        print("1 - Registrar")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Deletar")
        print("0 - Voltar")
        return self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3, 4])

    def mostra_tela_cadastro(self):
        print("\n---- Cadastrar serviço ----")
        print('\n(Deixe o Tipo de Serviço em branco para voltar)')
        while True:

            tipo_servico = input("Nome do Tipo de Serviço: ").strip()

            if not tipo_servico.strip():
                return None

            chassi_veiculo = self.le_num_inteiro("Chassi do veículo: ")

            if not chassi_veiculo:
                self.mostra_mensagem_erro("Chassi do veículo é obrigatório.")
                continue
        
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
            print('---------------------')

    def mostra_tela_alteracao(self):
        print('\n--- Alterar serviço ---')
        print('\n(Deixe o ID em branco para voltar)')
        print('\n(Deixe em branco o que não quiser alterar)')

        while True:
            id = self.le_num_inteiro('ID do serviço que deseja alterar: ')

            if not id:
                return None
            
            tipo_servico = input("Novo Tipo de Serviço: ").strip() or ' '

            chassi_veiculo = self.le_num_inteiro("Chassi do veículo: ") or ' '
            

            try:
                valor_str = input("Valor do serviço (ex: 250.50): ")
                if not valor_str.strip():
                    valor = ' '
                else:
                    valor = float(valor_str)
                    if valor <= 0:
                        self.mostra_mensagem_erro("O valor do serviço deve ser maior que 0.")
                        continue
            except ValueError:
                self.mostra_mensagem_erro("Valor inválido. Use '.' como separador decimal.")
                continue

            data_str = input("Data do serviço (dd/mm/aaaa): ").strip()
            if not data_str.strip():
                data_obj = ' '
            else:
                try:
                    data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
                except ValueError:
                    self.mostra_mensagem_erro(f"A data '{data_str}' não está no formato esperado 'dd/mm/aaaa'.")
                    continue

            dados = {
                'id': id,
                'tipo_servico': tipo_servico,
                'chassi': chassi_veiculo,
                'valor': valor,
                'data': data_obj,
            }

            return dados
        
    def mostra_tela_deletar(self):
        print('\n--- Deletar serviço ---')
        print('\n(Deixe em branco para voltar)')
        id_servico_para_deletar = self.le_num_inteiro('ID do serviço que deseja deletar: ')
        return id_servico_para_deletar