from limite.tela_servico import TelaServico
from entidade.servico import Servico


class ControladorServico:
    def __init__(self, controlador_principal):
        self.__tela = TelaServico(self)
        self.__controlador_principal = controlador_principal
        self.__dao = self.controlador_principal.loja.servico_dao

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def dao(self):
        return self.__dao

    def abre_tela_opcoes(self):
        switcher = {
            1: self.cadastra_servico,
            2: self.lista_servicos,
            3: self.altera_servico,
            4: self.deleta_servico,
        }
        while True:
            opcao = self.tela.mostra_tela_opcoes()
            if opcao == 0:
                break
            funcao = switcher.get(opcao)
            if funcao:
                funcao()
            else:
                self.tela.mostra_mensagem_erro("Opção inválida.")

    def cadastra_servico(self):
        while True:
            dados_servico = self.tela.mostra_tela_cadastro()

            if not dados_servico:
                return None

            veiculo = self.controlador_principal.loja.veiculo_cadastrado_dao.get(
                dados_servico["chassi_veiculo"]
            )

            if not veiculo:
                self.tela.mostra_mensagem_erro(
                    "Não foi encontrado veículo com este chassi"
                )
                continue

            tipo_servico = self.controlador_principal.loja.tipo_servico_dao.get_by_nome(
                dados_servico["tipo_servico"]
            )

            if not tipo_servico:
                self.tela.mostra_mensagem_erro(
                    "Não existe tipo de serviço cadastrado com este nome"
                )
                continue

            novo_servico = Servico(
                tipo_servico, veiculo, dados_servico["valor"], dados_servico["data"]
            )

            sucesso = self.dao.add(novo_servico)
            if sucesso:
                self.tela.mostra_mensagem("Serviço registrado")
                return novo_servico
            else:
                self.tela.mostra_mensagem_erro("Erro ao registrar serviço")
                return False

    def lista_servicos(self):
        servicos = self.dao.get_all()
        servicos_dict = [
            {
                "id": servico.id,
                "tipo_servico": servico.tipo_servico.nome,
                "veiculo": f"{servico.veiculo.marca.nome} - Chassi: {servico.veiculo.chassi}",
                "valor": servico.valor,
                "data": servico.data.strftime("%d/%m/%Y"),
            }
            for servico in servicos
        ]
        self.tela.mostra_tela_lista(servicos_dict)

    def altera_servico(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()

            if not novos_dados:
                return None

            servico = self.dao.get(novos_dados["id"])

            if not servico:
                self.tela.mostra_mensagem_erro("Não existe serviço com este ID.")
                continue

            tipo_servico = None
            if novos_dados["tipo_servico"] != " ":
                tipo_servico = self.controlador_principal.tipo_servico_dao.get_by_nome(
                    novos_dados["tipo_servico"]
                )
                if not tipo_servico:
                    self.tela.mostra_mensagem_erro(
                        "Não existe tipo de serviço cadastrado com este nome"
                    )
                    continue

            veiculo = None
            if novos_dados["chassi"] != " ":
                veiculo = self.controlador_principal.veiculo_dao.get(
                    novos_dados["chassi"]
                )
                if not veiculo:
                    self.tela.mostra_mensagem_erro(
                        "Não foi encontrado veículo com este chassi"
                    )
                    continue

            if tipo_servico:
                servico.tipo_servico = tipo_servico
            if veiculo:
                servico.veiculo = veiculo
            if novos_dados["valor"] != " ":
                servico.valor = novos_dados["valor"]
            if novos_dados["data"] != " ":
                servico.data = novos_dados["data"]

            sucesso = self.dao.update(servico)
            if sucesso:
                self.tela.mostra_mensagem("Serviço alterado.")
                return servico
            else:
                self.tela.mostra_mensagem_erro("Erro ao alterar serviço.")
                return False

    def deleta_servico(self):
        while True:
            id = self.tela.mostra_tela_deletar()

            if not id:
                return None

            servico_para_deletar = self.dao.get(id)

            if not servico_para_deletar:
                self.tela.mostra_mensagem_erro("Não existe serviço com este ID.")
                continue

            sucesso = self.dao.remove(id)
            if sucesso:
                self.tela.mostra_mensagem("Serviço removido.")
                return True
            else:
                self.tela.mostra_mensagem_erro("Erro ao remover serviço.")
                return False
