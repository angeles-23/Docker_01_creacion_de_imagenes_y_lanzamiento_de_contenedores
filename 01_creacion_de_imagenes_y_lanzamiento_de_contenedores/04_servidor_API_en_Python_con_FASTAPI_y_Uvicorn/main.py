# main.py
from fastapi import FastAPI

app = FastAPI(title="API Hola Docker", description="Ejemplo básico de FastAPI ejecutado en Docker")

@app.get("/")
def read_root():
    return {"mensaje": "🚀 Hola desde FastAPI en un contenedor Docker"}

@app.get("/saludo/{nombre}")
def read_item(nombre: str):
    return {"saludo": f"Hola, {nombre}. ¡Tu contenedor Docker funciona perfectamente!"}