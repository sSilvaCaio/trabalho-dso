from telaAbstrata import TelaAbstrata


class TelaVeiculo(TelaAbstrata):
    def __init__(self):
        pass

    def valida_dados_veiculo(self, dados: dict):
        dados_erro = dict()
        if not isinstance(dados.chassi, int):
            dados_erro['dado'] = 'chassi'
            dados_erro['tipo'] = 'int'
        
        if not isinstance(dados.ano, int):
            dados_erro['dado'] = 'ano'
            dados_erro['tipo'] = 'int'
        
        if not isinstance(dados.cor, str):
            dados_erro['dado'] = 'cor'
            dados_erro['tipo'] = 'str'
        
        if not isinstance(dados.placa, str):
            dados_erro['dado'] = 'placa'
            dados_erro['tipo'] = 'str'
        
        if not isinstance(dados.potencia, str):
            dados_erro['dado'] = 'potencia'
            dados_erro['tipo'] = 'str'
        
        if not isinstance(dados.quilometragem, int):
            dados_erro['dado'] = 'quilometragem'
            dados_erro['tipo'] = 'int'
        
        if not isinstance(dados.marca, str):
            dados_erro['dado'] = 'marca'
            dados_erro['tipo'] = 'str'
        
        if dados_erro['dado'] or dados_erro['tipo']:
            raise TypeError(dados_erro['dado'], dados_erro['tipo'])
        
        return True
    
    def mostra_tela_inicial(self):
        print("----Controle de veículo iniciado!!!!----")

    def mostra_tela_opcoes(self):
        pass