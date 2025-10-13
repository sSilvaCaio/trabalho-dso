from abc import abstractmethod, ABC


class TelaAbstrata(ABC):
    def le_num_inteiro(self, mensagem: str = "", inteiros_permitidos: list = None):
        while True:
            num_str = input(mensagem).strip()
            if not num_str:
                return None
            
            try:
                num_int = int(num_str)
                if inteiros_permitidos and num_int not in inteiros_permitidos:
                    self.mostra_mensagem_erro(f'Valor inválido. Opções permitidas: {inteiros_permitidos}')
                else:
                    return num_int
            except ValueError:
                self.mostra_mensagem_erro('Valor inválido. Digite um número inteiro.')

   def le_data(self, mensagem: str = ""):
        while True:
            data_str = input(mensagem).strip()
            if not data_str:
                return None
            
            try:
                data_obj = datetime.strptime(data_str, "%d/%m/%Y")
                return data_obj
            except ValueError:
                self.mostra_mensagem_erro('Data inválida. Use o formato dd/mm/aaaa (ex: 25/12/2024)')
        
    def mostra_mensagem_erro(self, mensagem: str):
        print("\n!! ERRO : ", mensagem)
        print()

    def mostra_mensagem(self, mensagem: str):
        print("\n>> ", mensagem)
        print()
