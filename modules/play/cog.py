from discord.ext import commands
import yt_dlp
import discord

class Music(commands.Cog, name="Music"):
    """
    `play` 
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx: commands.Context, url):
        """
        Play a music from youtube

        Example: 
        `haya play <url>`        
        """
        # Debug
        channel = ctx.author.voice.channel
        if not channel:
            await ctx.send("You need to be connected in a voice channel to use this command!")
            return
        await channel.connect()




async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))