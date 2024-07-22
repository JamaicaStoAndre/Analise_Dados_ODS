import pandas as pd
import plotly.express as px
import streamlit as st

def grafico_comparativo(df, municipios, colunas):
    df_filtro = df[df['Município'].isin(municipios)].copy()
    if df_filtro.empty:
        st.warning("Não há dados disponíveis para os municípios e indicadores selecionados.")
        return None

    df_filtro['id'] = df_filtro['id'].astype(str)  # Corrigir o id para string
    
    st.write("Dados filtrados para municípios e colunas selecionadas:", df_filtro)
    
    fig = px.line(df_filtro, x='Município', y=colunas, title='Comparação de Indicadores')
    return fig

def grafico_individual(df, municipio, colunas):
    df_filtro = df[df['NM_Municipio'] == municipio].copy()
    if df_filtro.empty:
        st.warning("Não há dados disponíveis para o município e indicadores selecionados.")
        return None

    df_filtro['ano'] = df_filtro['ano'].astype(str)  # Corrigir o ano para string
    
    st.write("Dados filtrados para município e colunas selecionadas:", df_filtro)
    
    fig = px.line(df_filtro, x='ano', y=colunas, title=f'Indicadores para {municipio}')
    return fig
