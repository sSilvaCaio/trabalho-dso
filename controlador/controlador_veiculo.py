from entidade.veiculo import Veiculo


class ControladorVeiculo:
    def __init__(self):
        self.__veiculos = []
        self.__tela_veiculo = TelaVeiculo(self)

    def inicia(self):
        print("----CONTROLADOR VEICULO ----")

    def cadastra_veiculo(self):
        dados_veiculo = {
            "chassi": 1,
            "ano": 2000,
            "cor": "Verde",
            "placa": "1a",
            "potencia": "123W",
            "quilometragem": 12,
            "marca": "fiat",
        }
        self.__tela_veiculo.mostra_tela_cadastro()
        for veiculo in self.__veiculos:
            if veiculo.chassi == dados_veiculo["chassi"]:
                print("Já existe um veículo cadastrado com este chassi")
                return False

        novo_veiculo = Veiculo(
            dados_veiculo["chassi"],
            dados_veiculo["ano"],
            dados_veiculo["cor"],
            dados_veiculo["placa"],
            dados_veiculo["potencia"],
            dados_veiculo["quilometragem"],
            dados_veiculo["marca"],
        )

        self.__veiculos.append(novo_veiculo)
        return novo_veiculo

    def lista_veiculos(self):
        return self.__tela_veiculo.mostra_tela_lista()

    def deleta_veiculo(self, veiculo):
        if veiculo not in self.__veiculos:
            print("O veículo não existe")
            return None

        veiculo_excluido = self.__veiculos.pop(veiculo)
        del veiculo_excluido
        print("Veiculo excluído")
        return True

    def altera_veiculo(self, novos_dados):

        for veiculo in self.__veiculos:
            if veiculo.chassi == novos_dados["chassi"]:
                veiculo.ano = novos_dados["ano"]
                veiculo.cor = novos_dados["cor"]
                veiculo.placa = novos_dados["placa"]
                veiculo.potencia = novos_dados["potencia"]
                veiculo.quilometragem = novos_dados["quilometragem"]
                veiculo.marca = novos_dados["marca"]

                return self.__tela_veiculo.mostra_tela_informacoes_veiculo()

        print("Veiculo não foi encontrado")
        return None

    def abre_tela_opcoes():
        switcher = {0: 'break', 1: self.cadastra_veiculo(), 2: self.lista_veiculos(), 3: self.abre_tela_informacoes_veiculo()}
        while True:
            