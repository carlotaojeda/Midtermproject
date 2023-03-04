import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from data.get_data import get_all_teams_names, get_all_statistic_per_team


def comparar_teams():
    
    # Creamos un título para nuestra página
    st.image ("https://img.republicworld.com/republic-prod/stories/images/162503626160dc15e5c9cbc.png")
    st.title("Comparar equipos")
    # Obtenemos la lista de jugadores utilizando la función get_all_players_name
    lista_equipos = get_all_teams_names()

    # Creamos un menú desplegable para que el usuario seleccione el primer jugador
    team_1 = st.selectbox("Elige un equipo", lista_equipos)

    # Creamos un menú desplegable para que el usuario seleccione el segundo jugador
    team_2 = st.selectbox("Elige otro equipo", lista_equipos)

    # Obtenemos las estadísticas del primer jugador utilizando la función get_all_statistic_per_player
    resultado_1 = get_all_statistic_per_team(team_1)

    # Obtenemos las estadísticas del segundo jugador utilizando la función get_all_statistic_per_player
    resultado_2 = get_all_statistic_per_team(team_2)

    # Creamos una lista con las estadísticas del primer jugador
    team_1_estadisticas = [resultado_1['posesion_total'], resultado_1['goles_a_favor'], resultado_1['goles_en_contra'], resultado_1['shots_totales'], resultado_1['shots_puerta']]

    # Creamos una lista con las estadísticas del segundo jugador
    team_2_estadisticas = [resultado_2['posesion_total'], resultado_2['goles_a_favor'], resultado_2['goles_en_contra'], resultado_2['shots_totales'], resultado_2['shots_puerta']]

    # Creamos una lista con las etiquetas para la gráfica
    etiquetas = ['Posesion', 'Goles a favor', 'Goles en contra', 'Shots totales', 'Shots a puerta']

    # Creamos un arreglo de números espaciados uniformemente utilizando numpy
    x = np.arange(len(etiquetas))

    # Definimos el ancho de cada barra
    width = 0.35

    # Creamos una figura y un eje para la gráfica
    fig, ax = plt.subplots()

    # Creamos las barras para el primer jugador
    rects1 = ax.bar(x - width/2, team_1_estadisticas, width, label=team_1)

    # Creamos las barras para el segundo jugador
    rects2 = ax.bar(x + width/2, team_2_estadisticas, width, label=team_2)

    # Añadimos una etiqueta para el eje y
    ax.set_ylabel('Estadísticas')

    # Añadimos etiquetas para el eje x
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)

    # Creamos una leyenda para la gráfica
    ax.legend()

    # Mostramos la gráfica en Streamlit utilizando la función st.pyplot()
    st.pyplot(fig)









