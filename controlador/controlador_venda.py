from entidade.venda import Venda
from limite.tela_venda import TelaVenda

class ControladorVenda:
    def __init__(self, controlador_principal):
        self.__tela = TelaVenda(self)
        self.__controlador_principal = controlador_principal
    
    @property
    def tela(self):
        return self.__tela
    
    @property
    def controlador_principal(self):
        return self.__controlador_principal
    
    def abre_tela_opcoes(self):
        switcher = {1: self.registra_venda, 2: self.lista_vendas, 3: self.altera_venda, 4: self.deleta_venda}
        
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")
    
    def registra_venda(self):
        while True:
            dados_venda = self.tela.mostra_tela_cadastro()
            if not dados_venda:
                return None
            
            veiculo = self.controlador_principal.controlador_veiculo.busca_veiculo_por_chassi(dados_venda['chassi'])
            if not veiculo:
                self.tela.mostra_mensagem_erro("Veículo não encontrado com este chassi.")
                continue
            
            if veiculo not in self.controlador_principal.loja.veiculos_em_estoque:
                self.tela.mostra_mensagem_erro("Veículo não está no estoque.")
                continue
            
            cliente = self.controlador_principal.controlador_cliente.busca_cliente_por_cpf(dados_venda['cpf_cliente'])
            if not cliente:
                self.tela.mostra_mensagem_erro("Cliente não encontrado com este CPF.")
                continue
            
            nova_venda = Venda(
                veiculo=veiculo,
                valor=dados_venda['valor'],
                cliente=cliente,
                data=dados_venda['data']
            )
            
            self.controlador_principal.loja.transacoes.append(nova_venda)
            self.controlador_principal.loja.veiculos_em_estoque.remove(veiculo)
            
            self.tela.mostra_mensagem("Venda registrada com sucesso!")
            return nova_venda
    
    def lista_vendas(self):
        vendas = [t for t in self.controlador_principal.loja.transacoes if isinstance(t, Venda)]
        if not vendas:
            self.tela.mostra_mensagem("Nenhuma venda registrada.")
            return None
        
        self.tela.mostra_tela_lista(vendas)
    
    def altera_venda(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()
            if not novos_dados:
                return None
            
            venda = self.busca_venda_por_id(novos_dados['id'])
            if not venda:
                self.tela.mostra_mensagem_erro('Não existe venda com este ID.')
                continue
            
            veiculo_antigo = venda.veiculo
            
            if novos_dados['chassi'] != ' ':
                veiculo = self.controlador_principal.controlador_veiculo.busca_veiculo_por_chassi(novos_dados['chassi'])
                if not veiculo:
                    self.tela.mostra_mensagem_erro("Veículo não encontrado com este chassi.")
                    continue
                
                if veiculo not in self.controlador_principal.loja.veiculos_em_estoque:
                    self.tela.mostra_mensagem_erro("Veículo não está no estoque.")
                    continue
                
                if veiculo_antigo not in self.controlador_principal.loja.veiculos_em_estoque:
                    self.controlador_principal.loja.veiculos_em_estoque.append(veiculo_antigo)
                
                self.controlador_principal.loja.veiculos_em_estoque.remove(veiculo)
                venda.veiculo = veiculo
            
            if novos_dados['cpf_cliente'] != ' ':
                cliente = self.controlador_principal.controlador_cliente.busca_cliente_por_cpf(novos_dados['cpf_cliente'])
                if not cliente:
                    self.tela.mostra_mensagem_erro("Cliente não encontrado com este CPF.")
                    continue
                venda.cliente = cliente
            
            if novos_dados['valor'] != ' ':
                venda.valor = novos_dados['valor']
            
            if novos_dados['data'] != ' ':
                venda.data = novos_dados['data']
            
            self.tela.mostra_mensagem('Venda alterada.')
            return venda
    
    def deleta_venda(self):
        while True:
            id_venda = self.tela.mostra_tela_deletar()
            if not id_venda:
                return None
            
            venda = self.busca_venda_por_id(id_venda)
            if not venda:
                self.tela.mostra_mensagem_erro("Não existe venda com este ID.")
                continue
            
            if venda.veiculo not in self.controlador_principal.loja.veiculos_em_estoque:
                self.controlador_principal.loja.veiculos_em_estoque.append(venda.veiculo)
            
            removido_com_sucesso = self.deleta_venda_por_objeto(venda)
            if removido_com_sucesso:
                self.tela.mostra_mensagem('Venda deletada e veículo devolvido ao estoque.')
                return True
            else:
                self.tela.mostra_mensagem_erro('Erro ao deletar venda.')
                return False
    
    def deleta_venda_por_objeto(self, venda_para_deletar: Venda):
        if venda_para_deletar and isinstance(venda_para_deletar, Venda):
            if venda_para_deletar in self.controlador_principal.loja.transacoes:
                self.controlador_principal.loja.transacoes.remove(venda_para_deletar)
                return True
        return False
    
    def busca_venda_por_id(self, id_venda):
        for transacao in self.controlador_principal.loja.transacoes:
            if isinstance(transacao, Venda) and transacao.id == id_venda:
                return transacao
        return None
    
    def busca_vendas_por_cliente(self):
        while True:
            cpf_cliente = self.tela.mostra_tela_busca_cliente()
            if not cpf_cliente:
                return None
            
            vendas_cliente = [t for t in self.controlador_principal.loja.transacoes 
                             if isinstance(t, Venda) and t.cliente.cpf == cpf_cliente]
            
            if not vendas_cliente:
                self.tela.mostra_mensagem_erro("Nenhuma venda encontrada para este cliente.")
                continue
            
            self.tela.mostra_tela_lista(vendas_cliente)
            return vendas_cliente
