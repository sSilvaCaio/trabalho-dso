from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente

class ControladorCliente:
    def __init__(self, controlador_principal):
        self.__tela = TelaCliente(self)
        self.__controlador_principal = controlador_principal
    
    @property
    def tela(self):
        return self.__tela
    
    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {1: self.cadastra_cliente, 2: self.lista_clientes, 3: self.altera_cliente, 4: self.deleta_cliente}
        
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")
    
    def cadastra_cliente(self):
        while True:
            dados_cliente = self.tela.mostra_tela_cadastro()
            if not dados_cliente:
                return None
            
            if self.busca_cliente_por_cpf(dados_cliente['cpf']):
                self.tela.mostra_mensagem_erro("Já existe um cliente com este CPF!")
                continue
            
            novo_cliente = Cliente(
                nome=dados_cliente["nome"],
                telefone=dados_cliente["telefone"],
                idade=dados_cliente["idade"],
                sexo=dados_cliente["sexo"],
                cpf=dados_cliente["cpf"],
            )
            
            self.controlador_principal.loja.clientes_cadastrados.append(novo_cliente)
            self.tela.mostra_mensagem("Cliente cadastrado com sucesso.")
            return novo_cliente
    
    def lista_clientes(self):
        clientes = self.controlador_principal.loja.clientes_cadastrados
        if not clientes:
            self.tela.mostra_mensagem("Nenhum cliente cadastrado.")
            return None
        
        self.tela.mostra_tela_lista(clientes)
    
    def deleta_cliente(self):
        while True:
            cpf = self.tela.mostra_tela_deletar()
            if not cpf:
                return None
            
            cliente = self.busca_cliente_por_cpf(cpf)
            if not cliente:
                self.tela.mostra_mensagem_erro("Não existe cliente com este CPF.")
                continue
            
            removido_com_sucesso = self.deleta_cliente_por_objeto(cliente)
            if removido_com_sucesso:
                self.tela.mostra_mensagem('Cliente deletado.')
                return True
            else:
                self.tela.mostra_mensagem_erro('Erro ao deletar cliente.')
                return False
    
    def altera_cliente(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()
            if not novos_dados:
                return None
            
            cliente = self.busca_cliente_por_cpf(novos_dados['cpf'])
            if not cliente:
                self.tela.mostra_mensagem_erro('Não existe cliente com este CPF.')
                continue
            
            if novos_dados['nome'] != ' ': cliente.nome = novos_dados["nome"]
            if novos_dados['telefone'] != ' ': cliente.telefone = novos_dados["telefone"]
            if novos_dados['idade'] != ' ': cliente.idade = novos_dados["idade"]
            if novos_dados['sexo'] != ' ': cliente.sexo = novos_dados["sexo"]
            
            self.tela.mostra_mensagem('Cliente alterado.')
            return cliente
    
    def deleta_cliente_por_objeto(self, cliente_para_deletar: Cliente):
        if cliente_para_deletar and isinstance(cliente_para_deletar, Cliente):
            if cliente_para_deletar in self.__controlador_principal.loja.clientes_cadastrados:
                self.__controlador_principal.loja.clientes_cadastrados.remove(cliente_para_deletar)
                return True
        return False
    
    def busca_cliente_por_cpf(self, cpf):
        for cliente in self.controlador_principal.loja.clientes_cadastrados:
            if cliente.cpf == cpf:
                return cliente
        return None
