from telegram import Update
from telegram.ext import ContextTypes
from services.chatIA import talkWithIa
from services.analyzeIA import analyzeFeeling
from constants.states import ANALYZE_SENTIMENT, MAIN_MENU

conversacionesPorUsuario = {}

LIMITE_CARACTERES = 4096

def splitMessage(texto):
    """Divide un texto largo en partes menores al límite de Telegram."""
    return [texto[i:i + LIMITE_CARACTERES] for i in range(0, len(texto), LIMITE_CARACTERES)]

async def freeConversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    usuarioId = update.effective_user.id
    texto = update.message.text

    if usuarioId not in conversacionesPorUsuario:
        conversacionesPorUsuario[usuarioId] = []

    if "analiza" in texto.lower() and "conversación" in texto.lower():
        conversacion = " ".join(conversacionesPorUsuario[usuarioId])
        resultado = f"He analizado nuestra charla y ya tengo los resultados. 🤖📋 ¡Vamos a verlos!:\n\n{analyzeFeeling(conversacion)}"
        for parte in splitMessage(resultado):
            await update.message.reply_text(parte)
        return ANALYZE_SENTIMENT

    conversacionesPorUsuario[usuarioId].append(texto)

    pensando = await update.message.reply_text("🤔 Estoy pensando...")

    respuesta = talkWithIa(texto)
    conversacionesPorUsuario[usuarioId].append(respuesta)

    if len(respuesta) <= LIMITE_CARACTERES:
        await pensando.edit_text(respuesta)
    else:
        await pensando.delete()
        for parte in splitMessage(respuesta):
            await update.message.reply_text(parte)

    return ANALYZE_SENTIMENT

async def endConversation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usuarioId = update.effective_user.id
    conversacionesPorUsuario.pop(usuarioId, None)
    await update.message.reply_text("👌 ¡Un gusto hablar contigo! Continue usando el ⌘")
    return MAIN_MENU
