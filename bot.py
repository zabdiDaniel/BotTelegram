from telegram.ext import ApplicationBuilder, CommandHandler

# Coloca tu token directamente en esta variable
BOT_TOKEN = "7598877614:AAHO5BRYZScuECv-jUA2g2D704AquqF_Chw"

# Función para manejar el comando /start
async def start(update, context):
    await update.message.reply_text("¡A chaque le encanta la verga!")

def main():
    # Crear la aplicación y asignar el token directamente
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Agregar un manejador para el comando /start
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()
