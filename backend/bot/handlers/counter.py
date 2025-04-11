from telegram import Update
from telegram.ext import ContextTypes
from collections import defaultdict
from storage.firebase_db import increaseCounter
import time

clicsPorUsuario = defaultdict(list)

async def setCounter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usuario = update.effective_user
    usuarioId = usuario.id
    nombre = usuario.first_name
    tiempoActual = time.time()

    clicsPorUsuario[usuarioId].append(tiempoActual)
    clicsPorUsuario[usuarioId] = [
        t for t in clicsPorUsuario[usuarioId] if tiempoActual - t <= 60
    ]

    contador = increaseCounter(usuarioId, nombre)

    mensajeExtra = ""
    if len(clicsPorUsuario[usuarioId]) >= 3:
        mensajeExtra = "\n⚠️ Despacio que me cuesta sumar..."

    await update.message.reply_text(
        f"Hey {nombre}, llevás {contador} veces apretando el contador.{mensajeExtra}"
    )
