from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import db
from weather import getWeather
from generator import generatePlans

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensaje": "API de Deltobot funcionando 🚀"}

@app.get("/usuarios")
def getUsers():
    usuarios_ref = db.collection('usuarios')
    docs = usuarios_ref.stream()

    usuarios = []
    for doc in docs:
        data = doc.to_dict()
        data["user_id"] = doc.id
        usuarios.append(data)

    return {"usuarios": usuarios}

@app.get("/clima")
def weather():
    return getWeather()

@app.get("/planes")
def plans():
    datos_clima = getWeather()

    if "error" in datos_clima:
        return {"error": datos_clima["error"]}

    pais = datos_clima["pais"]
    texto_ia = generatePlans(pais)

    return {
        "pais": pais,
        "pronostico": datos_clima["pronostico"],
        "planes_ia": texto_ia
    }