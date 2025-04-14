import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Painel Antifraude",
    layout="wide",
    page_icon="🛡️"
)

# Título
st.title("🛡️ Painel de Monitoramento Antifraude")
st.markdown("---")

# Dados de exemplo (substitua por seus dados reais)
dados = pd.DataFrame({
    "Mês": [1, 1, 2, 2, 3],
    "Métrica": ["Custo Total", "Falsos Positivos", "Recall", "Economia", "Custo Total"],
    "Valor": [649, 2.65, 66, 195, 552],
    "Meta": [552, 1.9, 75, 210, 454]
})

# Sidebar
with st.sidebar:
    st.header("Filtros")
    mes = st.selectbox("Mês", options=dados["Mês"].unique())
    
# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Recall", "78%", "+12%")
col2.metric("Falsos Positivos", "1.4%", "-1.25%")
col3.metric("Economia Mensal", "R$ 209k", "32%")

# Gráfico
st.plotly_chart(
    px.line(
        dados, 
        x="Mês", 
        y="Valor", 
        color="Métrica",
        title="Progresso Mensal"
    ),
    use_container_width=True
)

# Rodapé
st.markdown("---")
st.caption("Relatório gerado em " + pd.Timestamp.now().strftime("%d/%m/%Y"))
