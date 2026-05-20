import pandas as pd
import plotly.express as px
import streamlit as st

# leitura do arquivo CSV
car_data = pd.read_csv("app_plus_vehicles/vehicles.csv")

# cabeçalho
st.header("Análise Exploratória de Dados de Veículos")

# botão para histograma
hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando um histograma para a coluna 'odometer'")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# botão para gráfico de dispersão
scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Criando um gráfico de dispersão: preço vs odômetro")
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
    
