from limite.tela_abstrata import TelaAbstrata


class TelaRelatorios(TelaAbstrata):
    def __init__(self, controlador_relatorios):
        super().__init__()
        self.__controlador_relatorios = controlador_relatorios

    def mostra_tela_opcoes(self):
        print("\nEscolha um relatório:")
        print("1: Serviços mais prestados por mês")
        print("2: Quantidade de veículos em estoque por marca")
        print("0: Voltar")
        return self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2])

    def mostra_relatorio_servicos_por_mes(self, dados_relatorio: dict):
        print("\n" + "="*50)
        print("      RELATÓRIO DE SERVIÇOS MAIS PRESTADOS POR MÊS")
        print("="*50)

        if not dados_relatorio:
            self.mostra_mensagem_erro("Nenhum serviço prestado encontrado para gerar este relatório.")
            print("="*50)
            return

        for mes in sorted(dados_relatorio.keys()):
            print(f"\n Mês de Referência: {mes}")
            servicos_do_mes = dados_relatorio[mes]
            servicos_ordenados = sorted(servicos_do_mes.items(), key=lambda item: item[1], reverse=True)
            
            for nome_servico, quantidade in servicos_ordenados:
                plural = "vezes" if quantidade > 1 else "vez"
                print(f"  - {nome_servico:.<30} {quantidade} {plural}")
        
        print("\n" + "="*50)

    def mostra_relatorio_veiculos_em_estoque_por_marca(self, dados_relatorio: dict):
        print("\n" + "="*50)
        print("      RELATÓRIO DE VEÍCULOS POR MARCA")
        print("="*50)

        if not dados_relatorio:
            self.mostra_mensagem_erro("Nenhum veículo encontrado para gerar este relatório.")
            print("="*50)
            return

        marcas_ordenadas = sorted(dados_relatorio.items(), key=lambda item: item[1], reverse=True)
        
        for nome_marca, quantidade in marcas_ordenadas:
            plural = "veículos" if quantidade > 1 else "veículo"
            print(f"  - {nome_marca:.<30} {quantidade} {plural}")
        
        print("\n" + "="*50)