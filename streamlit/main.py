import streamlit as st
from page.comparar_jugador import comparar_jugador
from page.comparar_equipo import comparar_teams
from page.search_equipo import search_equipo
from page.search_jugador import search_jugador




columna = st.sidebar.selectbox("elige pagina",["Home" , "Buscar jugador", "Buscar equipo","Comparar jugadores", "Comparar equipos"])

if columna == "Home":
    st.title ("Eurocopa 2020")
    st.image ("https://www.spainenglish.com/wp-content/uploads/2020/03/EURO_2020_Logo_Lnd_OnLight_FC_CMYK-1024x375.png")
if columna == "Comparar jugadores":
    comparar_jugador()
if columna == "Buscar equipo":
    search_equipo()
if columna == "Comparar equipos":
    comparar_teams()
if columna == "Buscar jugador":
    search_jugador()
