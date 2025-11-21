from entidade.compra import Compra
from limite.tela_compra import TelaCompra

class ControladorCompra:
    def __init__(self, controlador_principal):
        self.__tela = TelaCompra(self)
        self.__controlador_principal = controlador_principal
    
    @property
    def tela(self):
        return self.__tela
    
    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {1: self.registra_compra, 2: self.lista_compras, 3: self.altera_compra, 4: self.deleta_compra}
        
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")
    
    def registra_compra(self):
        while True:
            dados_compra = self.tela.mostra_tela_cadastro()
            if not dados_compra:
                return None
            
            veiculo = self.controlador_principal.controlador_veiculo.busca_veiculo_por_chassi(dados_compra['chassi'])
            if not veiculo:
                self.tela.mostra_mensagem_erro("Veículo não encontrado com este chassi.")
                continue
            else:
                estoque = self.controlador_principal.loja.veiculos_em_estoque_dao.get_all()
                if veiculo in estoque:
                    self.tela.mostra_mensagem_erro("Veículo já está no estoque")
                    continue
            
            fornecedor = self.controlador_principal.controlador_fornecedor.busca_fornecedor_por_cnpj(dados_compra['cnpj_fornecedor'])
            if not fornecedor:
                self.tela.mostra_mensagem_erro("Fornecedor não encontrado com este CNPJ.")
                continue
            
            nova_compra = Compra(
                veiculo=veiculo,
                valor=dados_compra['valor'],
                fornecedor=fornecedor,
                data=dados_compra['data']
            )
            
            self.controlador_principal.loja.compra_dao.add(nova_compra)
            self.controlador_principal.loja.veiculos_em_estoque_dao.add(veiculo.chassi, veiculo)
            
            self.tela.mostra_mensagem("Compra registrada com sucesso!")
            return nova_compra
    
    def lista_compras(self):
        compras = self.controlador_principal.loja.compra_dao.get_all()
        if not compras:
            self.tela.mostra_mensagem("Nenhuma compra registrada.")
            return None

        self.tela.mostra_tela_lista(compras)
    
    def altera_compra(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()
            if not novos_dados:
                return None
            
            compra = self.busca_compra_por_id(novos_dados['id'])
            if not compra:
                self.tela.mostra_mensagem_erro('Não existe compra com este ID.')
                continue
            
            if novos_dados['chassi'] != ' ':
                veiculo = self.controlador_principal.controlador_veiculo.busca_veiculo_por_chassi(novos_dados['chassi'])
                if not veiculo:
                    self.tela.mostra_mensagem_erro("Veículo não encontrado com este chassi.")
                    continue
                compra.veiculo = veiculo
            
            if novos_dados['cnpj_fornecedor'] != ' ':
                fornecedor = self.controlador_principal.controlador_fornecedor.busca_fornecedor_por_cnpj(novos_dados['cnpj_fornecedor'])
                if not fornecedor:
                    self.tela.mostra_mensagem_erro("Fornecedor não encontrado com este CNPJ.")
                    continue
                compra.fornecedor = fornecedor
            
            if novos_dados['valor'] != ' ':
                compra.valor = novos_dados['valor']
            
            if novos_dados['data'] != ' ':
                compra.data = novos_dados['data']
            
            self.controlador_principal.loja.compra_dao.update(compra)
            self.tela.mostra_mensagem('Compra alterada.')
            return compra
    
    def deleta_compra(self):
        while True:
            id_compra = self.tela.mostra_tela_deletar()
            if not id_compra:
                return None
            
            compra = self.busca_compra_por_id(id_compra)
            if not compra:
                self.tela.mostra_mensagem_erro("Não existe compra com este ID.")
                continue
            
            estoque = self.controlador_principal.loja.veiculos_em_estoque_dao.get_all()
            if compra.veiculo.chassi in [v.chassi for v in estoque]:
                self.controlador_principal.loja.veiculos_em_estoque_dao.remove(compra.veiculo.chassi)
            
            removido_com_sucesso = self.deleta_compra_por_objeto(compra)
            if removido_com_sucesso:
                self.tela.mostra_mensagem('Compra deletada e veículo removido do estoque.')
                return True
            else:
                self.tela.mostra_mensagem_erro('Erro ao deletar compra.')
                return False
    
    def deleta_compra_por_objeto(self, compra_para_deletar: Compra):
        if compra_para_deletar and isinstance(compra_para_deletar, Compra):
            self.controlador_principal.loja.compra_dao.remove(compra_para_deletar.id)
            return True
        return False
    
    def busca_compra_por_id(self, id_compra):
        if not id_compra:
            return None
        return self.controlador_principal.loja.compra_dao.get(id_compra)
    
    def busca_compras_por_fornecedor(self):
        while True:
            cnpj_fornecedor = self.tela.mostra_tela_busca_fornecedor()
            if not cnpj_fornecedor:
                return None
            compras_fornecedor = [t for t in self.controlador_principal.loja.compra_dao.get_all()
                                  if t.fornecedor.cnpj == cnpj_fornecedor]
            
            if not compras_fornecedor:
                self.tela.mostra_mensagem_erro("Nenhuma compra encontrada para este fornecedor.")
                continue
            
            self.tela.mostra_tela_lista(compras_fornecedor)
            return compras_fornecedor
