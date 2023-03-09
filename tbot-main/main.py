import os
import requests
from fastapi import FastAPI, Request

# Initialize fastapi application
app = FastAPI()

bot_key = os.getenv("TELEGRAM_BOT_TOKEN") or ""
bot_url = "https://api.telegram.org/bot{token}".format(token=bot_key)

###########################################################################
# POST-Method for TELEGRAM-Webhook
@app.post("/open")
async def http_handler(request: Request):
    response_text, user_identity = None, None
    
    # Try parsing and handling text messages from telegram bot-api
    try:
        # Parse input message from JSON body
        incoming_data = await request.json()
        print("[*] Incoming POST request:",incoming_data)
        # Extract required values from input message
        user_identity = incoming_data['message']['chat']['id']
        message_text = incoming_data['message']['text']
        # Execute handler function for text messages
        response_text = handle_message(message_text)
    
    # Handle errors
    except Exception as e:
        response_text = "Sorry! I could not handle your last message properly!"
    
    print("[*] Response message:",user_identity,"=>",response_text)
    # Send response message
    return {"method": "sendMessage","text": response_text,"chat_id": user_identity}


def handle_message(message_text: str) -> str:
    """
        TODO: This function can be extended. You can apply any logic you like!
    """
    # Send greetings on '/start' message
    if message_text == "/start": return "Hello User!"
    # Otherwise simply repeat the input message
    else: return message_text



###########################################################################
# GET-Method for setting TELEGRAM webhook URL
@app.get("/")
def set_webhook_url(request: Request):
    print("[*] Set webhook url trigggered ...")
    # Format url to set webhook for telegram bot
    telegram_api_url = "{telegram_url}/setWebhook?url=https://{webhook_url}/open".format(
        telegram_url=bot_url,
        webhook_url=os.getenv("DETA_SPACE_APP_HOSTNAME")
    )
    print("[*] Telegram API-URL:",telegram_api_url)
    # Send GET reuqest to telegram bot-api
    telegram_response = requests.get(telegram_api_url)
    # Forward response from bot-api
    return telegram_response.json()