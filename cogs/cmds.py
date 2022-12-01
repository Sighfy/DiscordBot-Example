"""
Cogs are essentially classes that are designed to be read and subsequently registered to the bot. Cogs can contain listeners, commands, groups, etc

Below I have written a basic ping, help, and info command.

I've also used the comments to remove items and parts. Feel free to uncomment to play around with how it displays.

All of the commands here are the standard prefix commands
"""
import discord
from discord.ext import commands
from datetime import datetime

# This class and the setup definition below are a must when creating cogs as they interact with the load_extenssion call in discordbot.py / main
# It is best to go in this format:
# class <file name>(<type to register>)
class tools(commands.Cog):
    # We want to initialize the bot interaction to be used later on
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ping')
    #async def ping(self, ctx: commands.Context, *, text: str):
    async def ping(self, ctx: commands.Context):
        '''Get the bot's current latency.'''
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    # Register and name the specific command
    @commands.command(name='help')
    # One of the many checks that can be used. IF the bot does not have permission to send messages, it will raise an error
    @commands.bot_has_permissions(send_messages=True)
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

    @commands.command(name='info')
    async def info(self, ctx: commands.Context):
        '''Show a useful info menu'''
        bot_pfp = self.bot.user.avatar
        user_pfp = ctx.message.author.avatar
        guild_creation = str(ctx.guild.created_at).split()[0] # will only show data and not time
        current_utc = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S") # shows the current time in UTC format
    
        embed = discord.Embed(title=f'{ctx.guild.name}', description='Information on the server and bot', timestamp=datetime.utcnow(), color=0x000000)
        embed.set_author(name=f'{ctx.author}', icon_url=user_pfp)
        embed.add_field(name='Server created at', value=f'{guild_creation}', inline=False)
        embed.add_field(name='Number of members', value=f'{ctx.guild.member_count}', inline=False)
        # embed.add_field(name='Server Owner', value=f'{ctx.guild.owner}', inline=False)
        # embed.add_field(name='Server Region', value=f'{ctx.guild.region}')
        # embed.add_field(name='Server ID', value=f'{ctx.guild.id}', inline=False)
        embed.add_field(name='UTC time now', value=current_utc)
        # embed.add_field(name='Number of Servers', value=f'{len(self.bot.guilds)}', inline=False)
        embed.set_footer(text=f'{ctx.author}', icon_url=bot_pfp)
        # embed.set_thumbnail(url=<add a link or path to image here>)

        await ctx.send(embed=embed)

        # guilds documentation
        # https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild

async def setup(bot: commands.Bot):
    await bot.add_cog(tools(bot))