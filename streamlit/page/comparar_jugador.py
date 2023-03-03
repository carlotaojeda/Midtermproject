import streamlit as st
from data.get_data import get_all_players_name


def comparar_jugador ():
    st.title ("Comparar jugadores")
    lista_jugadores = get_all_players_name()
    jugador_1 = st.selectbox("Elige un jugador",lista_jugadores)
    jugador_2 = st.selectbox("Elige otro jugador",lista_jugadores)

    

