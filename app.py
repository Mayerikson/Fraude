import streamlit as st
import pandas as pd
import numpy as np

# Cache de dados para carregamento instantâneo
@st.cache_data
def carregar_dados():
    return pd.DataFrame({
        'Mês': [1, 1, 2, 2, 3],
        'Métrica': ['Custo Total', 'Falsos Positivos', 'Recall', 'Economia', 'Custo Total'],
        'Valor': [649, 2.65, 66, 195, 552],
        'Meta': [552, 1.9, 75, 210, 454]
    })

# Configuração rápida da página
st.set_page_config(page_title="Antifraude Turbo", layout="centered")

# Sidebar minimalista
with st.sidebar:
    st.title("⚙️ Filtros")
    mes = st.selectbox("Mês", options=[1, 2, 3])

# Dados cacheados
dados = carregar_dados()

# KPIs em colunas (carregamento prioritário)
col1, col2, col3 = st.columns(3)
col1.metric("📈 Recall", "78%", "+12%")
col2.metric("⚠️ Falsos Positivos", "1.4%", "-1.25%")
col3.metric("💰 Economia", "R$ 209k", "32%")

# Tabela otimizada
st.dataframe(
    dados[dados['Mês'] == mes],
    use_container_width=True,
    hide_index=True,
    height=200
)

# Gráfico simplificado
st.line_chart(
    dados,
    x='Mês',
    y='Valor',
    color='Métrica',
    height=300
)

# Simulador de fraude (sob demanda)
if st.checkbox("🕵️ Ativar simulador rápido"):
    valor = st.number_input("Valor (R$)", min_value=0, max_value=10000, value=1000)
    distancia = st.slider("Distância (km)", 0, 100, 50)
    risco = min(100, (valor * 0.001 + distancia * 0.2))
    st.progress(int(risco))
    st.caption(f"Risco estimado: {risco:.1f}%")
