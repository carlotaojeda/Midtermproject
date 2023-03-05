import streamlit as st
from data.get_data import get_all_players_name, get_all_statistic_per_player

def search_jugador():
    
    st.title("Busca un jugador")
    st.image ("https://okdiario.com/img/2021/05/30/jugadores-eurocopa-655x368.jpg")

    lista_jugadores = get_all_players_name()

    jugador = st.selectbox("Elige un jugador", lista_jugadores)

    stats = get_all_statistic_per_player(jugador)

    # Crear una tabla con los datos
    table = f"""
        <table>
            <tr>
                <td><b>Nombre:</b></td>
                <td>{stats['nombre']}</td>
            </tr>
            <tr>
                <td><b>Goles:</b></td>
                <td>{stats['goles']}%</td>
            </tr>
            <tr>
                <td><b>Asistencias:</b></td>
                <td>{stats['asistencias']}</td>
            </tr>
            <tr>
                <td><b>Tarjetas Rojas:</b></td>
                <td>{stats['tarjetas_rojas']}</td>
            </tr>
            <tr>
                <td><b>Tarjetas Amarillas:</b></td>
                <td>{stats['tarjetas_amarillas']}</td>
            </tr>
        </table>
    """

    # Mostrar la tabla utilizando markdown
    st.markdown(table, unsafe_allow_html=True)
