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
        try:
            if self.conexao.is_connected():
                self.cursor.close()
                self.conexao.close()
        except mysql.connector.Error as err:
            print(f"Erro ao tentar encerrar a conexão: {err}")        
            

class Administrador:
    def __init__(self, conexao):
          self.conexao = conexao
          
    def login_administrador(self, usuario, senha):
        try:
                query = 'SELECT matricula FROM senhas WHERE usuario = %s AND senha = %s'
                self.conexao.cursor.execute(query, (usuario, senha))
                
                info_administrador = self.conexao.cursor.fetchone()
                
                if info_administrador:
                    codigo_administrador = info_administrador[0]
                    
                    query_info = 'SELECT nome, codigo_autorizacao FROM administrador WHERE codigo_autorizacao = %s'
                    self.conexao.cursor.execute(query_info,(codigo_administrador,))
                    
                    resultado_info = self.conexao.cursor.fetchone()
                    
                    if resultado_info:
                        nome_administrador = resultado_info[0]
                        codigo_autorizacao = resultado_info[1]
                        print("Login bem-sucedido!")
                        print("------------Bem-vindo Administrador(a)--------")
                        print(f"Informações do Administrador - Nome: {nome_administrador}, Código: {codigo_autorizacao}")
                        
                        opcao_operacao = input("Qual operação deseja fazer [1]Registrar novo administrador, [2] Registrar diretor [3] registrar acesso de usuários, [4] Apagar acesso: ")
                        
                        
                        if opcao_operacao == '1':
                            print("------Para registrar um novo administrador-----")
                            nome_administrador = input("Usuário:  ")
                            codigo_autorizacao = input("Senha: ")
                            administrador.registrar_novo_administrador(nome_administrador, codigo_autorizacao)
                            
                        elif opcao_operacao == '2':
                            print("------Para registrar o diretor, basta  colocar matricula, nome--------")
                            matricula_diretor = input("Matricula: ")
                            nome_diretor = input("Nome: ")
                            administrador.registrar_diretor(matricula_diretor, nome_diretor)
                        
                        elif opcao_operacao == '3':
                            print("------Para registrar um funcionário, basta digitar o usuario, senha, colocar a matrícula da pessoa, também é necessário colocar o tipo de usuário------")
                            print("[1]Diretor, [2]Secretario(a), [3]Professor, [4]Aluno")
                            usuario_funcionario = input("Digite o usuário: ")
                            senha_funcionario = input("Senha do usuário: ")
                            matricula_usuario = input("Matrícula do usuário: ")
                            codigo_usuario = int(input("Digite o código: "))
                            administrador.registrar_usuario(usuario_funcionario, senha_funcionario, matricula_usuario, codigo_usuario)
                                
                        elif opcao_operacao == '4':
                                print("----Para apagar o acesso de um funcionário basta colocar o usuario e a matricula-----")
                                usuario_funcionario = input("Digite o usuário: ")
                                matricula_usuario = input("Digite a matricúla: ")
                                administrador.apagar_acesso(usuario_funcionario, matricula_usuario)
                    
                        else:
                            print("Digite uma opção válida.")     
                    else:
                        print("Erro ao tentar logar!")  
                         
        except mysql.connector.Error as err:
            print(f"Erro ao tentar apagar acesso do usuário: {err}")
         
             
    def registrar_novo_administrador(self, nome, codigo_autorizacao):
        try: 
            query = "INSERT INTO administrador(nome, codigo_autorizacao) VALUES (%s, %s)"
            self.conexao.cursor.execute(query, (nome, codigo_autorizacao))
            self.conexao.conexao.commit()
            print("Administrador registrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao tentar registrar administrador: {err}")
            
            
            
    def registrar_diretor(self, matricula, nome):
        try:
            query = "INSERT INTO diretor(Matricula, Nome) VALUES (%s, %s)"
            self.conexao.cursor.execute(query, (matricula, nome,))
            self.conexao.conexao.commit()
            print("Diretor registrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao tentar registrar diretor: {err}")
       
        
    def registrar_usuario(self, usuario, senha, matricula, tipo_usuario):
        try:
            query = "INSERT INTO senhas(usuario, senha, matricula, tipo_usuario) VALUES (%s, %s, %s, %s)"
            self.conexao.cursor.execute(query, (usuario, senha, matricula, tipo_usuario))
            self.conexao.conexao.commit()
            print("Usuário registrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar usuário: {err}")
       
            
    def apagar_acesso(self, usuario, matricula):
        try:
            query = "DELETE FROM senhas WHERE usuario = %s AND matricula = %s"
            self.conexao.cursor.execute(query, (usuario, matricula))
            self.conexao.conexao.commit()
            print("Usuário apagado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao tentar apagar o usuário: {err}")


