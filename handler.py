# import handlers
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, PreCheckoutQueryHandler, MessageHandler, Filters

from bot import start, buy, pre_checkout_query, successful_payment

import os

# get token from env
TOKEN = os.environ.get('TOKEN')

def main():

    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Add command handler for /buy
    dispatcher.add_handler(CommandHandler("buy", buy))

    # Add pre-checkout handler
    dispatcher.add_handler(PreCheckoutQueryHandler(pre_checkout_query))

    # Add callback handler for /buy
    dispatcher.add_handler(CallbackQueryHandler(successful_payment, pattern="successful_payment"))

    # handler for successful payment
    dispatcher.add_handler(MessageHandler(Filters.successful_payment, successful_payment))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()