from limite.telaAbstrata import TelaAbstrata

class TelaCompra(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print("----SISTEMA DE COMPRAS----")

    def mostra_tela_opcoes(self):
        print("\n----OPÇÕES----")
        print("1 - Registrar Compra")
        print("2 - Listar Compras")
        print("3 - Buscar Compras por Fornecedor")
        print("0 - Retornar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def mostra_tela_cadastro(self):
        print("\n----REGISTRO DE COMPRA----")
        chassi = int(input("Chassi do veículo: "))
        cnpj_fornecedor = input("CNPJ do fornecedor: ")
        valor = float(input("Valor da compra: "))
        return {"chassi": chassi, "cnpj_fornecedor": cnpj_fornecedor, "valor": valor}

    def seleciona_compra(self):
        indice = int(input("\nÍndice da compra: "))
        return indice

    def mostra_dados_compra(self, dados):
        print("\n----DADOS DA COMPRA----")
        print(f"Veículo: {dados['veiculo']}")
        print(f"Fornecedor: {dados['fornecedor']}")
        print(f"Valor: R$ {dados['valor']:.2f}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_mensagem_TypeError(self, erro):
        print(f"\nERRO: O campo '{erro[0]}' deve ser do tipo '{erro[1]}'")

    def mostra_mensagem_Exception(self, erro):
        print(f"\nERRO: {erro}")
