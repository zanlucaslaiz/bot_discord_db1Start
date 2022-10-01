import discord
import config
import asyncio


intents = discord.Intents.default()
intents.message_content = True
client =discord.Client(intents=intents)

@client.event
async def on_ready():
    print('online.')
    
@client.event
async def on_message(mensagem):
    if mensagem.author == client.user:
        return
    await mensagem.channel.send('Bem-vindo!')

async def setup():
    print('Setting up...')

async def main():  
    await setup()
    await client.start(config.TOKEN)

asyncio.run(main())