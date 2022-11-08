from discord.ext import commands
import discord
import glob

class Get(commands.Cog, name="Download"):
    """For Downloading listed files"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def get(self, ctx: commands.Context, lab, week, problem):
        """
        Get the .pdf files for the desired problem

        Example: 
        `haya get BG75 3 A`
        `haya get BG75 5 D`
        """
        problem = problem.upper()
        lab = lab.upper()
        file_path = glob.glob("./problems/*/" + lab + '-week-' + week + '-prob-' + problem + '.pdf')
        
        await ctx.send(file=discord.File(file_path[0]))

async def setup(bot: commands.Bot):
    await bot.add_cog(Get(bot))