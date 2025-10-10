from limite.telaAbstrata import TelaAbstrata

class TelaVenda(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print("----SISTEMA DE VENDAS----")

    def mostra_tela_opcoes(self):
        print("\n----OPÇÕES----")
        print("1 - Registrar Venda")
        print("2 - Listar Vendas")
        print("3 - Buscar Vendas por Cliente")
        print("0 - Retornar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def mostra_tela_cadastro(self):
        print("\n----REGISTRO DE VENDA----")
        chassi = int(input("Chassi do veículo: "))
        cpf_cliente = input("CPF do cliente: ")
        valor = float(input("Valor da venda: "))
        return {"chassi": chassi, "cpf_cliente": cpf_cliente, "valor": valor}

    def seleciona_venda(self):
        indice = int(input("\nÍndice da venda: "))
        return indice

    def mostra_dados_venda(self, dados):
        print("\n----DADOS DA VENDA----")
        print(f"Veículo: {dados['veiculo']}")
        print(f"Cliente: {dados['cliente']}")
        print(f"Valor: R$ {dados['valor']:.2f}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_mensagem_TypeError(self, erro):
        print(f"\nERRO: O campo '{erro[0]}' deve ser do tipo '{erro[1]}'")

    def mostra_mensagem_Exception(self, erro):
        print(f"\nERRO: {erro}")
