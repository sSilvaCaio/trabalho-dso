from abc import abstractmethod, ABC


class TelaAbstrata(ABC):
    def __init__(self):
        pass

    def le_num_inteiro(self, inteiros_permitidos: list, mensagem: str):
        while True:
            num_str = input(mensagem)
            try:
                num = int(num_str)
                if num not in inteiros_permitidos:
                    self.mostra_mensagem_erro('Número inserido não está na lista de números permitidos: ', inteiros_permitidos)
                return num
            except ValueError:
                self.mostra_mensagem_erro('O valor inserido deve ser um número inteiro.')
        
    def mostra_mensagem_erro(self, mensagem: str):
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Houve um erro: ", mensagem)
        print("!!!!!!!!!!!!!!!!!!!!!!!!")