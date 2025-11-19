from entidade.fornecedor import Fornecedor
from limite.tela_fornecedor import TelaFornecedor

class ControladorFornecedor:
    def __init__(self, controlador_principal):
        self.__tela = TelaFornecedor(self)
        self.__controlador_principal = controlador_principal
    
    @property
    def tela(self):
        return self.__tela
    
    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {1: self.cadastra_fornecedor, 2: self.lista_fornecedores, 3: self.altera_fornecedor, 4: self.deleta_fornecedor}
        
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")
    
    def cadastra_fornecedor(self):
        while True:
            dados_fornecedor = self.tela.mostra_tela_cadastro()
            if not dados_fornecedor:
                return None
            
            if self.busca_fornecedor_por_cnpj(dados_fornecedor['cnpj']):
                self.tela.mostra_mensagem_erro("Já existe um fornecedor com este CNPJ!")
                continue
            
            novo_fornecedor = Fornecedor(
                nome=dados_fornecedor["nome"],
                telefone=dados_fornecedor["telefone"],
                idade=dados_fornecedor["idade"],
                sexo=dados_fornecedor["sexo"],
                cnpj=dados_fornecedor["cnpj"],
            )
            
            self.controlador_principal.loja.fornecedor_dao.add(novo_fornecedor)
            self.tela.mostra_mensagem("Fornecedor cadastrado com sucesso.")
            return novo_fornecedor
    
    def lista_fornecedores(self):
        fornecedores = self.controlador_principal.loja.fornecedor_dao.get_all()
        if not fornecedores:
            self.tela.mostra_mensagem("Nenhum fornecedor cadastrado.")
            return None
        
        self.tela.mostra_tela_lista(fornecedores)
    
    def deleta_fornecedor(self):
        while True:
            cnpj = self.tela.mostra_tela_deletar()
            if not cnpj:
                return None
            
            fornecedor = self.busca_fornecedor_por_cnpj(cnpj)
            if not fornecedor:
                self.tela.mostra_mensagem_erro("Não existe fornecedor com este CNPJ.")
                continue
            
            removido_com_sucesso = self.deleta_fornecedor_por_objeto(fornecedor)
            if removido_com_sucesso:
                self.tela.mostra_mensagem('Fornecedor deletado.')
                return True
            else:
                self.tela.mostra_mensagem_erro('Erro ao deletar fornecedor.')
                return False
    
    def altera_fornecedor(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()
            if not novos_dados:
                return None
            
            fornecedor = self.busca_fornecedor_por_cnpj(novos_dados['cnpj'])
            if not fornecedor:
                self.tela.mostra_mensagem_erro('Não existe fornecedor com este CNPJ.')
                continue
            
            if novos_dados['nome'] != ' ': fornecedor.nome = novos_dados["nome"]
            if novos_dados['telefone'] != ' ': fornecedor.telefone = novos_dados["telefone"]
            if novos_dados['idade'] != ' ': fornecedor.idade = novos_dados["idade"]
            if novos_dados['sexo'] != ' ': fornecedor.sexo = novos_dados["sexo"]
            
            self.controlador_principal.loja.fornecedor_dao.update(fornecedor)
            self.tela.mostra_mensagem('Fornecedor alterado.')
            return fornecedor
    
    def deleta_fornecedor_por_objeto(self, fornecedor_para_deletar: Fornecedor):
        if fornecedor_para_deletar and isinstance(fornecedor_para_deletar, Fornecedor):
            self.controlador_principal.loja.fornecedor_dao.remove(fornecedor_para_deletar.cnpj)
            return True
        return False
    
    def busca_fornecedor_por_cnpj(self, cnpj):
        fornecedores = self.controlador_principal.loja.fornecedor_dao.get_all()
        for fornecedor in fornecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        return None