class Diretor:
    def __init__(self, conexao):
        self.conexao = conexao
        
    def login_diretor(self, usuario, senha):
            try:
                query = 'SELECT matricula FROM senhas WHERE usuario = %s AND senha = %s'
                self.conexao.cursor.execute(query, (usuario, senha))
                
                resultado = self.conexao.cursor.fetchone()
           
                if resultado:
                    matricula = resultado[0]
                    query_info = 'SELECT matricula, nome FROM diretor WHERE matricula = %s'
                    self.conexao.cursor.execute(query_info, (matricula, ))  
                    
                    info_diretor = self.conexao.cursor.fetchone()
                    
               
                    if info_diretor:
                        matricula_diretor = info_diretor[0]
                        nome_diretor = info_diretor[1]
                        print("Login bem-sucedido!")
                        print(f"Olá senhor(a) {nome_diretor}, matrícula: {matricula_diretor}")
                        
                        print("-------------Bem-vindo Diretor(a)--------")
                        
                        
                        opcao_operacao = int(input("[1] Registrar Secretário(a)[2] Ver Lista de Alunos matriculados,[3] Ver Lista de Professores : "))
                
                    
                        if opcao_operacao == 1:
                            print("---Para fazer o registro do(a) secretário(a), basta colocar o nome e a matricula.")
                            nome = input("Digite o nome: ")
                            matricula = input("Digite a Matrícula: ")
                            diretor.registrar_seretaria(nome, matricula)
                            
                        elif opcao_operacao == 2:
                            diretor.imprimir_tabela('escola.aluno')
                            
                        elif opcao_operacao == 3:
                            diretor.imprimir_tabela('escola.professor')
                    else:
                        print("Usuário ou senha incorretos.")
            except mysql.connector.Error as err:
                print(f"Não foi possível fazer o login: {err}")                
        
    def registrar_seretaria(self, nome, matricula):
        try:
            query = "INSERT INTO secretaria(matricula, nome) VALUES(%s, %s)"
            self.conexao.cursor.execute(query,(matricula, nome))
            self.conexao.conexao.commit()
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
        
    def login_secretaria(self, usuario, senha):
        try:
            query = 'SELECT matricula FROM senhas WHERE usuario = %s AND senha = %s'
            self.conexao.cursor.execute(query, (usuario, senha))
            
            resultado = self.conexao.cursor.fetchone()
            
            if resultado:
                matricula = resultado[0]
                query_info = 'SELECT matricula, nome FROM secretaria WHERE matricula = %s'
                self.conexao.cursor.execute(query_info, (matricula, ))
                
                info_secretaria = self.conexao.cursor.fetchone()
                
                if info_secretaria:
                    matricula_secretaria = info_secretaria[0]
                    nome_secretaria = info_secretaria[1]
                    print("Login bem-sucedido!")
                    print(f"Informações do(a) secretario(a) - Nome: {nome_secretaria}, Matricula: {matricula_secretaria}")    
                    
                    print("--------Bem-vindo Secretário(a)------------")
                    opcao_operacao = int(input("Qual operação deseja fazer "
                                            "[1]Matricular Aluno,"
                                            "[2]Registrar Professor,"
                                            "[3] Desmatricular Aluno"
                                            ",[4] Deletar registro do Professor, [5] Registrar Matéria, [6]Deletar Matéria, [7] Adicionar aula ao dia da semana:   "))
                    
                    if opcao_operacao == 1:
                            print("--Para matricular um aluno basta colocar o nome, matricula, semestre--")
                            nome_aluno = input("Nome: ")
                            matricula_aluno = input("Matrícula: ")
                            semestre_aluno = input("Semestre: ")
                            secretaria.matricular_aluno(nome_aluno, matricula_aluno, semestre_aluno)
                            
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
                        print("----Para deletar uma matéria basta fornecer o código----")
                        codigo_materia = int(input("Código: "))
                        secretaria.deletar_materia(codigo_materia)   
                        
                        
                    elif opcao_operacao == 7:
                        print("----Para adicionar uma aula ao dia da semana, basta colocar o nome da aula e o nome do professor-----")
                        nome_materia = input("Nome aula: ")
                        nome_professor = input("Nome do Professor: ")
                        secretaria.adicionar_aula_na_semana(nome_materia, nome_professor)
                        
                    else:
                        print("Digite um número válido.")
        except mysql.connector.Error as err: 
            print(f"Erro ao tentar logar: {err}")       

    def matricular_aluno(self, nome, matricula, semestre):
        try:
            query = "INSERT INTO aluno(matricula, nome, semestre) VALUES (%s, %s, %s)"
            self.conexao.cursor.execute(query, (matricula, nome, semestre))
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
            
            
    def deletar_materia(self, codigo_materia):
        try:
            query = "DELETE FROM materias WHERE codigo_materia = %s"
            self.conexao.cursor.execute(query, (codigo_materia, ))
            self.conexao.conexao.commit()
            print("Matéria deletada com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar matéria: {err}")
               
                 
    
    def adicionar_aula_na_semana(self, nome_materia, nome_professor):
        
        semestre = input("Qual é o semestre que você quer adicionar aula [1]primeiro semestre, [2] segundo semestre, [3] terceiro semestre: ")
        # continuar quando chegar da igreja.
        opcao = input("Escolha qual dia deseja adicionar a aula [1] Segunda-Feira, [2] Terça-Feira, [3]Quarta-Feira, [4]Quinta-Feira, [5] Sexta-Feira, [6] Sábado: ")
        
        try:
            if semestre == '1':
                tabela_semestre = "primeiro_semestre"
            elif semestre == '2':
                tabela_semestre = "segundo_semestre"
            elif semestre == '3':
                tabela_semestre = "terceiro_semestre"
            
            
            if opcao == '1':
                query = f"INSERT INTO {tabela_semestre}_segunda_feira(professores, materias) VALUES (%s, %s)"
            elif opcao == '2':
                query = f"INSERT INTO {tabela_semestre}_terca_feira(professores, materias) VALUES (%s, %s)"
            elif opcao == '3':
                query = f"INSERT INTO {tabela_semestre}_quarta_feira(professores, materias) VALUES (%s, %s)"
                
            elif opcao == '4':
                query = f"INSERT INTO {tabela_semestre}_quinta_feira(professores, materias) VALUES (%s, %s)"
                 
            elif opcao == '5':
                query = f"INSERT INTO {tabela_semestre}_sexta_feira(professores, materias) VALUES (%s, %s)"       
                
            elif opcao == '6':
                query = f"INSERT INTO {tabela_semestre}_sabado(professores, materias) VALUES (%s, %s)"
                    
            self.conexao.cursor.execute(query,(nome_professor, nome_materia,))
            self.conexao.conexao.commit()
            print("Aula adicionada com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar aula: {err}")   
        
    
