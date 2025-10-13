from entidade.marca import Marca
from limite.tela_marca import TelaMarca


class ControladorMarca():
    def __init__(self, controlador_principal):
        self.__tela = TelaMarca(self)
        self.__controlador_principal = controlador_principal

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {0: 'Voltar', 1: self.cadastra_marca, 2: self.lista_marcas, 3: self.altera_marca, 4: self.deleta_marca}
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastra_marca(self):
        while True:
            nome = self.tela.mostra_tela_cadastro()

            if not nome:
                return None
            
            if self.busca_marca_por_nome(nome):
                self.tela.mostra_mensagem_erro('Já existe uma marca com esse nome')
                continue
            
            nova_marca = Marca(nome)
            self.controlador_principal.loja.marcas.append(nova_marca)
            self.tela.mostra_mensagem('Marca ' + nome + ' adicionada')
            return nova_marca

    def altera_marca(self):
        while True:
            nome_atual, novo_nome = self.tela.mostra_tela_alteracao()

            if not nome_atual or not novo_nome:
                return None
            
            marca = self.busca_marca_por_nome(nome_atual)

            if not marca:
                self.tela.mostra_mensagem_erro('Não existe marca com o nome: ' + nome_atual)
                continue
            
            nova_marca = self.busca_marca_por_nome(novo_nome)
            if nova_marca:
                self.tela.mostra_mensagem_erro('Já existe uma marca com o nome: ' + novo_nome)
                continue
            
            marca.nome = novo_nome

            self.tela.mostra_mensagem(f'Nome da marca {nome_atual} foi alterado para {novo_nome}')

            return marca
    
    def lista_marcas(self):
        self.tela.mostra_tela_lista(self.controlador_principal.loja.marcas)

    def deleta_marca(self):
        while True:
            nome = self.tela.mostra_tela_deletar()

            if not nome:
                return None
            
            marca = self.busca_marca_por_nome(nome)

            if not marca:
                self.tela.mostra_mensagem_erro('Não existe marca com este nome.')
                continue
            
            self.controlador_principal.loja.marcas.remove(marca)
            self.tela.mostra_mensagem('Marca ' + nome + ' deletada')
            return True
    
    def busca_marca_por_nome(self, nome):
        for marca in self.controlador_principal.loja.marcas:
            if nome == marca.nome:
                return marca
        return None
    