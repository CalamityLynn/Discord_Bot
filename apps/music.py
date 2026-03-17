import discord
from discord.ext import commands
import asyncio
from yt_dlp import YoutubeDL

YTDL_OPTIONS = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "quiet": True,
}

FFMPEG_OPTIONS = {
    "options": "-vn"
}

class Music(commands.Cog):
     def __init__(self, bot):
        self.bot = bot
        self.queue = [] 
        self.is_playing = False
        self.voice_client = None

     @commands.command()
     async def play(self, ctx, url):
        # conecta automaticamente se não estiver no canal
        if not self.voice_client:
            if ctx.author.voice:
                self.voice_client = await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Conecte-se a uma call!")
                return

        self.queue.append(url)
        play = discord.Embed(
            title = 'Música Adicionada:',
            color = discord.Color.purple()
        )
        play.add_field(name = '', value =str(url), inline = True)
     
        await ctx.reply(embed=play)

        if not self.is_playing:
            self.is_playing = True
            while self.queue:
                current_url = self.queue.pop(0)

                YDL = YoutubeDL(YTDL_OPTIONS)
                info = YDL.extract_info(current_url, download=False)
                url2 = info['url']

                source = discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
                self.voice_client.play(source)

                while self.voice_client.is_playing() or self.voice_client.is_paused():
                    await asyncio.sleep(1)

            self.is_playing = False

     @commands.command()
     async def skip(self, ctx):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.stop()

            skip = discord.Embed()
            skip.add_field(name='', value="⏭️ Música pulada", inline=True)
            await ctx.send(embed=skip)

     @commands.command()
     async def pause(self, ctx):
         if self.voice_client and self.voice_client.is_playing():
               self.voice_client.pause()
               pause = discord.Embed()
               pause.add_field(name = '', value = "⏸️ Música pausada", inline = True)
               await ctx.reply(embed=pause)

     @commands.command()
     async def resume(self, ctx):
          if self.voice_client and self.voice_client.is_paused():
               self.voice_client.resume()
               resume = discord.Embed()
               resume.add_field(name = '', value = "▶️ Música retomada", inline = True)
               await ctx.reply(embed=resume)

     @commands.command()
     async def queue(self,ctx):
          if self.queue:
               fila = "\n".join(f"{i+1}. {url}" for i, url in enumerate(self.queue))
               queue = discord.Embed(
                   title = 'Queue',
                   color = discord.Color.purple()
               )
               queue.add_field(name= '', value =f"Fila:\n{fila}", inline = True) 

               await ctx.reply(embed=queue)
          else:
               queue = discord.Embed()
               queue.add_field(name= '', value = 'Fila vazia!')
               await ctx.reply(embed=queue)

     @commands.command()
     async def remove(self, ctx, index: int):
          if 0 < index <= len(self.queue):
               musica = self.queue.pop(index-1)

               remove = discord.Embed()
               remove.add_field(name='', value=f"Removida da fila: {musica}.")
               await ctx.send(embed=remove)
          else:
               await ctx.send("Música não encontrada.")

     @commands.command()
     async def leave(self, ctx):
          if self.voice_client:
               await self.voice_client.disconnect()
               self.voice_client = None
               self.queue.clear()
               self.is_playing = False
               leave = discord.Embed()
               leave.add_field(name='',value='Desconectado.')
               await ctx.send(embed=leave)

async def setup(bot):
    await bot.add_cog(Music(bot))