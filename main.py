import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import random
import re

# Carrega token do .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# Configura intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Função para carregar automaticamente todas as cogs
async def load_cogs():
    cogs_path = os.path.join(BASE_DIR, "cogs")
    for file in os.listdir(cogs_path):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
            print(f"Cog carregada: {file}")

# Evento para quando o bot ligar
@bot.event
async def on_ready():
    print(f'{bot.user} conectado!')

# Evento para responder mensagens que contenham "euthanasia"
@bot.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author.bot:
        return

    if "euthanasia" in message.content.lower():
        await message.reply("Só ano que vem :sob:")

    # Faz os outros comandos continuarem funcionando
    await bot.process_commands(message)





# Função principal para iniciar o bot
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

# Roda o bot
asyncio.run(main())