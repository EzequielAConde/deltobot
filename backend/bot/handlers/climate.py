import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from constants.states import WEATHER_CITY, MAIN_MENU
from services.getweather import getWeatherInfo
from storage.firebase_db import saveUser

async def askCountry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("¿De qué país o ciudad querés saber el clima?")
    return WEATHER_CITY

async def showClimate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ciudad = update.message.text

    mensaje_espera = await update.message.reply_text("Obteniendo clima.")

    for i in range(2):
        await asyncio.sleep(0.5)
        puntos = "." * (i + 2)
        await mensaje_espera.edit_text(f"Obteniendo clima{puntos}")

    reporteClima = await getWeatherInfo(ciudad)

    user = update.effective_user
    saveUser(user_id=user.id, nombre=user.first_name, pais=ciudad)

    await mensaje_espera.edit_text(reporteClima)
    return MAIN_MENU
