import streamlit as st
import pandas as pd
import numpy as np

st.title("Dashboard de Predicción de Regresión")

# Componentes de entrada interactivos (Sidebar)
st.sidebar.header("Parámetros de Entrada")
feature_1 = st.sidebar.slider("Característica 1", 0.0, 100.0, 50.0)
category = st.sidebar.selectbox("Categoría", ["Opción A", "Opción B", "Opción C"])

# Visualización y cálculo
st.write(f"### Análisis para {category}")
data = pd.DataFrame(np.random.randn(20, 2), columns=["X", "Y"])
st.line_chart(data)
