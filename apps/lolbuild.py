import discord
from discord.ext import commands
import requests
import random

versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
latest_version = versions[0]


url_champ = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/pt_BR/champion.json"
data_champ = requests.get(url_champ).json()
champs = data_champ["data"]

url_runa =  f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/pt_BR/runesReforged.json"
data_runa = requests.get(url_runa).json()
runas = data_runa

todas_runas = []
for path in data_runa:
    slot_primario = path['slots'][0]
    for rune in slot_primario["runes"]:
          rune_name = rune["name"]
          rune_icon = rune["icon"]
          todas_runas.append({
                "path": path["name"],
                "name": rune_name,
            })


class Lol(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
     @commands.command()
     async def lolbuild(self, ctx):
          campeao = random.choice(list(champs.keys()))
          info = champs[campeao]
          tipo = info['tags'][0] if info['tags'] else 'Desconhecido'
          runa = random.choice(todas_runas)
          imagem = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/img/champion/{campeao}.png"

          buildlol = discord.Embed(
               title = 'Build aleatória',
               description= 'Seleciona uma runa principal e um campeão aleatório do League of Legends.',
               color = discord.Color.purple()
          )
          buildlol.add_field(name = 'Nome', value = f"**{info['name']}**", inline = False)
          buildlol.add_field(name = 'Runa', value = f"**{runa['name']}**", inline = False)
          buildlol.set_thumbnail(url=imagem)
          
          await ctx.reply(embed=buildlol)


async def setup(bot):
    await bot.add_cog(Lol(bot))