class Professor:
    def __init__(self, conexao):
        self.conexao = conexao

    def login_professor(self, usuario, senha):
        
            try:
                query = 'SELECT matricula FROM senhas WHERE usuario = %s AND senha = %s'
                self.conexao.cursor.execute(query, (usuario, senha))

                resultado = self.conexao.cursor.fetchone()

                if resultado:
                    matricula = resultado[0]

                    query_info = 'SELECT * FROM professor WHERE matricula = %s'
                    self.conexao.cursor.execute(query_info, (matricula, ))
                    
                    info_professor = self.conexao.cursor.fetchone()
                    

                    if info_professor:
                        matricula_professor = info_professor[0]
                        nome_professor = info_professor[1]
                        materia_exercida = info_professor[2]
                        print("Login bem-sucedido!")
                        print(f"Informações Professor - Nome: {nome_professor}, Matricula: {matricula_professor}")
                        opcao_operacao = int(input("Escolha uma operação para fazer [1] Visualizar aulas, [2] Lançar as notas dos alunos, [3] Apagar notas: "))

                        if opcao_operacao == 1:
                            semestre = input("Qual o semestre que você deseja vizualizar as aulas digite apenas por extenso Primeiro semestre, Segundo semestre, Terceiro Semestre: ")
                            
                            opcao = input('Qual o dia que você deseja saber [1]Segunda-Feira, [2]Terca-Feira, [3]Quarta-Feira, [4]Quinta-Feira, [5]Sexta-Feira, [6]Sábado: ')

                            semestre_dias = {
                                'Primeiro semestre': 'primeiro_semestre',
                                'Segundo semestre': 'segundo_semestre',
                                'Terceiro semestre': 'terceiro_semestre'
                            }
                            
                            dia_semana = {
                                '1': 'segunda_feira',
                                '2': 'terca_feira',
                                '3': 'quarta_feira',
                                '4': 'quinta_feira',
                                '5': 'sexta_feira',
                                '6': 'sabado'
                            }


                            if semestre in semestre_dias and opcao in dia_semana:
                                semestre_nome = semestre_dias[semestre]
                                dia_nome = dia_semana[opcao]

                                # Constrói a consulta SQL substituindo os placeholders pelos valores correspondentes
                                query = f'SELECT * FROM escola.{semestre_nome}_{dia_nome} WHERE professores = %s'

                                # Executa a consulta
                                self.conexao.cursor.execute(query, (nome_professor,))
                                
                                # Obtém os resultados da consulta
                                resultados = self.conexao.cursor.fetchall()

                                print("Lista de Aulas: ")
                                for resultado in resultados:
                                    aulas_dadas = resultado[1]  # Acessa a primeira coluna da linha atual
                                    print(aulas_dadas)
                                    
                        elif opcao_operacao == 2:
                            matricula_aluno = input("Matricula aluno: ")
                            primeira_nota = int(input("Primeira nota: "))
                            segunda_nota = int(input("Segunda nota: "))
                            terceira_nota = int(input("Terceira nota: "))
                            opcao_operacao = input("Deseja adicionar outra nota [1]sim, [2]não: ")
                            if opcao_operacao == '1':
                                quarta_nota =int(input("Quarta nota: "))
                                
                                query = "SELECT nome, codigo_materia FROM materias WHERE codigo_materia = %s "
                                self.conexao.cursor.execute(query, (materia_exercida,))
                                
                                resultado = self.conexao.cursor.fetchone()
                                
                                if resultado:
                                    materia_exercida = resultado[0]
                                    operacao_notas = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
                                    formatacao_notas = "{:.2f}".format(operacao_notas)
                                    query_info = "SELECT * FROM aluno WHERE matricula = %s"
                                    
                                    self.conexao.cursor.execute(query_info, (matricula_aluno,))
                                    
                                    resultados = self.conexao.cursor.fetchone()
                                    
                                    if resultados:
                                        try:
                                            semestre_aluno = resultados[2]
                                            query = "INSERT INTO notas_alunos(materia, semestre, matricula, notas) VALUES (%s, %s, %s, %s)"
                                            self.conexao.cursor.execute(query, (materia_exercida, semestre_aluno, matricula_aluno, formatacao_notas))
                                            self.conexao.conexao.commit()
                                            print("Nota adicionada com sucesso!")
                                        except mysql.connector.Error as err:
                                            print(f"Erro ao tentar adicionar aula: {err}")
                                
                                opcao = input("Deseja inserir outra nota [1] sim, [2] não:")
                                
                                if opcao == '1':
                                    quinta_nota = int(input("Quinta nota: "))
                                    
                                    materia_exercida = resultado[0]
                                    operacao_notas = (primeira_nota + segunda_nota + terceira_nota + quarta_nota + quinta_nota) / 5
                                    formatacao_notas = "{:.2f}".format(operacao_notas)
                                    query_info = "SELECT * FROM aluno WHERE matricula = %s"
                                    
                                    self.conexao.cursor.execute(query_info, (matricula_aluno,))
                                    
                                    resultados = self.conexao.cursor.fetchone()
                                    
                                    if resultados:
                                        try:
                                            semestre_aluno = resultados[2]
                                            query = "INSERT INTO notas_alunos(materia, semestre, matricula, notas) VALUES (%s, %s, %s, %s)"
                                            self.conexao.cursor.execute(query, (materia_exercida, semestre_aluno, matricula_aluno, formatacao_notas))
                                            self.conexao.conexao.commit()
                                            print("Nota adicionada com sucesso!")
                                        except mysql.connector.Error as err:
                                            print(f"Erro ao tentar adicionar aula: {err}")
                                else:
                                    print(f"Notas: {operacao_notas}")
                                    
                            elif opcao_operacao == '2':
                                query = "SELECT nome, codigo_materia FROM materias WHERE codigo_materia = %s "
                                self.conexao.cursor.execute(query, (materia_exercida,))
                                
                                resultado = self.conexao.cursor.fetchone()
                                
                                if resultado:
                                    materia_exercida = resultado[0]
                                    operacao_notas = (primeira_nota + segunda_nota + terceira_nota) / 3
                                    formatacao_notas = "{:.2f}".format(operacao_notas)
                                    query_info = "SELECT * FROM aluno WHERE matricula = %s"
                                    
                                    self.conexao.cursor.execute(query_info, (matricula_aluno,))
                                    
                                    resultados = self.conexao.cursor.fetchone()
                                    
                                    if resultados:
                                        try:
                                            semestre_aluno = resultados[2]
                                            query = "INSERT INTO notas_alunos(materia, semestre, matricula, notas) VALUES (%s, %s, %s, %s)"
                                            self.conexao.cursor.execute(query, (materia_exercida, semestre_aluno, matricula_aluno, formatacao_notas))
                                            self.conexao.conexao.commit()
                                            print("Nota adicionada com sucesso!")
                                        except mysql.connector.Error as err:
                                            print(f"Erro ao tentar adicionar aula: {err}")
                                
                            else:
                                print("Opção inválida.")
                                
                        elif opcao_operacao == 3:
                            print("----Para apagar um nota basta digitar o nome da máteria e a nota do aluno-----")
                            nome_materia = input("Nome matéria: ")
                            nota_aluno = input("Nota aluno: ")
                            try:
                                query = "DELETE FROM notas_alunos WHERE materia = %s AND notas = %s"
                                self.conexao.cursor.execute(query, (nome_materia, nota_aluno,))
                                self.conexao.conexao.commit()
                                print("Nota deletada com sucesso!.")
                            except mysql.connector.Error as err:
                                print(f"Erro ao tentar deletar nota: {err}")
                            
                    else:
                        return "Matrícula não encontrada para este professor"
                else:
                    return "Usuário ou senha incorretos"

            except mysql.connector.Error as err:
                print(f"Erro ao obter informações do professor: {err}") 
            
