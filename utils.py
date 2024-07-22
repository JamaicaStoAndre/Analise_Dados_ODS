import pandas as pd

def carregar_dados(caminho_arquivo):
    # Carregar as três abas do arquivo .xlsx
    livro_codigos = pd.read_excel(caminho_arquivo, sheet_name='Livro de Códigos')
    todos_dados = pd.read_excel(caminho_arquivo, sheet_name='Todos os Dados')
    series_temporais = pd.read_excel(caminho_arquivo, sheet_name='Séries Temporais')
    return livro_codigos, todos_dados, series_temporais

def resumo_dados(df):
    resumo = {
        'Número de Linhas': df.shape[0],
        'Número de Colunas': df.shape[1],
        'Tamanho do Arquivo (MB)': df.memory_usage(deep=True).sum() / (1024**2),
        'Tipos de Dados': {col: str(dtype) for col, dtype in df.dtypes.items()}
    }
    return resumo
