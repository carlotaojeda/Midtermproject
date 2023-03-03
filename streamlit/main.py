import streamlit as st

st.title("Eurocopa 2020")

with st.sidebar:
    st.radio('Select one:', ["jugadores", "equipos"])