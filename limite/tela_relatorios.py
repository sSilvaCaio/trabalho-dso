from .tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaRelatorios(TelaAbstrata):
    def __init__(self, controlador_relatorios):
        super().__init__()
        self.__controlador_relatorios = controlador_relatorios
        sg.theme("DarkBlue3")

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Text("--- Relatórios ---", font=("Arial", 14, "bold"))],
            [sg.Button("Serviços por Mês", size=(25, 2))],
            [sg.Button("Veículos por Marca", size=(25, 2))],
            [sg.Button("Compras por Mês", size=(25, 2))],
            [sg.Button("Vendas por Mês", size=(25, 2))],
            [sg.Button("Voltar", size=(25, 2))],
        ]

        janela = sg.Window("Relatórios", layout)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Voltar":
                janela.close()
                return 0
            if evento == "Serviços por Mês":
                janela.close()
                return 1
            if evento == "Veículos por Marca":
                janela.close()
                return 2
            if evento == "Compras por Mês":
                janela.close()
                return 3
            if evento == "Vendas por Mês":
                janela.close()
                return 4

    def mostra_relatorio_servicos_por_mes(self, dados_relatorio: dict):
        if not dados_relatorio:
            sg.popup_error("Nenhum serviço prestado encontrado para gerar este relatório.")
            return

        texto = []
        texto.append("RELATÓRIO DE SERVIÇOS MAIS PRESTADOS POR MÊS\n" + "=" * 50)
        for mes in sorted(dados_relatorio.keys()):
            texto.append(f"\nMês de Referência: {mes}")
            servicos_do_mes = dados_relatorio[mes]
            servicos_ordenados = sorted(servicos_do_mes.items(), key=lambda item: item[1], reverse=True)
            for nome_servico, quantidade in servicos_ordenados:
                plural = "vezes" if quantidade > 1 else "vez"
                texto.append(f"  - {nome_servico:.<30} {quantidade} {plural}")

        sg.popup_scrolled("\n".join(texto), title="Serviços por Mês", size=(80, 20))

    def mostra_relatorio_veiculos_em_estoque_por_marca(self, dados_relatorio: dict):
        if not dados_relatorio:
            sg.popup_error("Nenhum veículo encontrado para gerar este relatório.")
            return

        texto = []
        texto.append("RELATÓRIO DE VEÍCULOS POR MARCA\n" + "=" * 50)
        marcas_ordenadas = sorted(dados_relatorio.items(), key=lambda item: item[1], reverse=True)
        for nome_marca, quantidade in marcas_ordenadas:
            plural = "veículos" if quantidade > 1 else "veículo"
            texto.append(f"  - {nome_marca:.<30} {quantidade} {plural}")

        sg.popup_scrolled("\n".join(texto), title="Veículos por Marca", size=(60, 15))

    def mostra_relatorio_compras_por_mes(self, dados_relatorio: dict):
        if not dados_relatorio:
            sg.popup_ok("Nenhuma compra encontrada para gerar este relatório.")
            return

        texto = ["RELATÓRIO DE COMPRAS POR MÊS\n" + "=" * 50]
        for mes in sorted(dados_relatorio.keys()):
            quantidade = dados_relatorio[mes]['quantidade']
            valor_total = dados_relatorio[mes]['valor_total']
            plural = "compras" if quantidade > 1 else "compra"
            texto.append(f"\nMês de Referência: {mes}")
            texto.append(f"   - Quantidade: {quantidade} {plural}")
            texto.append(f"   - Valor Total: R$ {valor_total:.2f}")

        sg.popup_scrolled("\n".join(texto), title="Compras por Mês", size=(70, 18))

    def mostra_relatorio_vendas_por_mes(self, dados_relatorio: dict):
        if not dados_relatorio:
            sg.popup_ok("Nenhuma venda encontrada para gerar este relatório.")
            return

        texto = ["RELATÓRIO DE VENDAS POR MÊS\n" + "=" * 50]
        for mes in sorted(dados_relatorio.keys()):
            quantidade = dados_relatorio[mes]['quantidade']
            valor_total = dados_relatorio[mes]['valor_total']
            plural = "vendas" if quantidade > 1 else "venda"
            texto.append(f"\nMês de Referência: {mes}")
            texto.append(f"   - Quantidade: {quantidade} {plural}")
            texto.append(f"   - Valor Total: R$ {valor_total:.2f}")

        sg.popup_scrolled("\n".join(texto), title="Vendas por Mês", size=(70, 18))
