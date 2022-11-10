from discord.ext import commands
import discord
import datetime
import contextlib
from .help_command import MyHelp

class HelpCog(commands.Cog, name="Help"):
    """Shows help info for commands and cogs"""

    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelp()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

async def setup(bot: commands.Bot):
    await bot.add_cog(MyHelp(bot))