class Aluno:
    def __init__(self, conexao):
        self.conexao = conexao
        
    def login_aluno(self, usuario, senha):
        query = 'SELECT * FROM senhas WHERE usuario = %s AND senha = %s'
        self.conexao.cursor.execute(query, (usuario, senha,))
        
        resultado = self.conexao.cursor.fetchone()
        
        if resultado:
            matricula = resultado[2]  # Supondo que a matrícula esteja no segundo campo retornado pela consulta
            print("Login bem-sucedido!")
            
            # Agora que temos a matrícula, buscamos as informações do aluno
            query_info = 'SELECT nome, semestre FROM aluno WHERE matricula = %s'
            self.conexao.cursor.execute(query_info, (matricula,))
            
            resultado_info = self.conexao.cursor.fetchone()
            
            if resultado_info:
                nome = resultado_info[0]  
                semestre_aluno= resultado_info[1]  
                
                print(f"Informações do aluno - Nome: {nome}, Matricula: {matricula}, Semestre: {semestre_aluno}")
                print('-'*50)
                opcao_operacao = input("Qual operação deseja fazer [1] Ver Aulas, [2] Ver a lista de professores,  [3] Ver lista de matérias, [4] Ver notas: ")
                if opcao_operacao == '1':
                    opcao = input("Qual dia você deseja vizualizar [1] Segunda-Feira, [2] Terça-Feira, [3] Quarta-Feira, [4] Quinta-Feira, [5] Sexta-Feira, [7] Sábado: ")
                    
                    if opcao == '1':
                        print("-------Segunda-Feira-------")
                        aluno.imprimir_tabela(f"escola.{semestre_aluno}_semestre_segunda_feira")
                    
                    
                    if opcao == '2':
                        print("-------Terça-Feira--------")
                        aluno.imprimir_tabela(f'escola.{semestre_aluno}_semestre_terca_feira')
                    
                    if opcao == '3':
                        print("-------Quarta-Feira--------")
                        aluno.imprimir_tabela(f'escola.{semestre_aluno}_semestre_quarta_feira')
                
                    if opcao == '4':
                        print("-------Quinta-Feira--------")
                        aluno.imprimir_tabela(f'escola.{semestre_aluno}_semestre_quinta_feira')
                    
                    if opcao == '5':
                        print("-------Sexta-Feira---------")
                        aluno.imprimir_tabela(f'escola.{semestre_aluno}_semestre_sexta_feira')
                
                    if opcao == '6':
                        print("-------Sábado--------------")
                        aluno.imprimir_tabela(f'escola.{semestre_aluno}_semestre_sabado')
                        
                elif opcao_operacao == '2':
                    opcao = input("Qual o dia que você deseja ver a lista de professores [1] Segunda-Feira, [2] Terça-Feira, [3] Quarta-Feira, [4] Quinta-Feira, [5] Sexta-Feira, [6] Sábado: ")
                    
                    if opcao == '1':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_segunda_feira"
                        nome_coluna = 'professores'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                    elif opcao == '2':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_terca_feira"
                        nome_coluna = 'professores'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                    elif opcao == '3':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_quarta_feira"
                        nome_coluna = 'professores'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                    elif opcao == '4':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_quinta_feira"
                        nome_coluna = 'professores'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                    elif opcao == '5':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_sexta_feira"
                        nome_coluna = 'professores'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                    elif opcao == '6':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_sabado"
                        nome_coluna = 'professores'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                        
                elif opcao_operacao == '3':
                    opcao = input("Qual o dia que você deseja ver a lista de materias [1] Segunda-Feira, [2] Terça-Feira, [3] Quarta-Feira, [4] Quinta-Feira, [5] Sexta-Feira, [6] Sábado: ")
                    
                    if opcao == '1':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_segunda_feira"
                        nome_coluna = 'materias'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                        
                    elif opcao == '2':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_terca_feira"
                        nome_coluna = 'materias'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                            
                    elif opcao == '3':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_quarta_feira"
                        nome_coluna = 'materias'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                    
                    elif opcao == '4':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_quinta_feira"
                        nome_coluna = 'materias'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                    
                    elif opcao == '5':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_sexta_feira"
                        nome_coluna = 'materias'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)
                        
                    elif opcao == '6':
                        nome_tabela = f"escola.{semestre_aluno}_semestre_sabado"
                        nome_coluna = 'materias'
                        aluno.imprimir_coluna(nome_tabela, nome_coluna)    
                        
                elif opcao_operacao == '4':
                    try:
                        # Consulta para obter as notas do aluno com base na matrícula
                        query = "SELECT * FROM notas_alunos WHERE matricula = %s"
                        self.conexao.cursor.execute(query, (matricula,))
                        resultado = self.conexao.cursor.fetchall()

                        if resultado:
                            print(f"--Essa é sua relação de notas {nome}---")
                            for nota in resultado:
                                print("Disciplina:", nota[0])  
                                print("Nota:", nota[3])  
                                print("-----")

                        else:
                            print("Nenhuma nota encontrada para a matrícula", matricula)

                    except mysql.connector.Error as err:
                        print(f"Erro ao executar a consulta: {err}")
                                                          
            else:
                print("Informações do aluno não encontradas.")
                return None, None 
        else:
            print("Usuário ou senha incorretos.")
            return None, None 
        
        
        
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

    def imprimir_coluna(self, nome_tabela, nome_coluna):
        try:
            query = f"SELECT {nome_coluna} FROM {nome_tabela}"
            self.conexao.cursor.execute(query)
            coluna = self.conexao.cursor.fetchall()
            
            if coluna:
                print(f"Lista de {nome_coluna}:")
                for item in coluna:
                    print(item[0])
            else:
                print("Não há dados disponíveis.")
        except mysql.connector.Error as err:
            print(f"Erro ao imprimir coluna: {err}")

        
    
    

