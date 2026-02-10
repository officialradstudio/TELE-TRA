import os
from telethon import TelegramClient, events

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

source_channel = os.getenv("SOURCE")
target_channel = os.getenv("TARGET")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        await client.send_message(target_channel, event.message)
        print("Message forwarded")
    except Exception as e:
        print("Error:", e)

print("Bot is running...")

client.start()
client.run_until_disconnected()
