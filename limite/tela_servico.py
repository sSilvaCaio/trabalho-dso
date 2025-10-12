from .telaAbstrata import TelaAbstrata
from controlador.controlador_servico import ControladorServico
from datetime import datetime, date


class TelaServico(TelaAbstrata):
    def __init__(self, controlador: ControladorServico):
        self.__controlador = controlador

    def valida_dados_servico(self, dados_str: dict):
        dados_limpos = {}
        erros = {}
        
        if not dados_str['tipo_servico'].strip():
            erros['tipo_servico'] = "O tipo de serviço é obrigatório"
        dados_limpos['tipo_servico'] = dados_str['tipo_servico']

        if not dados_str['chassi_veiculo'].strip():
            erros['chassi_veiculo'] = "O chassi do veículo é obrigatório"
        dados_limpos['chassi_veiculo'] = dados_str['chassi_veiculo']

        if not dados_str['valor'].strip():
            erros['valor'] = "O valor é obrigatório"
        dados_limpos['valor'] = dados_str['valor']

        self.valida_e_converte_data(dados_str['data'], erros, dados_limpos)

        if erros:
            return None, erros
        
        return dados_limpos, None

    def valida_e_converte_data(self, data_str, erros, dados_limpos):
        if not data_str.strip():
            erros['data'] = 'A data é obrigatória'
            return None
        formato = "%d/%m/%Y"
        try:
            objeto_datetime = datetime.strptime(data_str, formato)

            objeto_data = objeto_datetime.date()

            return objeto_data
        except ValueError:
            self.mostra_mensagem_erro(f'A data "{data_str}" não está no formato esperado "dd/mm/aaaa".')
    
    def mostra_tela_inicial(self):
        print('----Controlador serviço iniciado!!!!----')

    def mostra_tela_cadastro(self):
        print('\n--- Cadastro de serviço ---')
        while True:
            dados = {
            'tipo_servico': input('Tipo de serviço: '),
            'chassi_veiculo': input('Chassi do veículo: '),
            'valor': input('Valor: '),
            'data': input('Data: '),
            }

            dados_limpos, erros = self.valida_dados_servico(dados)

            if erros:
                for campo, erro in erros.items():
                    self.mostra_mensagem_erro(f'Erro no campo: "{campo}": {erro}')
                continue

            return dados_limpos
        
    def mostra_tela_lista(self, lista_servicos):
        print('\n--- Lista de serviços ---')
        for servico in lista_servicos:
            print(servico.__str__())

    def mostra_tela_alteracao(self):
        print('\n--- Alterar serviço ---')
        while True:
            dados = {
                'id': input('ID do serviço que deseja alterar: '),
                'tipo_servico': input('Tipo de serviço: '),
                'chassi_veiculo': input('Chassi do veículo: '),
                'valor': input('Valor: '),
                'data': input('Data: '),
            }

            dados_limpos, erros = self.valida_dados_servico(dados)

            if erros:
                for campo, erro in erros.items():
                    self.mostra_mensagem_erro(f'Erro no campo: "{campo}": {erro}')
                continue

            return dados_limpos