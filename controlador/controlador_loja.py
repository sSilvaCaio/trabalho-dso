from entidade.loja import Loja
from limite.tela_loja import TelaLoja
from excecoes.lojaNaoEncontradaException import LojaNaoEncontradaException


class ControladorLoja:
    def __init__(self):
        self.__lojas = []
        self.__tela_loja = TelaLoja(self)
    
    def busca_loja_por_cnpj(self, cnpj):
        for loja in self.__lojas:
            if loja.cnpj == cnpj:
                return loja
        else:
            raise LojaNaoEncontradaException
    
    def inicia(self):
        self.__tela_loja.mostra_tela_inicial()
    
    def cadastra_loja(self):
        try:
            dados_loja = self.__tela_loja.mostra_tela_cadastro()
            
            try:
                self.busca_loja_por_cnpj(dados_loja['cnpj'])
                self.__tela_loja.mostra_mensagem("ERRO: Já existe uma loja com este CNPJ!")
                return None
            except LojaNaoEncontradaException:
                pass
            
            nova_loja = Loja(
                dados_loja["nome"],
                dados_loja["cnpj"],
                dados_loja["endereco"]
            )
            self.__lojas.append(nova_loja)
            self.__tela_loja.mostra_mensagem("Loja cadastrada com sucesso!")
            return nova_loja
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def lista_lojas(self):
        if len(self.__lojas) == 0:
            self.__tela_loja.mostra_mensagem("Nenhuma loja cadastrada!")
            return
        
        for loja in self.__lojas:
            dados_loja = {
                "nome": loja.nome,
                "cnpj": loja.cnpj,
                "endereco": loja.endereco,
                "num_veiculos": len(loja.veiculos_em_estoque),
                "num_clientes": len(loja.clientes),
                "num_fornecedores": len(loja.fornecedores),
                "num_servicos": len(loja.servicos_prestados)
            }
            self.__tela_loja.mostra_dados_loja(dados_loja)
    
    def altera_loja(self):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            novos_dados = self.__tela_loja.mostra_tela_alteracao()
            
            if novos_dados["nome"]:
                loja.nome = novos_dados["nome"]
            if novos_dados["cnpj"]:
                loja.cnpj = novos_dados["cnpj"]
            if novos_dados["endereco"]:
                loja.endereco = novos_dados["endereco"]
            
            self.__tela_loja.mostra_mensagem("Loja alterada com sucesso!")
            return True
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def deleta_loja(self):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            self.__lojas.remove(loja)
            self.__tela_loja.mostra_mensagem("Loja deletada com sucesso!")
            return True
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def abre_tela_opcoes(self):
        switcher = {
            0: 'break',
            1: self.cadastra_loja,
            2: self.lista_lojas,
            3: self.altera_loja,
            4: self.deleta_loja,
            5: self.abre_tela_informacoes_loja,
            6: self.veiculos_em_estoque
        }
        
        while True:
            opcao = self.__tela_loja.mostra_tela_opcoes()
            funcao_escolhida = switcher.get(opcao)
            
            if funcao_escolhida == 'break':
                break
            elif funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_loja.mostra_mensagem("Opção inválida!")
    
    def abre_tela_informacoes_loja(self):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            dados_loja = {
                "nome": loja.nome,
                "cnpj": loja.cnpj,
                "endereco": loja.endereco,
                "num_veiculos": len(loja.veiculos_em_estoque),
                "num_clientes": len(loja.clientes),
                "num_fornecedores": len(loja.fornecedores),
                "num_servicos": len(loja.servicos_prestados)
            }
            self.__tela_loja.mostra_informacoes_completas(dados_loja)
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def veiculos_em_estoque(self):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            if len(loja.veiculos_em_estoque) == 0:
                self.__tela_loja.mostra_mensagem("Nenhum veículo em estoque!")
                return
            
            self.__tela_loja.mostra_mensagem("\n--- VEÍCULOS EM ESTOQUE ---")
            for veiculo in loja.veiculos_em_estoque:
                print(f"Chassi: {veiculo.chassi} | Placa: {veiculo.placa} | Marca: {veiculo.marca} | Ano: {veiculo.ano}")
                
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def realizar_compra(self, veiculo, fornecedor, valor):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            loja.veiculos_em_estoque.append(veiculo)
            
            if fornecedor not in loja.fornecedores:
                loja.fornecedores.append(fornecedor)
            
            self.__tela_loja.mostra_mensagem(f"Compra realizada! Veículo adicionado ao estoque da loja {loja.nome}.")
            return True
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def realizar_venda(self, veiculo, cliente, valor):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            if veiculo not in loja.veiculos_em_estoque:
                self.__tela_loja.mostra_mensagem("ERRO: Veículo não está no estoque desta loja!")
                return False
            
            loja.veiculos_em_estoque.remove(veiculo)
            
            if cliente not in loja.clientes:
                loja.clientes.append(cliente)
            
            self.__tela_loja.mostra_mensagem(f"Venda realizada! Veículo removido do estoque da loja {loja.nome}.")
            return True
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def cadastrar_cliente(self, cliente):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            if cliente not in loja.clientes:
                loja.clientes.append(cliente)
                self.__tela_loja.mostra_mensagem(f"Cliente {cliente.nome} cadastrado na loja com sucesso!")
            else:
                self.__tela_loja.mostra_mensagem("Cliente já está cadastrado nesta loja!")
            return True
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def cadastrar_fornecedor(self, fornecedor):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            if fornecedor not in loja.fornecedores:
                loja.fornecedores.append(fornecedor)
                self.__tela_loja.mostra_mensagem(f"Fornecedor {fornecedor.cnpj} cadastrado na loja com sucesso!")
            else:
                self.__tela_loja.mostra_mensagem("Fornecedor já está cadastrado nesta loja!")
            return True
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def registrar_servico(self, servico):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            loja.servicos_prestados.append(servico)
            self.__tela_loja.mostra_mensagem("Serviço registrado com sucesso!")
            return True
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
    def buscar_veiculo_por_placa(self, placa):
        lojas_encontradas = []
        
        for loja in self.__lojas:
            for veiculo in loja.veiculos_em_estoque:
                if veiculo.placa == placa:
                    lojas_encontradas.append(loja)
                    break
        
        if len(lojas_encontradas) == 0:
            self.__tela_loja.mostra_mensagem("Veículo não encontrado em nenhuma loja!")
            return None
        
        self.__tela_loja.mostra_mensagem(f"\nVeículo com placa {placa} encontrado em:")
        for loja in lojas_encontradas:
            dados_loja = {
                "nome": loja.nome,
                "cnpj": loja.cnpj,
                "endereco": loja.endereco,
                "num_veiculos": len(loja.veiculos_em_estoque),
                "num_clientes": len(loja.clientes),
                "num_fornecedores": len(loja.fornecedores),
                "num_servicos": len(loja.servicos_prestados)
            }
            self.__tela_loja.mostra_dados_loja(dados_loja)
        
        return lojas_encontradas
    
    def buscar_cliente_por_cpf(self, cpf):
        try:
            cnpj = self.__tela_loja.seleciona_loja()
            loja = self.busca_loja_por_cnpj(cnpj)
            
            for cliente in loja.clientes:
                if cliente.cpf == cpf:
                    self.__tela_loja.mostra_mensagem(f"Cliente encontrado: {cliente.nome}")
                    return cliente
            
            self.__tela_loja.mostra_mensagem("Cliente não encontrado nesta loja!")
            return None
            
        except TypeError as e:
            return self.__tela_loja.mostra_mensagem_TypeError(e.args)
        except Exception as e:
            return self.__tela_loja.mostra_mensagem_Exception(e)
    
