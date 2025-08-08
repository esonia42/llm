import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient('user_bot', api_id, api_hash)
@client.on(events.NewMessage())
async def echo_handler(event):
    await event.respond(event.text)
client.start()
client.run_until_disconnected()
