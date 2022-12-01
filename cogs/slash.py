"""
After you have learned about normal prefix commands from tools.py, you can check out how interaction or slash commands work.

It's a bit different and one way to think about it is this way, with prefix commands you can get input from the user after the command has been invoked. While this is also true with slash, slash has better input control since it displays it in the discord prompt.

Honestly you'll probably deal with hybrid commands the most, but in case you ever want a command to be interaction only, this is the way to do it
"""
import discord
from discord.ext import commands
from discord import app_commands

class slash(commands.Cog, name="slash"):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
    
    # the usage of @commands has been replaced with @app_commands
    # ctx has also been replaced with interaction and so on with other changes.
    @app_commands.command(name="quickpoll", description="A small example poll")
    @app_commands.describe(question="The question of the quickpoll.")
    @app_commands.checks.bot_has_permissions(send_messages=True)
    async def poll(self, interaction: discord.Interaction, question: str):
        """creates a quickpoll"""
        await interaction.response.send_message(content=f"{question}", allowed_mentions=discord.AllowedMentions(everyone=False, users=True, roles=False))
        message = await interaction.original_response()
        # the easest way to get information from a poll is by using the reactions in discord. Of course reactions can be used anywhere, but it's easy to show an example with a poll
        await message.add_reaction(":arrow_up:")
        await message.add_reaction(":arrow_down:")
    
async def setup(bot:commands.Bot):
    await bot.add_cog(slash(bot))