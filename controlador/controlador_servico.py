from .controlador_principal import ControladorPrincipal
from limite.tela_servico import TelaServico
from entidade.servico import Servico


class ControladorServico():
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__servicos = []
        self.__tela = TelaServico(self)
        if isinstance(controlador_principal, ControladorPrincipal):
            self.__controlador_principal = controlador_principal

    @property
    def tela(self):
        return self.__tela
    
    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def busca_servico_por_id(self, id: int):
        for servico in self.__servicos:
            if servico.id == id:
                return servico
        
        return None
    
    def busca_servico_por_dados(self, dados: dict):
        tipo_servico = self.controlador_principal.controlador_tipo_servico.busca_tipo_servico_por_nome(dados['tipo_servico'])
        veiculo = self.controlador_principal.controlador_veiculo.busca_veiculo_por_chassi(dados['chassi_veiculo'])
        for servico in self.__servicos:
            if (servico.tipo_servico == tipo_servico and
                    servico.veiculo == veiculo and
                    servico.valor == dados['valor'] and
                    servico.data == dados['data']):
                return servico
        
        return None

    def inicia(self):
        self.tela.mostra_tela_inicial()

    def cadastrar_servico(self):
        dados_servico = self.tela.mostra_tela_cadastro()

        if self.busca_servico_por_dados(dados_servico):
            self.tela.mostra_mensagem_erro('Já existe serviço cadastrado com esses dados')

        veiculo = (self.controlador_principal.controlador_veiculo.
                   busca_veiculo_por_chassi(dados_servico['chassi_veiculo']))

        if not veiculo:
            (self.controlador_principal.controlador_veiculo.tela.
            mostra_mensagem_erro('Não existe veículo cadastrado com este chassi'))
            return None

        tipo_servico = (self.controlador_principal.controlador_tipo_servico.
                        busca_tipo_servico_por_nome(dados_servico['tipo_servico']))
        
        if not tipo_servico:
            (self.controlador_principal.controlador_tipo_servico.tela.
             mostra_mensagem_erro('Não existe tipo de serviço cadastrado com este nome'))
            return None

        for servico in self.__servicos:
            if (servico.tipo_servico == tipo_servico and
                    servico.veiculo == veiculo and 
                    servico.valor == dados_servico['valor'] and
                    servico.data == dados_servico['data']):
                self.tela.mostra_mensagem_erro('Já existe um serviço cadastrado com esses dados.')
                return None
            
        novo_servico = Servico(tipo_servico, veiculo, dados_servico['valor'], dados_servico['data'])
        self.tela.mostra_mensagem_sucesso('Serviço registrado')
        self.__servicos.append(novo_servico)
        return novo_servico


    def lista_servicos(self):
        self.tela.mostra_tela_lista(self.__servicos)

    def altera_servico(self):
        novos_dados = self.tela.mostra_tela_alteracao()

        servico = self.busca_servico_por_id(novos_dados['id'])

        if not servico:
            self.tela.mostra_mensagem_erro('Não existe serviço cadastrado com este ID')

        tipo_servico = (self.controlador_principal.controlador_tipo_servico.
                        busca_tipo_servico_por_nome(novos_dados['tipo_servico']))
        
        if not tipo_servico:
            (self.controlador_principal.controlador_tipo_servico.tela.
             mostra_mensagem_erro('Não existe tipo de serviço cadastrado com este nome'))
            return None

        veiculo = self.controlador_principal.controlador_veiculo.busca_veiculo_por_chassi(novos_dados['chassi'])

        if not veiculo:
            (self.controlador_principal.controlador_veiculo.tela.
             mostra_mensagem_erro('Não existe veículo com este chassi.'))
            return None
        

        servico.tipo_servico = tipo_servico
        servico.veiculo = veiculo
        servico.valor = novos_dados["valor"]
        servico.data = novos_dados["data"]

        self.tela.mostra_mensagem_sucesso('Serviço alterado.')
        return servico

    
    def deleta_servico(self):
        id = self.tela.mostra_tela_deletar()
        servico_para_deletar = self.busca_servico_por_id(id)
        if not servico_para_deletar:
            self.tela.mostra_mensagem_erro('Não existe serviço com este ID.')
            return None
        
        self.__servicos.remove(servico_para_deletar)
        self.tela.mostra_mensagem_sucesso('Serviço removido.')
        return servico_para_deletar
    
