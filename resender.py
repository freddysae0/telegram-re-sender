from telethon import TelegramClient, events
import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Your API credentials and Data
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
your_channel = "momazos01"
channels_to_spy= ["memesltn", "ChistesyMasChistes" , "MemesTgm"  ]


# Create a Telegram client
client = TelegramClient('resender', api_id, api_hash)

for chat_to_spy in channels_to_spy: 
    @client.on(events.NewMessage(chats=chat_to_spy))
    async def handler(event):
        # Here you can add any action you want to perform with the new message
        print(f"New message received from {event.sender_id}: {event.raw_text}")
        await client.forward_messages(your_channel, event.message, drop_author=True)

async def main():
   # Connect and authorize if necessary
    await client.start()
    print(f"Watcher activated. Waiting for new messages in the defined channels")

    # Keep the client running to listen for events
    await client.run_until_disconnected()

# Start the client
with client:
    client.loop.run_until_complete(main())
