# import LabeledPrice from telegram
from telegram import LabeledPrice

import os

# get provider token from env
PROVIDER_TOKEN = os.environ.get('PROVIDER_TOKEN')

# Define a command handler for the /start command
def start(update, context):
    bot = context.bot
    chat_id = update.effective_chat.id
    text = "Welcome to my bot! To buy something, use the /buy command."
    bot.send_message(chat_id=chat_id, text=text)

# Define a command handler for the /buy command
def buy(update, context):
    # Create invoice
    bot = context.bot
    chat_id = update.effective_chat.id
    title = "My awesome product"
    description = "This is a description of my awesome product"
    payload = "CUSTOM-PAYLOAD"
    provider_token = PROVIDER_TOKEN
    start_parameter = "test-payment"
    currency = "UZS"
    prices = [
        LabeledPrice(label="Product", amount=100000),
    ]
    bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description=description,
        payload=payload,
        provider_token=provider_token,
        start_parameter=start_parameter,
        currency=currency,
        prices=prices,
    )

# Define a callback handler for the /buy command
def pre_checkout_query(update, context):
    print('pre_checkout_query')
    bot = context.bot
    query = update.pre_checkout_query
    print(query)
    if query.invoice_payload != "CUSTOM-PAYLOAD":
        # Pre-checkout failed
        bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=False, error_message="Something went wrong...")
    else:
        # Pre-checkout succeeded
        bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)

    
# Define a callback handler for the /buy command
def successful_payment(update, context):
    print('successful_payment')
    bot = context.bot
    print(update)
    message = update.effective_message
    bot.send_message(
        chat_id=message.chat_id,
        text="Thank you for your purchase! Your product will be shipped to you as soon as possible.",
    )