from discord.ext import commands

class Ping(commands.Cog, name="Testing"):
    """Feedback commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """
        Checks for a response from the bot

        Example: 
        `haya ping`        
        """
        await ctx.send("Pong")

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))