from entidade.tipo_servico import TipoServico
from limite.tela_tipo_servico import TelaTipoServico


class ControladorTipoServico():
    def __init__(self, controlador_principal):
        self.__tela = TelaTipoServico(self)
        self.__controlador_principal = controlador_principal

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {1: self.cadastra_tipo_servico, 2: self.lista_tipos_servico, 3: self.altera_tipo_servico, 4: self.deleta_tipo_servico}
        while True:
            opcao = self.__tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela.mostra_mensagem_erro("Opção inválida.")

    def cadastra_tipo_servico(self):
        while True:
            nome = self.tela.mostra_tela_cadastro()

            if not nome:
                return None
            
            if self.busca_tipo_servico_por_nome(nome):
                self.tela.mostra_mensagem_erro('Já existe um tipo de serviço com esse nome')
                continue

            novo_tipo = TipoServico(nome)
            self.controlador_principal.loja.tipos_servico.append(novo_tipo)
            self.tela.mostra_mensagem('Tipo de serviço ' + nome + ' foi adicionado')
            return novo_tipo

    def altera_tipo_servico(self):
        while True:
            nome_atual, novo_nome = self.tela.mostra_tela_alteracao()

            if not nome_atual or not novo_nome:
                return None
            
            tipo_servico = self.busca_tipo_servico_por_nome(nome_atual)
            if not tipo_servico:
                self.tela.mostra_mensagem_erro('Não existe tipo de serviço com o nome: ' + nome_atual)
                return None
            
            novo_tipo = self.busca_tipo_servico_por_nome(novo_nome)
            if novo_tipo:
                self.tela.mostra_mensagem_erro('Já existe um tipo de serviço com o nome: ' + novo_nome)
                return None
            
            tipo_servico.nome = novo_nome

            self.tela.mostra_mensagem(f'Nome do tipo de serviço {nome_atual} foi alterado para {novo_nome}')

            return tipo_servico
    
    def lista_tipos_servico(self):
        self.tela.mostra_tela_lista(self.controlador_principal.loja.tipos_servico)

    def deleta_tipo_servico(self):
        nome = self.tela.mostra_tela_deletar()

        if not nome:
            return None
        
        tipo_servico = self.busca_tipo_servico_por_nome(nome)
        if not tipo_servico:
            self.tela.mostra_mensagem_erro('Não existe tipo de serviço com este nome.')
            return None
        
        self.controlador_principal.loja.tipos_servico.remove(tipo_servico)
        self.tela.mostra_mensagem('Tipo de serviço ' + nome + ' deletado')
        return True

    def busca_tipo_servico_por_nome(self, nome):
        for tipo_servico in self.controlador_principal.loja.tipos_servico:
            if nome == tipo_servico.nome:
                return tipo_servico
        return None
    