import requests
import datetime
from collections import Counter
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    Credencial = credentials.Certificate("../../bot/firebase_key.json")
    firebase_admin.initialize_app(Credencial)

db = firestore.client()

OPENWEATHER_KEY = "abc5124211b0ef6dacc15e354d2ccd63"

dias_es = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miércoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

def getMostPopular():  # obtener_pais_mas_buscado
    usuarios_ref = db.collection('usuarios')
    docs = usuarios_ref.stream()

    paises = []
    for doc in docs:
        data = doc.to_dict()
        paises += [p.strip().lower() for p in data.get('paises_buscados', [])]

    if not paises:
        return None

    pais_mas_comun = Counter(paises).most_common(1)[0][0]
    return pais_mas_comun


def getForecast(pais):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={pais}&appid={OPENWEATHER_KEY}&units=metric&lang=es"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'list' not in data:
        return None

    pronostico_diario = {}
    for item in data['list']:
        fecha = item['dt_txt'].split(' ')[0]
        temp_max = item['main']['temp_max']
        temp_min = item['main']['temp_min']
        dia = datetime.datetime.strptime(fecha, "%Y-%m-%d").strftime("%A")
        dia_es = dias_es[dia]

        if dia_es not in pronostico_diario:
            pronostico_diario[dia_es] = {
                'max': temp_max,
                'min': temp_min
            }
        else:
            pronostico_diario[dia_es]['max'] = max(pronostico_diario[dia_es]['max'], temp_max)
            pronostico_diario[dia_es]['min'] = min(pronostico_diario[dia_es]['min'], temp_min)

    pronostico_lista = []
    for dia, temps in pronostico_diario.items():
        pronostico_lista.append({
            "dia": dia,
            "max": round(temps['max'], 1),
            "min": round(temps['min'], 1)
        })

    return pronostico_lista


def getWeather():
    pais = getMostPopular()
    if not pais:
        return {"error": "No hay países registrados."}

    pronostico = getForecast(pais)
    if not pronostico:
        return {"error": f"No se pudo obtener el clima para {pais}."}

    return {
        "pais": pais,
        "pronostico": pronostico
    }
