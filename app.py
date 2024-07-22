import streamlit as st
from utils import carregar_dados, resumo_dados
from visualization import grafico_comparativo, grafico_individual

# Lista de municípios para seleção
municipios = [
    "Armazém", "Braço do Norte", "Capivari de Baixo", "Grão-Pará", "Gravatal",
    "Imaruí", "Imbituba", "Jaguaruna", "Laguna", "Pedras Grandes", "Pescaria Brava",
    "Rio Fortuna", "Sangão", "Santa Rosa de Lima", "São Ludgero", "São Martinho",
    "Treze de Maio", "Tubarão"
]

# Inicialização das variáveis globais
if 'df_todos_dados' not in st.session_state:
    st.session_state.df_todos_dados = None
if 'df_series_temporais' not in st.session_state:
    st.session_state.df_series_temporais = None
if 'carregado' not in st.session_state:
    st.session_state.carregado = False

# Configuração do menu lateral
st.sidebar.title('Painel ODS')
opcao = st.sidebar.selectbox('Selecione a opção', ['Carregar Dados', 'Visualização Comparativa', 'Análise Detalhada'])

# Aba de carregamento de dados
if opcao == 'Carregar Dados':
    caminho_arquivo = st.sidebar.file_uploader("Escolha o arquivo Excel", type="xlsx")
    if caminho_arquivo is not None:
        try:
            livro_codigos, todos_dados, series_temporais = carregar_dados(caminho_arquivo)
            st.session_state.df_todos_dados = todos_dados
            st.session_state.df_series_temporais = series_temporais
            st.session_state.carregado = True
            resumo = resumo_dados(todos_dados)
            st.write("Resumo da aba 'Todos os Dados':", resumo)
            st.write(todos_dados.head())
            resumo_series = resumo_dados(series_temporais)
            st.write("Resumo da aba 'Séries Temporais':", resumo_series)
            st.write(series_temporais.head())
            st.write("Colunas da aba 'Todos os Dados':", todos_dados.columns.tolist())
            st.write("Colunas da aba 'Séries Temporais':", series_temporais.columns.tolist())
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")
    elif st.session_state.carregado:
        st.write("Dados já carregados:")
        st.write(st.session_state.df_todos_dados.head())

# Aba de visualização comparativa
if opcao == 'Visualização Comparativa' and st.session_state.df_todos_dados is not None:
    municipios_selecionados = st.sidebar.multiselect('Selecione os municípios', municipios)
    colunas_selecionadas = st.sidebar.multiselect('Selecione os indicadores', st.session_state.df_todos_dados.columns[1:])
    
    if municipios_selecionados and colunas_selecionadas:
        try:
            fig = grafico_comparativo(st.session_state.df_todos_dados, municipios_selecionados, colunas_selecionadas)
            if fig:
                st.plotly_chart(fig)
        except KeyError as e:
            st.error(f"Erro ao criar gráfico: {e}")
        except ValueError as e:
            st.error(f"Erro ao criar gráfico: {e}")
    else:
        st.warning("Por favor, selecione pelo menos um município e uma coluna para visualização.")

# Aba de análise detalhada
if opcao == 'Análise Detalhada' and st.session_state.df_series_temporais is not None:
    municipio_selecionado = st.sidebar.selectbox('Selecione o município', municipios)
    colunas_selecionadas = st.sidebar.multiselect('Selecione os indicadores', st.session_state.df_series_temporais.columns[1:])
    
    if municipio_selecionado and colunas_selecionadas:
        try:
            fig = grafico_individual(st.session_state.df_series_temporais, municipio_selecionado, colunas_selecionadas)
            if fig:
                st.plotly_chart(fig)
        except KeyError as e:
            st.error(f"Erro ao criar gráfico: {e}")
        except ValueError as e:
            st.error(f"Erro ao criar gráfico: {e}")
    else:
        st.warning("Por favor, selecione pelo menos um município e uma coluna para visualização.")
