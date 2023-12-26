import mysql.connector
import pandas as pd

class ConexaoBanco:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Victorhug2212@',
            database='escola'
        )
        self.cursor = self.conexao.cursor()


    def encerrar_conexao(self):
            if self.conexao.is_connected():
                self.cursor.close()
                self.conexao.close()
            

class Diretor:
    def __init__(self, conexao):
        self.conexao = conexao
        
        
    def registrar_seretaria(self, nome, matricula):
        try:
            query = "INSERT INTO secretaria(matricula, nome) VALUES(%s, %s)"
            self.conexao.cursor.execute(query,(matricula, nome))
            self.conexao.conexao.commmit()
            print("Secretaria registrada com sucesso!.")
        except mysql.connector.Error as err:
            print(f"Erro ao matricular secretária: {err}.")

    def imprimir_tabela(self, nome_tabela):
        try:
            consulta_colunas = f"SHOW COLUMNS FROM {nome_tabela}"
            self.conexao.cursor.execute(consulta_colunas)
            
            colunas = [coluna[0] for coluna in self.conexao.cursor.fetchall()]
            
            consulta = f"SELECT * FROM {nome_tabela}"
            self.conexao.cursor.execute(consulta)
            dados = self.conexao.cursor.fetchall()
            
            df = pd.DataFrame(dados, columns=colunas)
            print(df.to_string(index=False))
        except mysql.connector.Error as err:
            print(f"Erro ao imprimir tabela: {err}")
        finally:
            if 'conexao' in locals():
                conexao.close()


class Secretaria:
    def __init__(self, conexao):
        self.conexao = conexao

    def matricular_aluno(self, nome, matricula, sala):
        try:
            query = "INSERT INTO aluno(matricula, nome, sala) VALUES (%s, %s, %s)"
            self.conexao.cursor.execute(query, (matricula, nome, sala))
            self.conexao.conexao.commit()
            print("Aluno matriculado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir aluno: {err}")
            
    def registrar_professor(self, nome, matricula, materia_exercida):
        try:
            query = "INSERT INTO professor(matricula, nome, materia_exercida) VALUES (%s, %s, %s)"
            self.conexao.cursor.execute(query, (matricula, nome, materia_exercida))
            self.conexao.conexao.commit()
            print("Professor registrado com sucesso!.")
        except mysql.connector.Error as err:
            print(f"Erro ao tentar registrar professor: {err}.")
            
    def deletar_aluno(self, matricula):
        try:
            query = "DELETE FROM aluno WHERE matricula = %s"
            self.conexao.cursor.execute(query, (matricula, ))
            self.conexao.conexao.commit()
            print("Aluno desmatriculado com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar aluno: {err}.")    
                    
                    
    def deletar_professor(self, matricula):
        try:
            query = "DELETE FROM professor WHERE matricula = %s"
            self.conexao.cursor.execute(query, (matricula,))
            self.conexao.conexao.commit()
            print("Professor apagado dos registros.")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar professor: {err}")
            
    def adicionar_materia(self, nome, codigo):
        try:
            query = "INSERT INTO materias(nome, codigo_materia) VALUES (%s, %s)"
            self.conexao.cursor.execute(query, (nome, codigo))
            self.conexao.conexao.commit()
            print("Matéria adicionada com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar a matéria. {err}")
            
            
    def adicionar_sala(self, numero_sala):
        try:
            query = "INSERT INTO sala(idsala) VALUES (%s)"
            self.conexao.cursor.execute(query, (numero_sala, ))
            self.conexao.conexao.commit()
            print("Sala registrada com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao registrar sala: {err}")
            
    def deletar_materia(self, codigo_materia):
        try:
            query = "DELETE FROM materias WHERE codigo_materia = %s"
            self.conexao.cursor.execute(query, (codigo_materia, ))
            self.conexao.conexao.commit()
            print("Matéria deletada com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar matéria: {err}")
            
    def registrar_funcionario(self, usuario, senha, matricula, tipo_usuario):
        try:
            query = "INSERT INTO senhas(usuario, senha, matricula, tipo_usuario) VALUES (%s, %s, %s, %s)"
            self.conexao.cursor.execute(query, (usuario, senha, matricula, tipo_usuario))
            self.conexao.conexao.commit()
            print("Usuário registrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao tentar registrar usuário: {err}")               

