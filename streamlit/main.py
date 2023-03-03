import streamlit as st
from page.comparar_jugador import comparar_jugador


columna = st.sidebar.selectbox("elige pagina",["Home" , "Buscar jugador", "Buscar equipo","Comparar jugadores", "Comparar equipos"])

if columna == "Home":
    st.title ("Eurocopa 2020")
    
if columna == "Comparar jugadores":
    comparar_jugador()