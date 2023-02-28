from fastapi import FastAPI
from routers import jugadores, equipos

app = FastAPI ()
app.include_router(equipos.router)

@app.get("/")
def principal ():
    return {
        "Status": "Funciona"
    }