# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    print("Nombre de joueurs : "+str(len(guild.members)))



 
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Yooo {member.name}, Bienvenue sur peaceandcube, moi je suis Cravebot!'
    )
    print(member.name+" vient de rejoindre le serveur.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'peace' in message.content.lower():
        await message.channel.send('Ouais bien dit ça! Peace')




client.run(TOKEN)
