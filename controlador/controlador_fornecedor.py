from entidade.fornecedor import Fornecedor
from limite.tela_fornecedor import TelaFornecedor
from excecoes.fornecedorNaoEncontradoException import FornecedorNaoEncontradoException

class ControladorFornecedor:
    def __init__(self):
        self.__fornecedores = []
        self.__tela_fornecedor = TelaFornecedor(self)

    def busca_fornecedor_por_cnpj(self, cnpj):
        for fornecedor in self.__fornecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        raise FornecedorNaoEncontradoException

    def cadastra_fornecedor(self):
        try:
            self.__tela_fornecedor.mostra_tela_inicial()
            dados_fornecedor = self.__tela_fornecedor.mostra_tela_cadastro()
            try:
                self.busca_fornecedor_por_cnpj(dados_fornecedor['cnpj'])
                self.__tela_fornecedor.mostra_mensagem("ERRO: Fornecedor já cadastrado!")
                return None
            except FornecedorNaoEncontradoException:
                pass
            novo_fornecedor = Fornecedor(
                dados_fornecedor["nome"],
                dados_fornecedor["telefone"],
                dados_fornecedor["idade"],
                dados_fornecedor["sexo"],
                dados_fornecedor["cnpj"]
            )
            self.__fornecedores.append(novo_fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor cadastrado com sucesso!")
            return novo_fornecedor
        except TypeError as e:
            return self.__tela_fornecedor.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_fornecedor.mostra_mensagem_Exception(e)

    def lista_fornecedores(self):
        if len(self.__fornecedores) == 0:
            self.__tela_fornecedor.mostra_mensagem("Nenhum fornecedor cadastrado!")
            return
        for fornecedor in self.__fornecedores:
            dados_fornecedor = {
                "nome": fornecedor.nome,
                "telefone": fornecedor.telefone,
                "idade": fornecedor.idade,
                "sexo": fornecedor.sexo,
                "cnpj": fornecedor.cnpj
            }
            self.__tela_fornecedor.mostra_dados_fornecedor(dados_fornecedor)

    def altera_fornecedor(self):
        try:
            cnpj = self.__tela_fornecedor.seleciona_fornecedor()
            fornecedor = self.busca_fornecedor_por_cnpj(cnpj)
            novos_dados = self.__tela_fornecedor.mostra_tela_alteracao()
            if novos_dados["nome"]:
                fornecedor.nome = novos_dados["nome"]
            if novos_dados["telefone"]:
                fornecedor.telefone = novos_dados["telefone"]
            if novos_dados["idade"]:
                fornecedor.idade = novos_dados["idade"]
            if novos_dados["sexo"]:
                fornecedor.sexo = novos_dados["sexo"]
            self.__tela_fornecedor.mostra_mensagem("Fornecedor alterado com sucesso!")
            return True
        except TypeError as e:
            return self.__tela_fornecedor.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_fornecedor.mostra_mensagem_Exception(e)

    def deleta_fornecedor(self):
        try:
            cnpj = self.__tela_fornecedor.seleciona_fornecedor()
            fornecedor = self.busca_fornecedor_por_cnpj(cnpj)
            self.__fornecedores.remove(fornecedor)
            self.__tela_fornecedor.mostra_mensagem("Fornecedor deletado com sucesso!")
            return True
        except TypeError as e:
            return self.__tela_fornecedor.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_fornecedor.mostra_mensagem_Exception(e)

    def abre_tela_opcoes(self):
        switcher = {
            0: 'break',
            1: self.cadastra_fornecedor,
            2: self.lista_fornecedores,
            3: self.altera_fornecedor,
            4: self.deleta_fornecedor
        }
        while True:
            opcao = self.__tela_fornecedor.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao)
            if funcao_escolhida == 'break':
                break
            elif funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_fornecedor.mostra_mensagem("Opção inválida!")
