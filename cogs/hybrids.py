"""
Please check out tools.py before this when learning.

Hybrid commands are commands that will work as both prefix and app commands.
They are usually written the same as prefix commands, however they do have different restrictions and sometimes you will also need ti import the app commands to deal with error checking and app command specific items.

"""
#get started like always with imports and cog setup

import discord
from discord.ext import commands
from datetime import datetime

class HybridCMDs(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot

    # A check used to ensure that the bot has the ability to send messages in a channel
    # the use of hybrid_commands instead of command makes it a hybrid haha
    # To prevent spamming, it's good to include a cooldown. In this case it is 5 seconds per use. 
    @commands.bot_has_permissions(send_messages = True)
    @commands.hybrid_command(name="help", description="A help menu example")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx: commands.Context):
        '''Show a useful help menu'''
        bot_pfp = self.bot.user.avatar
        user_pfp = ctx.message.author.avatar
        # This is how you build an embeded messsage. Play arounf with the inline option to see how to format the embed.
        embed = discord.Embed(title='Help Menu', description='Not much to see here', timestamp=datetime.utcnow(), color=discord.Color.blurple())
        embed.set_author(name=f'{ctx.author}', icon_url=user_pfp)
        embed.add_field(name='Field 1', value='test1', inline=True)
        embed.add_field(name='Field 2', value='test2', inline=False)
        embed.add_field(name='Field 3', value='test3', inline=False)
        embed.set_footer(text='footer text', icon_url=bot_pfp)
        embed.set_thumbnail(url='https://i.insider.com/602ee9ced3ad27001837f2ac?width=2000&format=jpeg&auto=webp')

        # This is similar to print, but will send the response to discord as a response to the command invokation.
        # In this case it is an embed
        # Using reply instead of send will have the bot reply to whoever invoked the message
        await ctx.reply(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(HybridCMDs(bot))