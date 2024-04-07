import conexao_sistema


class Gerente:
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def Verificar_Estoque(self, n_paes, n_identificacao_vendedor):
        self.n_paes = n_paes
        self.n_identificacao_vendedor = n_identificacao_vendedor
    
    def Controle_de_Funcionario(self, nome_funcionario, n_identificao_funcionario):
        self.nome_funcionario = nome_funcionario
        self.n_identificacao_vendedor = n_identificao_funcionario