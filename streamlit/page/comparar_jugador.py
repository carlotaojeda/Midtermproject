import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from data.get_data import get_all_players_name, get_all_statistic_per_player


def comparar_jugador():
    
    # Creamos un título para nuestra página
    st.image ("https://phantom-marca.unidadeditorial.es/c3dad7b360ab2410fca3991721db8740/resize/1320/f/jpg/assets/multimedia/imagenes/2021/06/11/16234017254168.jpg")
    st.title("Comparar jugadores")
    st.subheader ("Elige dos jugadores de la Eurocopa 2020 para poder comparar las estadísticas.")
    st.markdown ("1. Los números de goles durante la Eurocopa 2020")
    st.markdown ("2. Total de asistencias")
    st.markdown ("3. Total de tarjetas Amarillas")
    st.markdown ("4. Total de tarjetas Rojas")
    # Obtenemos la lista de jugadores utilizando la función get_all_players_name
    lista_jugadores = get_all_players_name()

    # Creamos un menú desplegable para que el usuario seleccione el primer jugador
    jugador_1 = st.selectbox("Elige un jugador", lista_jugadores)

    # Creamos un menú desplegable para que el usuario seleccione el segundo jugador
    jugador_2 = st.selectbox("Elige otro jugador", lista_jugadores)

    # Obtenemos las estadísticas del primer jugador utilizando la función get_all_statistic_per_player
    resultado_1 = get_all_statistic_per_player(jugador_1)

    # Obtenemos las estadísticas del segundo jugador utilizando la función get_all_statistic_per_player
    resultado_2 = get_all_statistic_per_player(jugador_2)

    # Creamos una lista con las estadísticas del primer jugador
    jugador_1_estadisticas = [resultado_1['goles'], resultado_1['asistencias'], resultado_1['tarjetas_amarillas'], resultado_1['tarjetas_rojas']]

    # Creamos una lista con las estadísticas del segundo jugador
    jugador_2_estadisticas = [resultado_2['goles'], resultado_2['asistencias'], resultado_2['tarjetas_amarillas'], resultado_2['tarjetas_rojas']]

    # Creamos una lista con las etiquetas para la gráfica
    etiquetas = ['Goles', 'Asistencias', 'Tarjetas amarillas', 'Tarjetas rojas']

    # Creamos un arreglo de números espaciados uniformemente utilizando numpy
    x = np.arange(len(etiquetas))

    # Definimos el ancho de cada barra
    width = 0.25

    # Creamos una figura y un eje para la gráfica
    fig, ax = plt.subplots()

    # Creamos las barras para el primer jugador
    rects1 = ax.bar(x - width/2, jugador_1_estadisticas, width, label=jugador_1)

    # Creamos las barras para el segundo jugador
    rects2 = ax.bar(x + width/2, jugador_2_estadisticas, width, label=jugador_2)

    # Añadimos una etiqueta para el eje y
    ax.set_ylabel('Estadísticas')

    # Añadimos etiquetas para el eje x
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)

    # Creamos una leyenda para la gráfica
    ax.legend()

    # Mostramos la gráfica en Streamlit utilizando la función st.pyplot()
    st.pyplot(fig)









