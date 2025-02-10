import streamlit as st
import pandas as pd
import plotly_express as px

vehicles_data = pd.read_csv('vehicles_us.csv')

st.header(':red[Anuncios de Vehiculos] :car:')

year_button = st.button('Autos por Modelo de Año')
if year_button:
    st.write('Distribucion de Autos por Modelo de Año')
    fig_h = px.histogram(vehicles_data, x='model_year')
    st.plotly_chart(fig_h, use_container_width=True)

corr_button = st.button('Relacion Precio Vehiculo y Kilometraje')
if corr_button:
    st.write('Correlacion entre la variable PRECIO y la variables KILOMETRAJE')
    fig_sc = px.scatter(vehicles_data, x= 'odometer', y= 'price')
    st.plotly_chart(fig_sc)

his_check = st.checkbox('Autos por modelo')
if his_check:
    st.write ('Distribucion de Autos por Modelo')
    fig_hmo = px.histogram(vehicles_data, x = 'model')
    st.plotly_chart(fig_hmo)