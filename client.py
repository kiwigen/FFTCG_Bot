import os
import discord
from dotenv import load_dotenv
from card import Card
import db


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:        
        if guild.name == GUILD:
            print(f'{client.user} has connected to: \n'
            f'{guild.name}(id: {guild.id})'
            )
            break


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #reagiere nur auf Befehle
    command = message.content

    if command[0] == '!':
        if command == '!help' or command == '!h':
            pass
        if command.startswith('!card '):
            param = command.split(' ')
            if param[1][0].isdigit():
                karte = Card(param[1]) 
                print(f'{karte.name}')
            else:
                karte = Card(param[1]) 
                print(f'{karte.name}')
            response = f'Karte erkannt: {karte.name}'
            await message.channel.send(response)




client.run(token)