import pandas as pd

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Victor'],
    'Idade': [25, 30, 35, 18],
    'Profissão': ['Engenheiro', 'Advogada', 'Professor', 'Estudante']
}

dataframe = pd.DataFrame(dados)

nome_arquivo = 'C:/Users/vitor/OneDrive/Área de Trabalho/Planilha de dados.xlsx'

try:
    dataframe.to_excel(nome_arquivo, index=False)
    print(f'Dados salvos na planilha "{nome_arquivo}" com sucesso!')
except Exception as e:
    print(f"Erro ao salvar a planilha: {e}")
