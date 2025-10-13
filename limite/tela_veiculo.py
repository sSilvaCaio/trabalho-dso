from limite.tela_abstrata import TelaAbstrata


class TelaVeiculo(TelaAbstrata):
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
        while True:
            print('\n--- Cadastrar veículo ---')
            print('\n(Deixe o chassi em branco para voltar)')
            print('\n(Deixe o valor em branco caso não queira alterar)')

            chassi = self.le_num_inteiro("Chassi: ")

            if not chassi:
                return None
            
            if self.__controlador.busca_veiculo_por_chassi(chassi):
                self.mostra_mensagem_erro("Já existe um veículo com este chassi!")
                continue
            
            dados = {
                'chassi': chassi,
                'ano': self.le_num_inteiro("Ano: "),
                'cor': input('Cor: ').strip(),
                'placa': input('Placa: ').strip(),
                'potencia': input('Potencia: ').strip(),
                'quilometragem': self.le_num_inteiro("Quilometragem: "),
                'marca': input('Marca: ').strip(),
            }

            dados_limpos, erros = self.valida_dados_veiculo(dados)

            if erros:
                for campo, erro in erros.items():
                    self.mostra_mensagem_erro(f'Erro no campo: "{campo}": {erro}')
                continue

            return dados_limpos

    def mostra_tela_lista(self, lista_veiculos):
        print('\n--- Lista de veículos ---')
        for veiculo in lista_veiculos:
            print(veiculo.__str__())
        
    def mostra_tela_deletar(self):
        print('\n--- Deletar veículo ---')
        print('\n(Deixe em branco para voltar)')
        chassi_veiculo_para_deletar = self.le_num_inteiro('Chassi do veículo que deseja deletar: ')
        return chassi_veiculo_para_deletar

    def mostra_tela_alteracao(self):
        print('\n--- Alterar veículo ---')
        print('\n(Deixe o chassi em branco para voltar)')
        while True:

            chassi = self.le_num_inteiro('Chassi do veículo que deseja alterar: ')

            if not chassi:
                return None
            
            if not self.__controlador.busca_veiculo_por_chassi(chassi):
                    self.mostra_mensagem_erro("Não foi encontrado um veículo com este chassi!")
                    continue
            
            while True:
                dados = {
                    'chassi': chassi,
                    'ano': self.le_num_inteiro("Ano: ") or ' ',
                    'cor': input('Cor: ') or ' ',
                    'placa': input('Placa: ') or ' ',
                    'potencia': input('Potencia: ') or ' ',
                    'quilometragem': self.le_num_inteiro("Quilometragem: ") or ' ',
                    'marca': input('Marca: ') or ' ',
                    }

                dados_limpos, erros = self.valida_dados_veiculo(dados)

                if erros:
                    for campo, erro in erros.items():
                        self.mostra_mensagem_erro(f'Erro no campo: "{campo}": {erro}')
                    continue

                return dados_limpos

    def valida_dados_veiculo(self, dados_str: dict):
        dados_limpos = {}
        erros = {}
        
        self.valida_e_converte_dados_int_veiculo(dados_str, 'chassi', erros, dados_limpos)
        self.valida_e_converte_dados_int_veiculo(dados_str, 'ano', erros, dados_limpos)

        if not dados_str['cor']:
            erros['cor'] = "A cor é obrigatória"
        dados_limpos['cor'] = dados_str['cor']

        if not dados_str['placa']:
            erros['placa'] = "A placa é obrigatória"
        dados_limpos['placa'] = dados_str['placa']

        if not dados_str['potencia']:
            erros['potencia'] = "A potência é obrigatória"
        dados_limpos['potencia'] = dados_str['potencia']

        self.valida_e_converte_dados_int_veiculo(dados_str, 'quilometragem', erros, dados_limpos)

        if not dados_str['marca']:
            erros['marca'] = "A marca é obrigatória"
        dados_limpos['marca'] = dados_str['marca']

        if erros:
            return None, erros
        
        return dados_limpos, None
    
    def valida_e_converte_dados_int_veiculo(self, dados_str: dict, nome_campo: str, erros: dict, dados_limpos: dict):
        valor_str = dados_str[nome_campo]
        
        if valor_str == ' ':
            dados_limpos[nome_campo] = valor_str
            return
        
        if valor_str is None:
            erros[nome_campo] = f"O campo '{nome_campo}' é obrigatório."
            return

        
        try:
            valor_int = int(valor_str)

            if nome_campo == 'chassi' and valor_int <= 0:
                erros[nome_campo] = f'O chassi inserido é inválido. Insira um número maior que 0.'

            if nome_campo == 'ano' and not (1884 <= valor_int <= 2026):
                erros[nome_campo] = f'O ano inserido é inválido. Insira um ano entre 1884 e 2025.'
            
            if nome_campo == 'quilometragem' and valor_int < 0:
                erros[nome_campo] = 'A quilometragem não pode ser negativa.'
            
            dados_limpos[nome_campo] = valor_int
        
        except ValueError:
            erros[nome_campo] = f'O valor "{valor_str}" não é válido. Insira um número inteiro'