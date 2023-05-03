"""
Discord Chatbot Template
Created on Wed May  3 11:26:16 2023
@author: Aru
"""
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} had connected to Discord!')

client.run(TOKEN)
