import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="poblacion mundial", layout="wide")



st.title("analisis de la poblacion mundial")
st.write("aqui tenemos los diez paises mas poblados del mundo")

archivo = st.file_uploader("selecciona el archivo csv", type=["csv"])

if archivo:
    datos = pd.read_csv(archivo)

    top10 = datos.sort_values(
        "2022 Population",
        ascending=False,
    ).head(10)

    st.dataframe(top10[[
        "Country/Territory",
        "2015 Population",
        "2020 Population",
        "2022 Population"
    ]])

    paises = top10['Country/Territory'].to_numpy()
    poblacion_2015 = top10['2015 Population'].to_numpy()
    poblacion_2020 = top10['2020 Population'].to_numpy()
    poblacion_2022 = top10['2022 Population'].to_numpy()

    total = np.sum(poblacion_2022)
    promedio = np.mean(poblacion_2022)
    mediana = np.median(poblacion_2022)
    minimo = np.min(poblacion_2022)
    maximo = np.max(poblacion_2022)

    st.subheader("estadisticas de la poblacion de 2022")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("poblacion total", f"{total/1000000:,.2f} Millones")
    col2.metric("poblacion promedio", f"{promedio/1000000:,.2f} Millones")
    col3.metric("poblacion mediana", f"{mediana/1000000:,.2f} Millones")
    col4.metric("poblacion minima", f"{minimo/1000000:,.2f} Millones")
    col5.metric("poblacion maxima", f"{maximo/1000000:,.2f} Millones")

    st.subheader("comparacion de la poblacion por pais")

    grafico = top10.set_index("Country/Territory")[[
        "2015 Population",
        "2020 Population",
        "2022 Population"
    ]] / 1000000

    st.bar_chart(grafico)

    st.subheader("datos de los 10 paises")

    st.dataframe(top10[[
        "Country/Territory",
        "2015 Population",
        "2020 Population",
        "2022 Population"
    ]])
else:
    st.info("primero debes cargar el dataset")
