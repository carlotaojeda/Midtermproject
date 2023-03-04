import streamlit as st
from data.get_data import get_all_teams_names, get_all_statistic_per_team

def search_equipo():
    
    st.title("Busca un equipo")
    st.image ("https://e00-marca.uecdn.es/assets/multimedia/imagenes/2018/12/02/15437514534555.jpg")

    lista_equipos = get_all_teams_names()

    equipo = st.selectbox("Elige un equipo", lista_equipos)

    stats = get_all_statistic_per_team(equipo)

    # Crear una tabla con los datos
    table = f"""
        <table>
            <tr>
                <td><b>Equipo:</b></td>
                <td>{stats['equipo']}</td>
            </tr>
            <tr>
                <td><b>Posesión total:</b></td>
                <td>{stats['posesion_total']}%</td>
            </tr>
            <tr>
                <td><b>Goles a favor:</b></td>
                <td>{stats['goles_a_favor']}</td>
            </tr>
            <tr>
                <td><b>Goles en contra:</b></td>
                <td>{stats['goles_en_contra']}</td>
            </tr>
            <tr>
                <td><b>Shots totales:</b></td>
                <td>{stats['shots_totales']}</td>
            </tr>
            <tr>
                <td><b>Shots a puerta:</b></td>
                <td>{stats['shots_puerta']}</td>
            </tr>
        </table>
    """

    # Mostrar la tabla utilizando markdown
    st.markdown(table, unsafe_allow_html=True)
