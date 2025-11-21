from entidade.veiculo import Veiculo
from limite.tela_veiculo import TelaVeiculo


class ControladorVeiculo:
    def __init__(self, controlador_principal):
        self.__tela = TelaVeiculo(self)
        self.__controlador_principal = controlador_principal
        self.__dao_cadastrados = self.controlador_principal.loja.veiculo_cadastrado_dao
        self.__dao_em_estoque = self.controlador_principal.loja.veiculo_em_estoque_dao

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def dao_cadastrados(self):
        return self.__dao_cadastrados

    @property
    def dao_em_estoque(self):
        return self.__dao_em_estoque

    def abre_tela_opcoes(self):
        switcher = {
            1: self.cadastra_veiculo,
            2: self.lista_veiculos_cadastrados,
            3: self.lista_veiculos_em_estoque,
            4: self.altera_veiculo,
            5: self.deleta_veiculo,
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

    def cadastra_veiculo(self):
        while True:
            dados_veiculo = self.tela.mostra_tela_cadastro()

            if not dados_veiculo:
                return None

            if self.dao_cadastrados.get(dados_veiculo["chassi"]):
                self.tela.mostra_mensagem_erro("Já existe um veículo com este chassi!")
                continue

            obj_marca = self.controlador_principal.loja.marca_dao.get_by_nome(
                dados_veiculo["marca"]
            )
            if not obj_marca:
                self.tela.mostra_mensagem_erro(
                    f'A marca "{dados_veiculo["marca"]}" não foi encontrada.'
                )
                continue

            novo_veiculo = Veiculo(
                chassi=dados_veiculo["chassi"],
                ano=dados_veiculo["ano"],
                cor=dados_veiculo["cor"],
                placa=dados_veiculo["placa"],
                potencia=dados_veiculo["potencia"],
                quilometragem=dados_veiculo["quilometragem"],
                marca=obj_marca,
            )

            sucesso = self.dao_cadastrados.add(novo_veiculo)
            if sucesso:
                self.tela.mostra_mensagem("Veículo cadastrado.")
                return True
            else:
                self.tela.mostra_mensagem_erro("Erro ao cadastrar veículo.")
                return False

    def lista_veiculos_cadastrados(self):
        veiculos = self.dao_cadastrados.get_all()
        veiculos_dict = [
            {
                "chassi": veiculo.chassi,
                "ano": veiculo.ano,
                "cor": veiculo.cor,
                "placa": veiculo.placa,
                "potencia": veiculo.motor.potencia,
                "quilometragem": veiculo.motor.quilometragem,
                "marca": veiculo.marca.nome,
            }
            for veiculo in veiculos
        ]
        self.tela.mostra_tela_lista_cadastrados(veiculos_dict)
        return True

    def lista_veiculos_em_estoque(self):
        veiculos = self.dao_em_estoque.get_all()
        veiculos_dict = [
            {
                "chassi": veiculo.chassi,
                "ano": veiculo.ano,
                "cor": veiculo.cor,
                "placa": veiculo.placa,
                "potencia": veiculo.motor.potencia,
                "quilometragem": veiculo.motor.quilometragem,
                "marca": veiculo.marca.nome,
            }
            for veiculo in veiculos
        ]
        self.tela.mostra_tela_lista_em_estoque(veiculos_dict)
        return True

    def deleta_veiculo(self):
        while True:
            chassi = self.tela.mostra_tela_deletar()

            if not chassi:
                return None

            if not self.dao_cadastrados.get(chassi):
                self.tela.mostra_mensagem_erro("Não existe veículo com este chassi.")
                continue

            removido_do_estoque = True
            if self.dao_em_estoque.get(chassi):
                removido_do_estoque = self.dao_em_estoque.remove(chassi)

            removido_com_sucesso = self.dao_cadastrados.remove(chassi)

            if removido_com_sucesso and removido_do_estoque:
                self.tela.mostra_mensagem("Veículo deletado.")
                return True
            else:
                self.tela.mostra_mensagem_erro("Erro ao deletar veículo.")
                return False

    def altera_veiculo(self):
        while True:
            novos_dados = self.tela.mostra_tela_alteracao()
            if not novos_dados:
                return None

            veiculo = self.dao_cadastrados.get(novos_dados["chassi"])

            if not veiculo:
                self.tela.mostra_mensagem_erro("Não existe veículo com este chassi.")
                continue

            obj_marca = None
            if novos_dados["marca"] is not None:
                obj_marca = self.controlador_principal.marca_dao.get_by_nome(
                    novos_dados["marca"]
                )
                if not obj_marca:
                    self.tela.mostra_mensagem_erro(
                        f'A marca "{novos_dados["marca"]}" não foi encontrada.'
                    )
                    continue

            if novos_dados["ano"] is not None:
                veiculo.ano = novos_dados["ano"]
            if novos_dados["cor"] is not None:
                veiculo.cor = novos_dados["cor"]
            if novos_dados["placa"] is not None:
                veiculo.placa = novos_dados["placa"]
            if novos_dados["potencia"] is not None:
                veiculo.motor.potencia = novos_dados["potencia"]
            if novos_dados["quilometragem"] is not None:
                veiculo.motor.quilometragem = novos_dados["quilometragem"]
            if obj_marca:
                veiculo.marca = obj_marca

            ok_cadastrados = self.dao_cadastrados.update(veiculo)
            ok_estoque = True
            if self.dao_em_estoque.get(veiculo.chassi):
                ok_estoque = self.dao_em_estoque.update(veiculo)

            if ok_cadastrados and ok_estoque:
                self.tela.mostra_mensagem("Veículo alterado.")
                return veiculo
            else:
                self.tela.mostra_mensagem_erro("Erro ao alterar veículo.")
                return False
