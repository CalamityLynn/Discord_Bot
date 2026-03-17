from discord.ext import commands
import discord
import math

class Calc(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
    
     @commands.command()
     async def soma(self, ctx, *numeros: float):
          resultado = sum(numeros)

          soma = discord.Embed(
               title = '➕Soma',
                    color = discord.Color.purple()
          )
          soma.add_field(name='🔢Valores', value=str(numeros), inline=True)
          soma.add_field(name='🟰Soma', value=str(resultado), inline=True)
               
          await ctx.reply(embed=soma)

     @commands.command()
     async def mult(self, ctx, *numeros: float):
          resultado = math.prod(numeros)

          mult = discord.Embed(
               title = '✖️Multiplicação',
                    color = discord.Color.purple()
          )
          mult.add_field(name='🔢Valores', value=str(numeros), inline=True)
          mult.add_field(name='🟰Produto', value=str(resultado), inline=True)
               
          await ctx.reply(embed=mult)


     @commands.command()
     async def div(self, ctx, num1: float, num2: float):
          resultado = num1 / num2
          div = discord.Embed(
               title = '➗Divisão',
                    color = discord.Color.purple()
          )
          div.add_field(name='🔢Valores', value=f'{num1}, {num2}', inline=True)
          div.add_field(name='🟰Quociente', value=str(resultado), inline=True)
               
          await ctx.reply(embed=div)



async def setup(bot):
    await bot.add_cog(Calc(bot))