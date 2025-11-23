from collections import defaultdict

from entidade.compra import Compra
from entidade.venda import Venda


class GeradorDeRelatorios:
    def __init__(self, controlador_relatorios):
        self.__controlador_relatorios = controlador_relatorios

    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios
    
    def processa_dados_servicos_por_mes(self, loja):
        contagem_servicos = defaultdict(lambda: defaultdict(int))
        for servico in loja.servico_dao.get_all():
            chave_mes = servico.data.strftime('%Y-%m')
            nome_servico = servico.tipo_servico.nome
            contagem_servicos[chave_mes][nome_servico] += 1
        
        return {mes: dict(contagens) for mes, contagens in contagem_servicos.items()}
    
    def processa_dados_veiculos_em_estoque_por_marca(self, loja):
        contagem_veiculos = defaultdict(int)
        for veiculo in loja.veiculo_em_estoque_dao.get_all():
            nome_marca = veiculo.marca.nome
            contagem_veiculos[nome_marca] += 1
        
        return dict(contagem_veiculos)  

    def processa_dados_compras_por_mes(self, loja, ano):
        contagem_compras = defaultdict(lambda: defaultdict(int))
        compras = []
        try:
            compras = loja.compra_dao.get_all()
        except Exception:
            compras = []

        for transacao in compras:
            if isinstance(transacao, Compra) and transacao.data.year == ano:
                chave_mes = transacao.data.strftime('%Y-%m')
                contagem_compras[chave_mes]['quantidade'] += 1
                contagem_compras[chave_mes]['valor_total'] += transacao.valor if transacao.valor else 0.0
        
        return dict(contagem_compras)
    
    def processa_dados_vendas_por_mes(self, loja, ano):
        contagem_vendas = defaultdict(lambda: defaultdict(int))
        vendas = []
        try:
            vendas = loja.venda_dao.get_all()
        except Exception:
            vendas = []

        for transacao in vendas:
            if isinstance(transacao, Venda) and transacao.data.year == ano:
                chave_mes = transacao.data.strftime('%Y-%m')
                contagem_vendas[chave_mes]['quantidade'] += 1
                contagem_vendas[chave_mes]['valor_total'] += transacao.valor if transacao.valor else 0.0
        
        return dict(contagem_vendas)
