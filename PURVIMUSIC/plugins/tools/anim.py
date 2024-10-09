import random
import asyncio
from pyrogram import Client, filters
from PURVIMUSIC import app

# Create a list of emojis
emojis = [
    "😀", "😂", "😍", "😎", "🥳", "🤖", "👻", "🌟", "🍀", "🎉",
    "💖", "🔥", "✨", "😇", "🤩", "😜", "😺", "🐶", "🐱", "🦄"
]

# Command handler for /play
@app.on_message(filters.command("play"))
async def start_handler(client, message):
    random_emoji = random.choice(emojis)
    
    # Send the reply message
    sent_message = await message.reply_text(f"{random_emoji}")
    
    # Wait for a specified amount of time (e.g., 5 seconds)
    await asyncio.sleep(0)
    
    # Delete the user's original message
    await message.delete()
    
    # Delete the bot's reply message after the wait
    await sent_message.delete()
