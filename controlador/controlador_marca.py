from entidade.marca import Marca
from limite.tela_marca import TelaMarca
from .controlador_principal import ControladorPrincipal


class ControladorMarca():
    def __init__(self, controlador_principal: ControladorPrincipal):
        self.__marcas = []
        self.__tela = TelaMarca(self)
        if isinstance(controlador_principal, ControladorPrincipal):
            self.__controlador_principal = controlador_principal

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    def busca_marca_por_nome(self, nome):
        for marca in self.__marcas:
            if nome == marca.nome:
                return marca
        return None
    
    def inicia(self):
        self.tela.mostra_tela_inicial()

    def cadastra_marca(self):
        nome = self.tela.mostra_tela_cadastro()
        if self.busca_marca_por_nome(nome):
            self.tela.mostra_mensagem_erro('Já existe uma marca com esse nome')
            return None
        nova_marca = Marca(nome)
        self.__marcas.append(nova_marca)
        self.tela.mostra_mensagem_sucesso('Marca ' + nome + ' adicionada')
        return nova_marca

    def altera_marca(self):
        nome_atual, novo_nome = self.tela.mostra_tela_alteracao()
        marca = self.busca_marca_por_nome(nome_atual)
        if not marca:
            self.tela.mostra_mensagem_erro('Não existe marca com o nome: ' + nome_atual)
            return None
        
        nova_marca = self.busca_marca_por_nome(novo_nome)
        if nova_marca:
            self.tela.mostra_mensagem_erro('Já existe uma marca com o nome: ' + novo_nome)
            return None
        
        marca.nome = novo_nome

        self.tela.mostra_mensagem_sucesso(f'Nome da marca {nome_atual} foi alterado para {novo_nome}')

        return marca
    
    def lista_marcas(self):
        self.tela.mostra_tela_lista(self.__marcas)

    def deleta_marca(self):
        nome = self.tela.mostra_tela_deletar()
        marca = self.busca_marca_por_nome()
        if not marca:
            self.tela.mostra_mensagem_erro('Não existe marca com este nome.')
            return None
        
        self.__marcas.remove(marca)
        self.tela.mostra_mensagem_sucesso('Marca ' + nome + ' deletada')
        return True
    
    def abre_tela_opcoes(self):
        switcher = {0: 'Voltar', 1: self.cadastra_marca, 2: self.lista_marcas, 3: self.altera_marca, 4: self.deleta_marca}
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()