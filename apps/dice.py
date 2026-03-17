import discord
from discord.ext import commands
import random
import re

class Dice(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

     # Roda dados e soma seus valores
     @commands.Cog.listener("on_message")
     async def on_message(self, message):

     # Ignora mensagens do próprio bot
          if message.author.bot:
               return

          # Regex para detectar mensagens do tipo "XdY" (ex: 2d20)
          match = re.search(r"(\d+)d(\d+)", message.content.lower())
          if match:
               quantidade = int(match.group(1))
               lados = int(match.group(2))

               # Limites de segurança
               if quantidade > 10000 or lados > 1000:
                    await message.channel.send("Limite: 10000 dados, 1000 lados.")
                    return

               # Rolagem dos dados
               resultados = [random.randint(1, lados) for _ in range(quantidade)]
               total = sum(resultados)

               # Formata a resposta
               embed = discord.Embed(
                    title = '🎲Rolls',
                    color = discord.Color.purple()
               )

               
               embed.add_field(name = '🎲Rolagem:', value = message.content, inline = True)
               embed.add_field(name = '🔃Resultados:', value = ', '.join(map(str, resultados)), inline = True)
               embed.add_field(name = '➕Total:', value = str(total), inline = True)
          
               await message.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Dice(bot))