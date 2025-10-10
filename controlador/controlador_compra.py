from entidade.compra import Compra
from limite.tela_compra import TelaCompra

class ControladorCompra:
    def __init__(self):
        self.__compras = []
        self.__tela_compra = TelaCompra(self)

    def registra_compra(self, veiculo, fornecedor, valor):
        try:
            nova_compra = Compra(veiculo, valor, fornecedor)
            self.__compras.append(nova_compra)
            self.__tela_compra.mostra_mensagem("Compra registrada com sucesso!")
            return nova_compra
        except TypeError as e:
            return self.__tela_compra.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_compra.mostra_mensagem_Exception(e)

    def lista_compras(self):
        if len(self.__compras) == 0:
            self.__tela_compra.mostra_mensagem("Nenhuma compra registrada!")
            return
        for i, compra in enumerate(self.__compras):
            dados_compra = {
                "veiculo": f"{compra.veiculo.marca} - {compra.veiculo.placa}",
                "fornecedor": compra.fornecedor.nome,
                "valor": compra.valor
            }
            print(f"\nCompra {i}:")
            self.__tela_compra.mostra_dados_compra(dados_compra)

    def busca_compras_por_fornecedor(self, cnpj_fornecedor):
        compras_fornecedor = []
        for compra in self.__compras:
            if compra.fornecedor.cnpj == cnpj_fornecedor:
                compras_fornecedor.append(compra)
        if len(compras_fornecedor) == 0:
            self.__tela_compra.mostra_mensagem("Nenhuma compra encontrada para este fornecedor!")
            return None
        for compra in compras_fornecedor:
            dados_compra = {
                "veiculo": f"{compra.veiculo.marca} - {compra.veiculo.placa}",
                "fornecedor": compra.fornecedor.nome,
                "valor": compra.valor
            }
            self.__tela_compra.mostra_dados_compra(dados_compra)
        return compras_fornecedor

    def abre_tela_opcoes(self):
        switcher = {
            0: 'break',
            1: self.registra_compra,
            2: self.lista_compras,
            3: self.busca_compras_por_fornecedor
        }
        while True:
            opcao = self.__tela_compra.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao)
            if funcao_escolhida == 'break':
                break
            elif funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_compra.mostra_mensagem("Opção inválida!")
