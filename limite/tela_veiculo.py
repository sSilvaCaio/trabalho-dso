from telaAbstrata import TelaAbstrata
from controlador.controlador_veiculo import ControladorVeiculo


class TelaVeiculo(TelaAbstrata):
    def __init__(self, controlador: ControladorVeiculo):
        self.__controlador = controlador

    def valida_dados_veiculo(self, dados_str: dict):
        dados_limpos = {}
        erros = {}
        
        self.valida_e_converte_dados_int_veiculo(dados_str, 'chassi', erros, dados_limpos)
        self.valida_e_converte_dados_int_veiculo(dados_str, 'ano', erros, dados_limpos)

        if not dados_str['cor'].strip():
            erros['cor'] = "A cor é obrigatória"
        dados_limpos['cor'] = dados_str['cor']

        if not dados_str['placa'].strip():
            erros['placa'] = "A placa é obrigatória"
        dados_limpos['placa'] = dados_str['placa']

        if not dados_str['potencia'].strip():
            erros['potencia'] = "A potência é obrigatória"
        dados_limpos['potencia'] = dados_str['potencia']

        self.valida_e_converte_dados_int_veiculo(dados_str, 'quilometragem', erros, dados_limpos)

        if not dados_str['marca'].strip():
            erros['marca'] = "A marca é obrigatória"
        dados_limpos['marca'] = dados_str['marca']

        if erros:
            return None, erros
        
        return dados_limpos, None
    
    def valida_e_converte_dados_int_veiculo(self, dados_str: dict, nome_campo: str, erros: dict, dados_limpos: dict):
        valor_str = (dados_str[nome_campo] or '').strip()
        if not valor_str:
            erros[nome_campo] = f"O campo '{nome_campo}' é obrigatório."
            return
        
        try:
            valor_int = int(valor_str)
            if nome_campo == 'ano' and not (1884 <= valor_int <= 2026):
                erros[nome_campo] = f'O ano {nome_campo} é inválido.'
            
            if nome_campo == 'quilometragem' and valor_int < 0:
                erros[nome_campo] = 'A quilometragem não pode ser negativa.'
            
            dados_limpos[nome_campo] = valor_int
        
        except ValueError:
            erros[nome_campo] = f'O valor "{valor_str}" não é válido. Insira um número inteiro'
    
    def mostra_tela_inicial(self):
        print("----Controle de veículo iniciado!!!!----")
    
    def mostra_tela_cadastro(self):
        print('\n--- Cadastro de veículo ---')
        while True:
            dados = {
            'chassi': input('Chassi: '),
            'ano': input('Ano: '),
            'cor': input('Cor: '),
            'placa': input('Placa: '),
            'potencia': input('Potencia: '),
            'quilometragem': input('Quilometragem: '),
            'marca': input('Marca: '),
            }

            dados_limpos, erros = self.valida_dados_veiculo(dados)

            if erros:
                for campo, erro in erros.items():
                    self.mostra_mensagem_erro(f'Erro no campo: "{campo}": {erro}')
                continue

            return dados_limpos

    def mostra_tela_lista(self, lista_veiculos):
        print('\n--- Lista de veículos ---')
        for i in range(len(lista_veiculos)):
            print(f'Veículo {i+1}: {lista_veiculos[i].__str__()}')
        
    def mostra_tela_deletar(self):
        print('\n--- Deletar veículo ---')
        chassi_veiculo_para_deletar = self.le_num_inteiro('Chassi do veículo que deseja deletar: ')
        return chassi_veiculo_para_deletar

    def mostra_tela_alteracao(self):
        print('\n--- Alterar veículo ---')
        while True:
            dados = {
                'chassi': input('Chassi do veículo que deseja alterar: '),
                'ano': input('Ano: '),
                'cor': input('Cor: '),
                'placa': input('Placa: '),
                'potencia': input('Potencia: '),
                'quilometragem': input('Quilometragem: '),
                'marca': input('Marca: '),
                }

            dados_limpos, erros = self.valida_dados_veiculo(dados)

            if erros:
                for campo, erro in erros.items():
                    self.mostra_mensagem_erro(f'Erro no campo: "{campo}": {erro}')
                continue

            return dados_limpos

    def mostra_tela_opcoes(self):
        print("Escolha o que você quer fazer:")
        print("1: Cadastrar")
        print("2: Listar")
        print("3: Alterar")
        print("4: Deletar")
        print("0: Voltar")

        opcao_escolhida = self.le_num_inteiro('Número desejado: ', [0, 1, 2, 3, 4, 5])

        return opcao_escolhida