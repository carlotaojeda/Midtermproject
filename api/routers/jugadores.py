from fastapi import APIRouter
from database.mongo import db
from json import loads
from bson import json_util


router = APIRouter ()

@router.get("/jugadores")
def jugadores_todos():
    filter = {}
    project = {"_id": 0 }
    resultado = db["players"].find(filter,project)
    return loads(json_util.dumps(resultado))


@router.get("/jugadores/nombres")
def jugadores_nombres():
    resultado = db["players"].distinct("nombre")
    return loads(json_util.dumps(resultado))


@router.get("/jugador/{nombre}/stats")
def stats_by_jugador(nombre):
    nombre = nombre.capitalize()
    filter = {"nombre": nombre}
    project = {"_id": 0 }
    resultado = db["players"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El jugador no jugó la Eurocopa"}


@router.get("/jugador/{nombre}/goles")
def goles_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"nombre": nombre}
    project = {"goles":1, "_id": 0 }
    resultado = db["players"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El jugador no participó la Eurocopa"}
    
    
@router.get("/jugador/{nombre}/asistencias")
def asistencias_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"nombre": nombre}
    project = {"asistencias":1, "_id": 0 }
    resultado = db["players"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El jugador no participó la Eurocopa"}
    
    
@router.get("/jugador/{nombre}/amarillas")
def amarillas_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"nombre": nombre}
    project = {"tarjetas_amarillas":1, "_id": 0 }
    resultado = db["players"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El jugador no participó la Eurocopa"}
    
@router.get("/jugador/{nombre}/rojas")
def rojas_by_name(nombre):
    nombre = nombre.capitalize()
    filter = {"nombre": nombre}
    project = {"tarjetas_rojas":1, "_id": 0 }
    resultado = db["players"].find(filter,project)
    try:
        return loads(json_util.dumps(resultado[0]))
    except:
        return {"Mensaje":" El jugador no participó la Eurocopa"}
    

@router.get("/jugadores/estadistica/maximo")
def jugadores_estadistica_maximo(stats:str):
    stats_dict = {
        'goles': 'goles',
        'asistencias': 'asistencias',
        'tarjetas_rojas': 'tarjetas_rojas',
        'tarjetas_amarillas': 'tarjetas_amarillas'
    }
    
    if stats not in stats_dict:
        return {"message": "Esa estadistica no existe"}
    
    column = stats_dict[stats]
    filter = {}
    project = {"_id":0, "nombre":1, column:1}

    res = list(db["players"].find(filter, project).sort(column, -1).limit(2))
    
    try:   
        return loads(json_util.dumps(res[0]))
    except:
        return {"message": "Hubo un problema!"}