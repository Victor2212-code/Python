import conexao_sistema 

class Padeiro:
    def login(self, nome, codigo_identificao):
        self.nome = nome
        self.codigo_identificacao = codigo_identificao
        print(nome, codigo_identificao)
    
    def Registrar_Estoque(self, qtd_paes):
        self.qtd_paes = qtd_paes
    