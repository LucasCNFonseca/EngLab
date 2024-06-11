import pickle
import pandas as pd

# Função para carregar o modelo
def carregar_modelo():
    with open('modelo.pkl', 'rb') as file:
        modelo = pickle.load(file)
    return modelo

# Função para fazer predições
def prever_fraude(modelo, dados):
    # Adicione aqui o pré-processamento necessário para os dados, se houver
    return modelo.predict(dados)