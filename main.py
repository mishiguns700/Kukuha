# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['1', '2', '3']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! я бот тестер, пожалуйста, выбери тест, который ты хочешь пройти"
    )
    await update.message.reply_html(
        rf"1 - тип темперамента_1"
    )
    await update.message.reply_html(
        rf"2 - тип темперамента_2"
    )
    await update.message.reply_html(
        rf"3 - IQ-тест",
        reply_markup=markup
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


def main():
    application = Application.builder().token("6218641307:AAETxF-N_OoITvKa98VUhk568qpmPt3k_RI").build()
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.run_polling()


if __name__ == '__main__':
    main()
