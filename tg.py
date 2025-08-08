import os
from google import genai
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

client_tg = TelegramClient('user_bot', api_id, api_hash)
@client_tg.on(events.NewMessage())
async def message_handler(event):
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=event.text
    )
    await event.respond(response.text)
client_tg.start()
client_tg.run_until_disconnected()
