from entidade.marca import Marca
from limite.tela_marca import TelaMarca
from excecao.marca_ja_existe_exception import MarcaJaExisteException
from excecao.marca_nao_encontrada_exception import MarcaNaoEncontradaException


class ControladorMarca:
    def __init__(self, controlador_principal):
        self.__tela = TelaMarca(self)
        self.__controlador_principal = controlador_principal
        self.__dao = self.controlador_principal.loja.marca_dao

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def dao(self):
        return self.__dao

    def abre_tela_opcoes(self):
        switcher = {
            1: self.cadastra_marca,
            2: self.lista_marcas,
            3: self.altera_marca,
            4: self.deleta_marca,
        }
        while True:
            opcao = self.__tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela.mostra_mensagem_erro("Opção inválida.")

    def cadastra_marca(self):
        while True:
            nome = self.tela.mostra_tela_cadastro()
            if not nome:
                return None

            try:
                if self.dao.get_by_nome(nome):
                    raise MarcaJaExisteException(nome)

                nova_marca = Marca(nome)
                if self.dao.add(nova_marca):
                    self.tela.mostra_mensagem("Marca " + nome + " adicionada")
                    return nova_marca
                self.tela.mostra_mensagem_erro("Erro ao adicionar marca.")
                return None

            except MarcaJaExisteException as e:
                self.tela.mostra_mensagem_erro(str(e))
                continue

    def altera_marca(self):
        while True:
            nome_atual, novo_nome = self.tela.mostra_tela_alteracao()

            if not nome_atual or not novo_nome:
                return None

            try:
                marca = self.dao.get_by_nome(nome_atual)
                if not marca:
                    raise MarcaNaoEncontradaException(nome_marca=nome_atual)

                if self.dao.get_by_nome(novo_nome):
                    raise MarcaJaExisteException(novo_nome)

                marca.nome = novo_nome
                if self.dao.update(marca):
                    self.tela.mostra_mensagem(
                        f"Nome da marca {nome_atual} foi alterado para {novo_nome}"
                    )
                    return marca
                return None

            except (MarcaNaoEncontradaException, MarcaJaExisteException) as e:
                self.tela.mostra_mensagem_erro(str(e))
                continue

    def lista_marcas(self):
        marcas = self.dao.get_all()
        marcas_dict = [{"id": marca.id, "nome": marca.nome} for marca in marcas]
        self.tela.mostra_tela_lista(marcas_dict)

    def deleta_marca(self):
        while True:
            nome = self.tela.mostra_tela_deletar()

            if not nome:
                return None

            try:
                marca = self.dao.get_by_nome(nome)
                if not marca:
                    raise MarcaNaoEncontradaException(nome_marca=nome)

                if self.dao.remove(marca.id):
                    self.tela.mostra_mensagem("Marca " + nome + " deletada")
                    return True
                return None

            except MarcaNaoEncontradaException as e:
                self.tela.mostra_mensagem_erro(str(e))
                continue
