from entidade.veiculo import Veiculo
from limite.tela_veiculo import TelaVeiculo


class ControladorVeiculo:
    def __init__(self, controlador_principal):
        self.__tela = TelaVeiculo(self)
        self.__controlador_principal = controlador_principal
    
    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {1: self.cadastra_veiculo, 2: self.lista_veiculos_cadastrados, 3: self.lista_veiculos_em_estoque, 4: self.altera_veiculo, 5: self.deleta_veiculo}
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")

    def cadastra_veiculo(self):
        while True:
            dados_veiculo = self.tela.mostra_tela_cadastro()

            if not dados_veiculo: return None

            if self.busca_veiculo_por_chassi(dados_veiculo['chassi']):
                self.tela.mostra_mensagem_erro("Já existe um veículo com este chassi!")
                continue
            
            obj_marca = self.controlador_principal.controlador_marca.busca_marca_por_nome(dados_veiculo['marca'])
            if not obj_marca:
                (self.controlador_principal.controlador_marca.tela.
                 mostra_mensagem_erro(f'A marca "{dados_veiculo['marca']}" não foi encontrada.'))
                continue
            
            novo_veiculo = Veiculo(
                chassi=dados_veiculo["chassi"],
                ano=dados_veiculo["ano"],
                cor=dados_veiculo["cor"],
                placa=dados_veiculo["placa"],
                potencia=dados_veiculo["potencia"], 
                quilometragem=dados_veiculo["quilometragem"],
                marca=obj_marca,
            )
            self.controlador_principal.loja.veiculos_cadastrados.append(novo_veiculo)
            self.tela.mostra_mensagem("Veículo cadastrado.")
            return novo_veiculo

    def lista_veiculos_cadastrados(self):
        veiculos = self.controlador_principal.loja.veiculos_cadastrados

        if not veiculos:
            self.tela.mostra_mensagem("Nenhum veículo cadastrado.")
            return None
        
        self.tela.mostra_tela_lista_cadastrados(veiculos)

    def lista_veiculos_em_estoque(self):
        veiculos = self.controlador_principal.loja.veiculos_em_estoque

        if not veiculos:
            self.tela.mostra_mensagem("Nenhum veículo em estoque.")
            return None
        
        self.tela.mostra_tela_lista_em_estoque(veiculos)

    def deleta_veiculo(self):
        while True:
            chassi = self.tela.mostra_tela_deletar()

            if not chassi:
                return None
            
            veiculo = self.busca_veiculo_por_chassi(chassi)

            if not veiculo:
                self.tela.mostra_mensagem_erro("Não existe veículo com este chassi.")
                continue

            removido_com_sucesso = self.deleta_veiculo_por_objeto(veiculo)
            if removido_com_sucesso:
                self.tela.mostra_mensagem('Veículo deletado.')
                return True
            else:
                self.tela.mostra_mensagem_erro('Erro ao deletar veículo.')
                return False
            

    def altera_veiculo(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()
            if not novos_dados:
                return None
            
            veiculo = self.busca_veiculo_por_chassi(novos_dados['chassi'])
            if not veiculo:
                self.tela.mostra_mensagem_erro('Não existe veículo com este chassi.')
                continue
            
            obj_marca = self.controlador_principal.controlador_marca.busca_marca_por_nome(novos_dados['marca']) or ' '
            if not obj_marca:
                (self.controlador_principal.controlador_marca.tela.
                mostra_mensagem_erro(f'A marca "{novos_dados['marca']}" não foi encontrada.'))
                continue

            if novos_dados['ano'] != ' ': veiculo.ano = novos_dados["ano"]
            if novos_dados['cor'] != ' ': veiculo.cor = novos_dados["cor"]
            if novos_dados['placa'] != ' ': veiculo.placa = novos_dados["placa"]
            if novos_dados['potencia'] != ' ': veiculo.motor.potencia = novos_dados["potencia"]
            if novos_dados['quilometragem'] != ' ': veiculo.motor.quilometragem = novos_dados["quilometragem"]
            if novos_dados['marca'] != ' ': veiculo.marca = obj_marca

            self.tela.mostra_mensagem('Veículo alterado.')
            return veiculo

    def deleta_veiculo_por_objeto(self, veiculo_para_deletar: Veiculo):
        if veiculo_para_deletar and isinstance(veiculo_para_deletar, Veiculo):

            if veiculo_para_deletar in self.__controlador_principal.loja.veiculos_cadastrados:
                self.__controlador_principal.loja.veiculos_cadastrados.remove(veiculo_para_deletar)

            if veiculo_para_deletar in self.__controlador_principal.loja.veiculos_em_estoque:
                self.__controlador_principal.loja.veiculos_em_estoque.remove(veiculo_para_deletar)
            
            return True
        return False
        
    def busca_veiculo_por_chassi(self, chassi):
            for veiculo in self.controlador_principal.loja.veiculos_cadastrados:
                if veiculo.chassi == chassi:
                    return veiculo
            return None
    