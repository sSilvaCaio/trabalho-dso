from entidade.venda import Venda
from limite.tela_venda import TelaVenda

class ControladorVenda:
    def __init__(self):
        self.__vendas = []
        self.__tela_venda = TelaVenda(self)

    def registra_venda(self, veiculo, cliente, valor):
        try:
            nova_venda = Venda(veiculo, valor, cliente)
            self.__vendas.append(nova_venda)
            self.__tela_venda.mostra_mensagem("Venda registrada com sucesso!")
            return nova_venda
        except TypeError as e:
            return self.__tela_venda.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_venda.mostra_mensagem_Exception(e)

    def lista_vendas(self):
        if len(self.__vendas) == 0:
            self.__tela_venda.mostra_mensagem("Nenhuma venda registrada!")
            return
        for i, venda in enumerate(self.__vendas):
            dados_venda = {
                "veiculo": f"{venda.veiculo.marca} - {venda.veiculo.placa}",
                "cliente": venda.cliente.nome,
                "valor": venda.valor
            }
            print(f"\nVenda {i}:")
            self.__tela_venda.mostra_dados_venda(dados_venda)

    def busca_vendas_por_cliente(self, cpf_cliente):
        vendas_cliente = []
        for venda in self.__vendas:
            if venda.cliente.cpf == cpf_cliente:
                vendas_cliente.append(venda)
        if len(vendas_cliente) == 0:
            self.__tela_venda.mostra_mensagem("Nenhuma venda encontrada para este cliente!")
            return None
        for venda in vendas_cliente:
            dados_venda = {
                "veiculo": f"{venda.veiculo.marca} - {venda.veiculo.placa}",
                "cliente": venda.cliente.nome,
                "valor": venda.valor
            }
            self.__tela_venda.mostra_dados_venda(dados_venda)
        return vendas_cliente

    def abre_tela_opcoes(self):
        switcher = {
            0: 'break',
            1: self.registra_venda,
            2: self.lista_vendas,
            3: self.busca_vendas_por_cliente
        }
        while True:
            opcao = self.__tela_venda.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao)
            if funcao_escolhida == 'break':
                break
            elif funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_venda.mostra_mensagem("Opção inválida!")
