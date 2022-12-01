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