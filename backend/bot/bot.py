from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ConversationHandler, ContextTypes
)
from handlers.menu import showMainMenu, handleSelMenu
from handlers.counter import setCounter
from handlers.manager import splitMessage, endConversation, freeConversation
from constants.states import MAIN_MENU, WEATHER_CITY, ANALYZE_SENTIMENT
from handlers.climate import showClimate
import config

async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usuario = update.effective_user
    nombre = usuario.first_name
    await update.message.reply_text(f"¡Hola, {nombre}! Soy DeltoBot 🤖 un gusto verte por aquí")
    return await showMainMenu(update, context)


def main():
    app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

    app.job_queue.run_repeating(lambda context: None, interval=3600)

    manejadorConversacion = ConversationHandler(
        entry_points=[CommandHandler('start', iniciar)],
        states={
            MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, handleSelMenu)],
            WEATHER_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, showClimate)],
            ANALYZE_SENTIMENT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, freeConversation),
                CommandHandler("cortar", endConversation),
            ],
        },
        fallbacks=[CommandHandler('start', iniciar)],
        conversation_timeout=300,
    )

    app.add_handler(manejadorConversacion)
    app.add_handler(CommandHandler("count", setCounter))


    app.run_polling()

if __name__ == '__main__':
    main()
