from discord.ext import commands

class Gerais(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
    
     @commands.command()
     async def ola(self, ctx):
          await ctx.send(f'Olá, {ctx.author.name}!')

     @commands.command()
     async def say(self, ctx, *, mensagem):
          await ctx.send(mensagem)
      
async def setup(bot):
    await bot.add_cog(Gerais(bot))

