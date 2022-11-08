from discord.ext import commands
from typing import Optional, Set
import discord

class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return f"{self.context.clean_prefix}{command.qualified_name} {command.signature}"

    async def _help_embed(
        self, title: str, description: Optional[str] = None, mapping: Optional[str] = None,
        command_set: Optional[Set[commands.Command]] = None
    ):
        embed = discord.Embed(title=title)
        if description:
            embed.description = description
        # avatar = self.context.bot.user.avatar or self.context.bot.user.default_avatar
        # embed.set_author(name=self.context.user.name, icon_url=avatar.url)
        if command_set:
            # show help about all commands in each cog
            filtered = await self.filter_commands(command_set, sort=True)
            for command in filtered:
                embed.add_field(
                    name=self.get_command_signature(command), 
                    value=command.short_doc or "...", 
                    inline=False
                )

        if mapping:
            for cog, command_set in mapping.items():
                filtered = await self.filter_commands(command_set, sort=True)
                if not filtered:
                    continue
                name = cog.qualified_name if cog else "No category"
                # \u2002 us an en-space
                cmd_list = "\u2002".join(
                    f"`{self.context.clean_prefix}{cmd.name}`" for cmd in filtered
                )
                value = (
                    f"{cog.description}\n{cmd_list}"
                    if cog and cog.description
                    else cmd_list
                )
                embed.add_field(name=name, value=value)
        return embed

    async def send_bot_help(self, mapping: dict):
        embed = await self._help_embed(
            title="Commands",
            description=self.context.bot.description,
            mapping=mapping,
        )
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = await self._help_embed(
            title=command.qualified_name,
            description=command.help,
            command_set=command.commands if isinstance(command, commands.Group) else None
        )
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog: commands.Cog):
        embed = await self._help_embed(
            title=cog.qualified_name,
            command_set=cog.commands, 
            description=cog.description,
        )
        await self.get_destination().send(embed=embed)



class Help(commands.Cog, name="Help"):
    """Shows help inf about commands"""

    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))