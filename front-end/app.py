# front-end/app.py
import streamlit as st
import pandas as pd
import sys
import os

# Adicionando o caminho da raiz do projeto ao sys.path para permitir a importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo_fraude import carregar_modelo, prever_fraude

# Carregar o modelo de detecção de fraudes
modelo = carregar_modelo()

# Título da aplicação
st.title('Detecção de Fraudes em Transações Financeiras')

# Descrição
st.write("""
Esta aplicação utiliza um modelo de inteligência artificial para detectar fraudes em transações financeiras.
Suba um arquivo CSV com as transações e veja os resultados.
""")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Carregar o arquivo CSV
    data = pd.read_csv(uploaded_file)
    
    # Mostrar uma amostra dos dados
    st.write("Visualização dos dados:")
    st.write(data.head())
    
    # Prever fraudes
    if st.button('Detectar Fraudes'):
        predicoes = prever_fraude(modelo, data)
        data['Fraude'] = predicoes
        
        # Mostrar resultados
        st.write("Resultados da detecção de fraudes:")
        st.write(data)
        
        # Baixar resultados
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Baixar resultados como CSV",
            data=csv,
            file_name='resultados_fraude.csv',
            mime='text/csv'
        )
