from discord.ext import commands

class Ping(commands.Cog, name="Testing"):
    """
    `ping` 
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """
        Checks for a response from the bot

        Example: 
        `haya ping`        
        """
        await ctx.send("I'm late `{0}ms` to *nii-sama*.".format(round(self.bot.latency, 3)))

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))