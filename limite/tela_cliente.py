from limite.telaAbstrata import TelaAbstrata

class TelaCliente(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print("----SISTEMA DE CLIENTES----")

    def mostra_tela_opcoes(self):
        print("\n----OPÇÕES----")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Alterar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Retornar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def mostra_tela_cadastro(self):
        print("\n----CADASTRO DE CLIENTE----")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        cpf = input("CPF: ")
        return {"nome": nome, "telefone": telefone, "idade": idade, "sexo": sexo, "cpf": cpf}

    def mostra_tela_alteracao(self):
        print("\n----ALTERAÇÃO DE CLIENTE----")
        print("Deixe em branco para não alterar")
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        idade = input("Nova idade: ")
        sexo = input("Novo sexo: ")
        return {"nome": nome, "telefone": telefone, "idade": int(idade) if idade else None, "sexo": sexo}

    def seleciona_cliente(self):
        cpf = input("\nCPF do cliente: ")
        return cpf

    def mostra_dados_cliente(self, dados):
        print("\n----DADOS DO CLIENTE----")
        print(f"Nome: {dados['nome']}")
        print(f"Telefone: {dados['telefone']}")
        print(f"Idade: {dados['idade']}")
        print(f"Sexo: {dados['sexo']}")
        print(f"CPF: {dados['cpf']}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_mensagem_TypeError(self, erro):
        print(f"\nERRO: O campo '{erro[0]}' deve ser do tipo '{erro[1]}'")

    def mostra_mensagem_Exception(self, erro):
        print(f"\nERRO: {erro}")
