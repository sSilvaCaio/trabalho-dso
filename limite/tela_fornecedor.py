from limite.telaAbstrata import TelaAbstrata

class TelaFornecedor(TelaAbstrata):
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_tela_inicial(self):
        print("----SISTEMA DE FORNECEDORES----")

    def mostra_tela_opcoes(self):
        print("\n----OPÇÕES----")
        print("1 - Cadastrar Fornecedor")
        print("2 - Listar Fornecedores")
        print("3 - Alterar Fornecedor")
        print("4 - Excluir Fornecedor")
        print("0 - Retornar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def mostra_tela_cadastro(self):
        print("\n----CADASTRO DE FORNECEDOR----")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        cnpj = input("CNPJ: ")
        return {"nome": nome, "telefone": telefone, "idade": idade, "sexo": sexo, "cnpj": cnpj}

    def mostra_tela_alteracao(self):
        print("\n----ALTERAÇÃO DE FORNECEDOR----")
        print("Deixe em branco para não alterar")
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        idade = input("Nova idade: ")
        sexo = input("Novo sexo: ")
        return {"nome": nome, "telefone": telefone, "idade": int(idade) if idade else None, "sexo": sexo}

    def seleciona_fornecedor(self):
        cnpj = input("\nCNPJ do fornecedor: ")
        return cnpj

    def mostra_dados_fornecedor(self, dados):
        print("\n----DADOS DO FORNECEDOR----")
        print(f"Nome: {dados['nome']}")
        print(f"Telefone: {dados['telefone']}")
        print(f"Idade: {dados['idade']}")
        print(f"Sexo: {dados['sexo']}")
        print(f"CNPJ: {dados['cnpj']}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_mensagem_TypeError(self, erro):
        print(f"\nERRO: O campo '{erro[0]}' deve ser do tipo '{erro[1]}'")

    def mostra_mensagem_Exception(self, erro):
        print(f"\nERRO: {erro}")
