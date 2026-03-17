import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz

diahora = "06:00"
tardehora = "15:00"
noitehora = "19:00"

canal_id = 1134963949608116356

class Saudations(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
          self.verificar_horario.start()

     @tasks.loop(seconds=60)
     async def verificar_horario(self):
          agora = datetime.now().strftime("%H:%M")
     
          if agora == diahora:
               canal = self.bot.get_channel(canal_id)
               if canal:
                await canal.send("Bom dia!")

          if agora == tardehora:
               canal = self.bot.get_channel(canal_id)
               if canal:
                await canal.send("Boa tarde!")

          if agora == noitehora:
               canal = self.bot.get_channel(canal_id)
               if canal:
                await canal.send("Boa noite!:sleeping:")

     @verificar_horario.before_loop
     async def before_loop(self):
          await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(Saudations(bot))