conexao = ConexaoBanco()

opcao = int(input("Qual é seu tipo de usuário [0]Administrador, [1] Secretário(a), [2] Professor, [3] Diretor, [4] Aluno: "))

match opcao:
    
    case 0:
        administrador = Administrador(conexao) 
        print("Tela de login")
        nome_administrador = input("Usuário: ")
        codigo_autorizacao = input("Senha: ")
        administrador.login_administrador(nome_administrador, codigo_autorizacao)
    case 1:
        secretaria = Secretaria(conexao)
        print("Tela de Login")
        usuario_secretario = input("Digite seu usuário: ")
        senha_secretario = input("Digite sua senha: ")
        secretaria.login_secretaria(usuario_secretario, senha_secretario)
    case 2:
        professor = Professor(conexao)
        print("Tela de Login")
        usuario_professor = input("Digite seu usuário: ")
        senha_professor = input("Digite sua senha: ")
        professor.login_professor(usuario_professor, senha_professor)
    
    case 3:
        diretor = Diretor(conexao)
        print("Tela de Login")
        usuario_diretor = input("Digite seu usuário: ")
        senha_diretor = input("Digite a senha: ")
        diretor.login_diretor(usuario_diretor, senha_diretor)
    
    case 4:
        aluno = Aluno(conexao)
        print("Tela de Login")
        usuario_aluno = input("Digite seu usuário: ")
        senha_aluno = input("Digite sua senha: ")
        aluno.login_aluno(usuario_aluno, senha_aluno)
        
    case _:
        print("Digite os usuários que estão no primiero login de 1 a 4.")    
                    
conexao.encerrar_conexao()