import requests
import config
from services.generateresponsse import generateTips

def getWeatherTip(condicion: str) -> str:
    condicion = condicion.lower()
    if "rain" in condicion:
        return "🌧️ Parece que va a llover. ¡Llevá paraguas!"
    elif "clear" in condicion:
        return "☀️ Está despejado. ¡Disfrutá el día!"
    elif "cloud" in condicion:
        return "⛅ Un día nublado. Podría refrescar más tarde."
    elif "snow" in condicion:
        return "❄️ Va a nevar. ¡Abrigate bien!"
    else:
        return "🤔 No estoy seguro del clima, pero salí preparado por las dudas."

async def getWeatherInfo(ciudad: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={config.OPENWEATHER_API_KEY}&units=metric&lang=es"

    try:
        respuesta = requests.get(url)
        datos = respuesta.json()

        if datos.get("cod") != 200:
            return f"No encontré información del clima para '{ciudad}'. 😓"

        temperatura = datos["main"]["temp"]
        condicion = datos["weather"][0]["description"]
        recomendacion = getWeatherTip(condicion)
        consejoExtra = await generateTips(ciudad, condicion)

        resultado = (
            f"🌍 Qué lindo es: {ciudad.title()}\n"
            f"🌡️ Tenemos una temperatura de: {temperatura}°C\n"
            f"🌤️ Las condiciones de hoy son: {condicion.capitalize()}\n"
        )

        if consejoExtra:
            resultado += f"\n💡 {consejoExtra}"

        return resultado

    except Exception as e:
        return f"❌ Ocurrió un error al consultar el clima: {e}"
