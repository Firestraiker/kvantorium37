import logging
from logging import info, error, exception, warning
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='dev.log')

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    update.message.reply_text('Привет! Я бот, повторяющий слова, написанные тобой в чате.')


def help_command(update, context):
    update.message.reply_text('Help!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(
        "1173900008:AAEH1M8St4toafkR0KX-KiREt4bGjMKInpc", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
