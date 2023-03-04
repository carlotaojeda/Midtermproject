import streamlit as st
from page.comparar_jugador import comparar_jugador
from page.comparar_equipo import comparar_teams
from page.search_equipo import search_equipo
from page.search_jugador import search_jugador




columna = st.sidebar.selectbox("Elige pagina",["Home" , "Buscar jugador", "Buscar equipo","Comparar jugadores", "Comparar equipos"])

if columna == "Home":
    st.image ("https://www.spainenglish.com/wp-content/uploads/2020/03/EURO_2020_Logo_Lnd_OnLight_FC_CMYK-1024x375.png")
    st.subheader ("Dashboard de la Eurocopa 2020.")
    st.text ("Compara las estadísticas de los jugadores/equipos o busca esta info individualmente.")
    st.text (" Elige en la barra de la izquierda lo que quieras descubrir")
    st.markdown ("1.Compara las estadísticas de los jugadores")
    st.markdown ("2.Busca las estadisticas generales de cada equipo")
    st.markdown ("3.Compara las estadísticas de los equipos que jugaron")
    st.markdown ("4.Busca las estadísticas individuales de cada jugador")
if columna == "Comparar jugadores":
    comparar_jugador()
if columna == "Buscar equipo":
    search_equipo()
if columna == "Comparar equipos":
    comparar_teams()
if columna == "Buscar jugador":
    search_jugador()
