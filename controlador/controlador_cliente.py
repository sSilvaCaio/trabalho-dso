from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from excecoes.clienteNaoEncontradoException import ClienteNaoEncontradoException

class ControladorCliente:
    def __init__(self):
        self.__clientes = []
        self.__tela_cliente = TelaCliente(self)

    def busca_cliente_por_cpf(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        raise ClienteNaoEncontradoException

    def cadastra_cliente(self):
        try:
            self.__tela_cliente.mostra_tela_inicial()
            dados_cliente = self.__tela_cliente.mostra_tela_cadastro()
            try:
                self.busca_cliente_por_cpf(dados_cliente['cpf'])
                self.__tela_cliente.mostra_mensagem("ERRO: Cliente já cadastrado!")
                return None
            except ClienteNaoEncontradoException:
                pass
            novo_cliente = Cliente(
                dados_cliente["nome"],
                dados_cliente["telefone"],
                dados_cliente["idade"],
                dados_cliente["sexo"],
                dados_cliente["cpf"]
            )
            self.__clientes.append(novo_cliente)
            self.__tela_cliente.mostra_mensagem("Cliente cadastrado com sucesso!")
            return novo_cliente
        except TypeError as e:
            return self.__tela_cliente.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_cliente.mostra_mensagem_Exception(e)

    def lista_clientes(self):
        if len(self.__clientes) == 0:
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado!")
            return
        for cliente in self.__clientes:
            dados_cliente = {
                "nome": cliente.nome,
                "telefone": cliente.telefone,
                "idade": cliente.idade,
                "sexo": cliente.sexo,
                "cpf": cliente.cpf
            }
            self.__tela_cliente.mostra_dados_cliente(dados_cliente)

    def altera_cliente(self):
        try:
            cpf = self.__tela_cliente.seleciona_cliente()
            cliente = self.busca_cliente_por_cpf(cpf)
            novos_dados = self.__tela_cliente.mostra_tela_alteracao()
            if novos_dados["nome"]:
                cliente.nome = novos_dados["nome"]
            if novos_dados["telefone"]:
                cliente.telefone = novos_dados["telefone"]
            if novos_dados["idade"]:
                cliente.idade = novos_dados["idade"]
            if novos_dados["sexo"]:
                cliente.sexo = novos_dados["sexo"]
            self.__tela_cliente.mostra_mensagem("Cliente alterado com sucesso!")
            return True
        except TypeError as e:
            return self.__tela_cliente.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_cliente.mostra_mensagem_Exception(e)

    def deleta_cliente(self):
        try:
            cpf = self.__tela_cliente.seleciona_cliente()
            cliente = self.busca_cliente_por_cpf(cpf)
            self.__clientes.remove(cliente)
            self.__tela_cliente.mostra_mensagem("Cliente deletado com sucesso!")
            return True
        except TypeError as e:
            return self.__tela_cliente.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_cliente.mostra_mensagem_Exception(e)

    def abre_tela_opcoes(self):
        switcher = {
            0: 'break',
            1: self.cadastra_cliente,
            2: self.lista_clientes,
            3: self.altera_cliente,
            4: self.deleta_cliente
        }
        while True:
            opcao = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao)
            if funcao_escolhida == 'break':
                break
            elif funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_cliente.mostra_mensagem("Opção inválida!")
