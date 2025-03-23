import discord
import os
import asyncio 

intents = discord.Intents.default()
intents.messages = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

    await client.change_presence(status=discord.Status.idle)

    await asyncio.sleep(5) 
    
    activity = discord.Activity(type=discord.ActivityType.watching, name="/ho3s")
    await client.change_presence(activity=activity)

TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)
