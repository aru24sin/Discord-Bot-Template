"""
Discord AI Chatbot
Created on Wed May  3 11:26:16 2023
@author: Aru
"""
import os
import discord
intents = discord.Intents.default()

TOKEN = 'MTEwMzM0MDAyMTc1MjI3MDg2OA.G7ieMr.VDk0vOlezapEM2b6iiBJbuAncwEpHeVvF8Ugl0'

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} had connected to Discord!')

client.run(TOKEN)