from fastapi import APIRouter
from database.mongo import db
from json import loads
from bson import json_util

router = APIRouter()

@router.get("/equipos")
def equipos_todos():
    filter = {}
    project = {"_id": 0 }
    resultado = db["teams"].find(filter,project)
    return loads(json_util.dumps(resultado))

@router.get("/equipos/nombres")
def equipos_nombres():
    resultado = db["teams"].distinct("equipo")
    return loads(json_util.dumps(resultado))

@router.get("/equipo/{nombre}")
def data_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"equipo": nombre}
    project = {"_id": 0 }
    resultado = db["teams"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El equipo no jugó la Eurocopa"}

@router.get("/equipo/{nombre}/posesion")
def posesion_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"equipo": nombre}
    project = {"posesion_total":1, "_id": 0 }
    resultado = db["teams"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El equipo no jugó la Eurocopa"}
    
@router.get("/equipo/{nombre}/goles_favor")
def goles_favor_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"equipo": nombre}
    project = {"goles_a_favor":1, "_id": 0 }
    resultado = db["teams"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El equipo no jugó la Eurocopa"}
    
@router.get("/equipo/{nombre}/goles_contra")
def goles_contra_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"equipo": nombre}
    project = {"goles_en_contra":1, "_id": 0 }
    resultado = db["teams"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El equipo no jugó la Eurocopa"}
    
@router.get("/equipo/{nombre}/tiros_totales")
def total_shots_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"equipo": nombre}
    project = {"shots_totales":1, "_id": 0 }
    resultado = db["teams"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El equipo no jugó la Eurocopa"}
    
@router.get("/equipo/{nombre}/tiros_puerta")
def shots_on_target_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"equipo": nombre}
    project = {"shots_puerta":1, "_id": 0 }
    resultado = db["teams"].find(filter,project)
    print (resultado)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El equipo no jugó la Eurocopa"}
    
@router.get("/estadistica/maximo")
def estadistica_maximo(stats:str):
    stats_dict = {
        'goleshechos': 'goles_a_favor',
        'golesrecibidos': 'goles_en_contra',
        'posesion': 'posesion_total',
        'tirospuerta': 'shots_puerta',
        'shots': 'shots_totales'
    }
    
    if stats not in stats_dict:
        return {"message": "Esa estadistica no existe"}
    
    column = stats_dict[stats]
    filter = {}
    project = {"_id":0, "equipo":1, column:1}

    res = db["teams"].find(filter, project).sort(column, -1).limit(2)
    
    try:   
        return loads(json_util.dumps(res[0]))
    except:
        return {"message": "Hubo un problema!"}