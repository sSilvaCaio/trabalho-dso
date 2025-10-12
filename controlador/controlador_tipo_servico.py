from entidade.tipo_servico import TipoServico
from limite.tela_tipo_servico import TelaTipoServico
from .controlador_principal import ControladorPrincipal


class ControladorTipoServico():
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__tipos_servico = []
        self.__tela = TelaTipoServico(self)
        if isinstance(controlador_principal, ControladorPrincipal):
            self.__controlador_principal = controlador_principal

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    def busca_tipo_servico_por_nome(self, nome):
        for tipo_servico in self.__tipos_servico:
            if nome == tipo_servico.nome:
                return tipo_servico
        return None
    
    def inicia(self):
        self.tela.mostra_tela_inicial()

    def cadastra_tipo_servico(self):
        nome = self.tela.mostra_tela_cadastro()
        if self.busca_tipo_servico_por_nome(nome):
            self.tela.mostra_mensagem_erro('Já existe um tipo de serviço com esse nome')
            return None
        novo_tipo = TipoServico(nome)
        self.__tipos_servico.append(novo_tipo)
        self.tela.mostra_mensagem_sucesso('Tipo de serviço ' + nome + ' adicionada')
        return novo_tipo

    def altera_tipo_servico(self):
        nome_atual, novo_nome = self.tela.mostra_tela_alteracao()
        tipo_servico = self.busca_tipo_servico_por_nome(nome_atual)
        if not tipo_servico:
            self.tela.mostra_mensagem_erro('Não existe tipo de serviço com o nome: ' + nome_atual)
            return None
        
        novo_tipo = self.busca_tipo_servico_por_nome(novo_nome)
        if novo_tipo:
            self.tela.mostra_mensagem_erro('Já existe um tipo de serviço com o nome: ' + novo_nome)
            return None
        
        tipo_servico.nome = novo_nome

        self.tela.mostra_mensagem_sucesso(f'Nome do tipo de serviço {nome_atual} foi alterado para {novo_nome}')

        return tipo_servico
    
    def lista_tipos_servico(self):
        self.tela.mostra_tela_lista(self.__tipos_servico)

    def deleta_tipo_servico(self):
        nome = self.tela.mostra_tela_deletar()
        tipo_servico = self.busca_tipo_servico_por_nome()
        if not tipo_servico:
            self.tela.mostra_mensagem_erro('Não existe tipo de serviço com este nome.')
            return None
        
        self.__tipos_servico.remove(tipo_servico)
        self.tela.mostra_mensagem_sucesso('Tipo de serviço ' + nome + ' deletada')
        return True
    
    def abre_tela_opcoes(self):
        switcher = {0: 'Voltar', 1: self.cadastra_tipo_servico, 2: self.lista_tipos_servico, 3: self.altera_tipo_servico, 4: self.deleta_tipo_servico}
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()