from collections import defaultdict

class GeradorDeRelatorios:
    def __init__(self, controlador_relatorios):
        self.__controlador_relatorios = controlador_relatorios

    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios
    
    def processa_dados_servicos_por_mes(self, loja):
        contagem_servicos = defaultdict(lambda: defaultdict(int))
        for servico in loja.servicos_prestados:
            chave_mes = servico.data.strftime('%Y-%m')
            nome_servico = servico.tipo_servico.nome
            contagem_servicos[chave_mes][nome_servico] += 1
        
        return {mes: dict(contagens) for mes, contagens in contagem_servicos.items()}