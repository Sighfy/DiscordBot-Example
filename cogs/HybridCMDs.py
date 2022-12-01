"""
Please check out cmds.py before this when learning.

Hybrid commands are commands that will work as both prefix and app commands.
They are usually written the same as prefix commands, however they do have different restrictions and sometimes you will also need ti import the app commands to deal with error checking and app command specific items.

"""
#get started like always with imports and cog setup

import discord
from discord.ext import commands

class HybridCMDs(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(HybridCMDs(bot))