from limite.tela_servico import TelaServico
from entidade.servico import Servico


class ControladorServico():
    def __init__(self, controlador_principal):
        self.__tela = TelaServico(self)
        self.__controlador_principal = controlador_principal

    @property
    def tela(self):
        return self.__tela
    
    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {
            1: self.cadastra_servico,
            2: self.lista_servicos,
            3: self.altera_servico,
            4: self.deleta_servico,
        }
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")
    
    def cadastra_servico(self):
        while True:
            dados_servico = self.tela.mostra_tela_cadastro()

            if not dados_servico:
                return None

            veiculo = (self.controlador_principal.controlador_veiculo.
                    busca_veiculo_por_chassi(dados_servico['chassi_veiculo']))
            
            if not veiculo:
                (self.controlador_principal.controlador_veiculo.tela.
                mostra_mensagem_erro('Não foi encontrado veículo com este chassi'))
                continue

            tipo_servico = (self.controlador_principal.controlador_tipo_servico.
                            busca_tipo_servico_por_nome(dados_servico['tipo_servico']))
            
            if not tipo_servico:
                (self.controlador_principal.controlador_tipo_servico.tela.
                mostra_mensagem_erro('Não existe tipo de serviço cadastrado com este nome'))
                continue
            
            if self.busca_servico_por_atributos(tipo_servico, veiculo, dados_servico['valor'], dados_servico['data']):
                self.tela.mostra_mensagem_erro('Já existe serviço cadastrado com esses dados')
                continue

            novo_servico = Servico(tipo_servico, veiculo, dados_servico['valor'], dados_servico['data'])
            self.tela.mostra_mensagem_sucesso('Serviço registrado')
            self.controlador_principal.loja.servicos_prestados.append(novo_servico)
            return novo_servico


    def lista_servicos(self):
        self.tela.mostra_tela_lista(self.__servicos)

    def altera_servico(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()

            if not novos_dados:
                return None

            servico = self.busca_servico_por_id(novos_dados['id'])

            if not servico:
                self.tela.mostra_mensagem_erro('Não existe serviço cadastrado com este ID')
                continue

            tipo_servico = (self.controlador_principal.controlador_tipo_servico.
                            busca_tipo_servico_por_nome(novos_dados['tipo_servico']))
            
            if not tipo_servico:
                (self.controlador_principal.controlador_tipo_servico.tela.
                mostra_mensagem_erro('Não existe tipo de serviço cadastrado com este nome'))
                continue

            veiculo = self.controlador_principal.controlador_veiculo.busca_veiculo_por_chassi(novos_dados['chassi'])

            if not veiculo:
                (self.controlador_principal.controlador_veiculo.tela.
                mostra_mensagem_erro('Não existe veículo com este chassi.'))
                continue
            
            if self.busca_servico_por_atributos(tipo_servico, veiculo, novos_dados['valor'], novos_dados['data']):
                self.tela.mostra_mensagem_erro('Já existe serviço cadastrado com esses dados')
                continue
            
            if tipo_servico:
                servico.tipo_servico = tipo_servico
            if veiculo:
                servico.veiculo = veiculo
            if novos_dados['valor']:
                servico.valor = novos_dados["valor"]
            if novos_dados['data']:
                servico.data = novos_dados["data"]

            self.tela.mostra_mensagem('Serviço alterado.')
            return servico

    
    def deleta_servico(self):
        while True:
            id = self.tela.mostra_tela_deletar()

            if not id:
                return None

            servico_para_deletar = self.busca_servico_por_id(id)

            if not servico_para_deletar:
                self.tela.mostra_mensagem_erro('Não existe serviço com este ID.')
                continue
            
            self.controlador_principal.loja.servicos_prestados.remove(servico_para_deletar)
            self.tela.mostra_mensagem_sucesso('Serviço removido.')
            return True
    
    def busca_servico_por_id(self, id: int):
        for servico in self.controlador_principal.loja.servicos_prestados:
            if servico.id == id:
                return servico
        
        return None
    
    def busca_servico_por_atributos(self, tipo_servico, veiculo, valor, data):
        for servico in self.__controlador_principal.loja.servicos_prestados:
            if (servico.tipo_servico == tipo_servico and
                servico.veiculo == veiculo and
                servico.valor == valor and
                servico.data == data):
                return servico
        return None
    