class Professor:
    def __init__(self, conexao):
        self.conexao = conexao

    def login(self, nome, usuario, senha):
        try:
            query = "SELECT usuario, senha FROM professor WHERE nome = %s"
            self.conexao.cursor.execute(query, (nome,))
            resultado = self.conexao.cursor.fetchone()

            if resultado:
                db_usuario, db_senha = resultado
                if usuario == db_usuario and senha == db_senha:
                    print("Login bem-sucedido!")
                else:
                    print("Usuário ou senha incorretos.")
            else:
                print("Professor não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao acessar a tabela: {err}")
            
class Aluno:
    def __init__(self, conexao):
        self.conexao = conexao

conexao = ConexaoBanco()

opcao = int(input("Qual é seu tipo de usuário [1] Secretário(a), [2] Professor, [3] Diretor, [4] Aluno: "))

if opcao == 1:
    secretaria = Secretaria(conexao)
    print("--------Bem-vindo Secretário(a)------------")
    opcao_operacao = int(input("Qual operação deseja fazer "
                            "[1]Matricular Aluno,"
                            "[2]Registrar Professor,"
                            "[3] Desmatricular Aluno"
                            ",[4] Deletar registro do Professor, [5] Registrar Matéria, [6] Registrar sala, [7]Deletar Matéria, [8] Registrar acesso dos funcionários:   "))
    
    if opcao_operacao == 1:
            print("--Para matricular um aluno basta colocar o nome, matricula, sala")
            nome_aluno = input("Nome: ")
            matricula_aluno = input("Matrícula: ")
            sala_aluno = int(input("Sala: "))
            secretaria.matricular_aluno(nome_aluno, matricula_aluno, sala_aluno)
            
    elif opcao_operacao == 2:
        print("---Para registrar um Professor basta colocar nome, matricula, código da materia exercida---")
        nome_professor = input("Nome: ")
        matricula_professor = input("Matricula: ")
        materia_exercida = input("Materia Exercida: ")
        secretaria.registrar_professor(nome_professor, matricula_professor, materia_exercida)
        
    elif opcao_operacao == 3:
        print("-----Para desmatricular um aluno basta colocar sua matrícula-----")
        matricula_aluno = input("Digite a Matrícula: ")
        secretaria.deletar_aluno(matricula_aluno)
        
    elif opcao_operacao == 4:
        print("------Para deletar um professor basta colocar a  sua matrícula-----")
        matricula_professor = input("Digite a matrícula: ")
        secretaria.deletar_professor(matricula_professor)
        
    elif opcao_operacao == 5:
        print("----Para adicionar uma matéria, basta colocar o nome e o código----")
        nome_materia = input("Nome da Máteria: ")
        codigo_materia = int(input("Código: "))
        secretaria.adicionar_materia(nome_materia, codigo_materia)
        
    
    elif opcao_operacao == 6:
        print("------Para registrar uma sala basta colocar o número da sala------")
        numero_sala =int(input("Número da sala: "))
        secretaria.adicionar_sala(numero_sala)
        
    elif opcao_operacao == 7:
        print("----Para deletar uma matéria basta fornecer o código----")
        codigo_materia = int(input("Código: "))
        secretaria.deletar_materia(codigo_materia)   
        
        
    elif opcao_operacao == 8:
        print("------Para registrar um funcionário, basta digitar o usuario, senha, colocar a matrícula da pessoa, também é necessário colocar o tipo de usuário------")
        print("[1]Diretor, [2]Secretario(a), [3]Professor, [4]Aluno")
        usuario_funcionario = input("Digite o usuário: ")
        senha_funcionario = input("Senha do usuário: ")
        nome_usuario = input("Matrícula do usuário: ")
        codigo_usuario = int(input("Digite o código: "))
        secretaria.registrar_funcionario(usuario_funcionario, senha_funcionario, nome_usuario, codigo_usuario)
         
elif opcao == 2:
    professor = Professor(conexao)
    
    
elif opcao == 3:
    diretor = Diretor(conexao)
    opcao_operacao = int(input("[1] Registrar Secretário(a), [2] Ver Lista de Alunos matriculados, [3] Ver Lista de Professores : "))
    
    if opcao_operacao == 1:
        print("---Para fazer o registro do(a) secretário(a), basta colocar o nome e a matricula.")
        nome = input("Digite o nome: ")
        matricula = input("Digite a Matrícula: ")
        diretor.registrar_seretaria(nome, matricula)
        
    elif opcao_operacao == 2:
        diretor.imprimir_tabela('escola.aluno')
        
    elif opcao_operacao == 3:
        diretor.imprimir_tabela('escola.professor')
    
    
elif opcao == 4:
    aluno = Aluno(conexao)

conexao.encerrar_conexao()