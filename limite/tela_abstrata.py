from abc import ABC
import FreeSimpleGUI as sg


class TelaAbstrata(ABC):
    """Classe base para telas. Fornece mensagens via FreeSimpleGUI.

    Mantém um método `le_num_inteiro` simples para compatibilidade, mas as
    telas GUI devem implementar suas próprias janelas (ver exemplos nas
    classes de tela)."""

    def le_num_inteiro(self, mensagem: str = "", inteiros_permitidos: list = None):
        # Compatibilidade: usa uma popup simples para entrada de número.
        layout = [
            [sg.Text(mensagem)],
            [sg.Input(key="__entrada__")],
            [sg.Button("OK"), sg.Button("Cancelar")],
        ]

        janela = sg.Window("Entrada Numérica", layout, modal=True, finalize=True)
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Cancelar":
                janela.close()
                return None

            entrada = valores.get("__entrada__", "").strip()
            if not entrada:
                janela.close()
                return None

            try:
                num_int = int(entrada)
                if inteiros_permitidos and num_int not in inteiros_permitidos:
                    sg.popup_error(f"Valor inválido. Opções permitidas: {inteiros_permitidos}")
                    continue
                janela.close()
                return num_int
            except ValueError:
                sg.popup_error("Valor inválido. Digite um número inteiro.")

    def mostra_mensagem_erro(self, mensagem: str):
        sg.popup_error(mensagem)

    def mostra_mensagem(self, mensagem: str):
        sg.popup_ok(mensagem)
