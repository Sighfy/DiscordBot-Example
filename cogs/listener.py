import discord
from discord.ext import commands


class Listeners(commands.Cog, name="listener"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener('on_message')
    # This is how listener(s)
    # on_message acts as a listener to all messages
    # While it is possible to have multiple listeners there can only be one on_message listener.
    # What this means is that if you have multiple message items you want to listen to, you will have to stack them here.
    # This is also why I prefer to have an entire file dedicated to just this listener
    async def on_message(self, message: discord.Message):
        # We do not want the bot to reply to itself or other bots
        if message.author == self.bot.user:
            return

        # If the bot is mentioned, it will respond saying hi
        if message.author.bot == False and self.bot.user.mentioned_in(message) and len(message.content) == len(self.bot.user.mention):
            await message.channel.send(f'Hello! I am {self.bot.user.mention}!')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Listeners(bot))