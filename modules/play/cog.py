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
        print("play command used")
        try:
            userState = ctx.author.voice
            if not userState:
                await ctx.send("You need to be connected in a voice channel to use this command!")
                return
            print("user has entered the voice chat ")
            await userState.channel.connect()
        except:
            print("something's broken")

async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))