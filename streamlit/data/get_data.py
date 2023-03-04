import re
import requests

def get_all_teams_statistics():
    return requests.get(f"http://127.0.0.1:8000/equipos").json()

def get_all_teams_names():
    return requests.get(f"http://127.0.0.1:8000/equipos/nombres").json()

def get_all_statistic_per_team(nombres):
    return requests.get(f"http://127.0.0.1:8000/equipo/{nombres}").json()

def get_all_possession_per_team(nombres):
    return requests.get(f"http://127.0.0.1:8000/equipo/{nombres}/posesion").json()

def get_all_golesfavor_per_team(nombres):
    return requests.get(f"http://127.0.0.1:8000/equipo/{nombres}/goles_favor").json()

def get_all_golescontra_per_team(nombres):
    return requests.get(f"http://127.0.0.1:8000/equipo/{nombres}/goles_contra").json()

def get_all_shots_per_team(nombres):
    return requests.get(f"http://127.0.0.1:8000/equipo/{nombres}/tiros_totales").json()

def get_all_shots_ontarget_per_team(nombres):
    return requests.get(f"http://127.0.0.1:8000/equipo/{nombres}/iros_puerta").json()

def get_all_statistic_max():
    return requests.get(f"http://127.0.0.1:8000/estadistica/maximo").json()

def get_all_players_statistics():
    return requests.get(f"http://127.0.0.1:8000/jugadores").json()

def get_all_players_name():
    return requests.get(f"http://127.0.0.1:8000/jugadores/nombres").json()

def get_all_statistic_per_player(nombres):
    return requests.get(f"http://127.0.0.1:8000/jugador/{nombres}/stats").json()

def get_all_goals_per_player(nombres):
    return requests.get(f"http://127.0.0.1:8000/jugador/{nombres}/goles").json()

def get_all_asistencias_per_player(nombres):
    return requests.get(f"http://127.0.0.1:8000/jugador/{nombres}/asistencias").json()

def get_all_yellow_card_per_player(nombres):
    return requests.get(f"http://127.0.0.1:8000/jugador/{nombres}/amarillas").json()

def get_all_red_card_per_player(nombres):
    return requests.get(f"http://127.0.0.1:8000/jugador/{nombres}/rojas").json()

def get_all_max_statistics_player(nombres):
    return requests.get(f"http://127.0.0.1:8000/jugadores/estadistica/maximo").json()