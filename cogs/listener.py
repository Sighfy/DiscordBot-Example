import discord
from discord.ext import commands


class Listeners(commands.Cog, name="listener"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener('on_message')
    # This is how commands are made
    # on_message acts as a listener to all messages
    # This is not ideal in 2.0.0 but in 1.7.3 this will suffice for a small private bot
    async def on_message(self, message: discord.Message):
        # We do not want the bot to reply to itself or other bots
        if message.author == self.bot.user:
            return

        # If the bot is mentioned, it will respond saying hi
        if message.author.bot == False and self.bot.user.mentioned_in(message) and len(message.content) == len(self.bot.user.mention):
            await message.channel.send(f'Hello! I am {self.bot.user.mention}!')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Listeners(bot))