from discord.ext import commands
import os
import discord
import glob

class List(commands.Cog, name="Show"):
    """Commands for showing purposes"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def list(self, ctx: commands.Context, flag=None):
        """
        Listing the available folders that has all the problems
        
        Example: 
        `haya list` for showing folders only
        `haya list files` for showing folders with files
        """
        dir1 = os.listdir("./problems")
        dir1.sort()
        dir2 = glob.glob("./problems/*/*.pdf")
        dir2.sort()
        counter = 0

        arr = list()
        if flag == 'files':
            for folder in dir1:
                arr.append("📁 " + folder + '\n')
                for i in range(0 + 6*counter,6 + 6*counter):
                    arr.append(os.path.basename(dir2[i]) + '\n')
                counter += 1
        else:
            for folder in dir1:
                arr.append("📁 " + folder + '\n')

        embed = discord.Embed(title="List of Available Problems", colour=discord.Colour.from_str('#fdf0b3'))
        embed.add_field(
            name="BG75", 
            value="".join(arr), 
            inline=False
        )
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(List(bot))