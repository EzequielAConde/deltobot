from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from constants.states import MAIN_MENU, WEATHER_CITY, ANALYZE_SENTIMENT
from handlers.counter import setCounter
from handlers.climate import askCountry

menuOpciones = [
    ["¡Quiero saber el clima!"],
    ["¡Quiero contar!"],
    ["Hablar con DeltoBot 🤖"]
]

menuTeclado = ReplyKeyboardMarkup(menuOpciones, resize_keyboard=True)

async def showMainMenu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "¿En qué te puedo ayudar? Elegí una opción ⌘",
        reply_markup=menuTeclado
    )
    return MAIN_MENU

async def handleSelMenu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    texto = update.message.text

    if texto == "¡Quiero saber el clima!":
        return await askCountry(update, context)

    elif texto == "¡Quiero contar!":
        await setCounter(update, context)
        return await showMainMenu(update, context)

    elif texto == "Hablar con DeltoBot 🤖":
        await update.message.reply_text(
            "¡Hola, soy DeltoBot 🤖 Un gusto conocerte, decime en qué puedo ayudarte.\n\n"
            "1) Usá /cortar para terminar la conversación.\n"
            "2) Puedes escribirme *Analiza cómo estuvo la conversación* para sacar un diagnóstico de nuestra charla.",
            parse_mode="Markdown"
        )
        return ANALYZE_SENTIMENT

    else:
        await update.message.reply_text("Esa opción no se encuentra. Por favor, elegí una del menú.")
        return MAIN_MENU
