"""
Example Discord bot using Discord.py 1.7.3
To run the newest features including app commands, modals, buttons, and more be sure to use Discord.py 2.0.0 or greater
Some library calls will need to be edited to suppor this change, so be sure to look at the breaking changes documentation here:
https://discordpy.readthedocs.io/en/stable/migrating.html
"""

import os
import discord
from discord.ext import commands


# Register the prefix and intents of the bot.
prefix = ["dpy"]
intents = discord.Intents.default()
intents.members = True
# Define the bot to be used later to create events and request form discord api information
bot = commands.Bot(command_prefix=prefix, intents=intents)
# This is optional, but since I have defined the help command in another cog, it would be best to remove the default help command
bot.remove_command('help')

# Called on .run sequence
@bot.event
async def on_ready():
    print("Everything's all ready to go~", bot.user)
    # Change the presence of the bot allowing for a more dynamic look. Most people will put the bot's prefix and help command here
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Bot making'))


# This is how commands are made
@bot.event
# on_message acts as a listener to all messages
# This is not ideal in 2.0.0 but in 1.7.3 this will suffice for a small private bot
async def on_message(message):
    # We do not want the bot to reply to itself or other bots
    if message.author == bot.user:
        return

    # Whenever the bot is tagged, respond with its prefix
    if message.content.startswith(f'<@!{bot.user.id}>') and len(message.content) == len(f'<@!{bot.user.id}>'):
        await message.channel.send(f'My prefix here is `{prefix}`')

    # print to console the user and what they typed
    '''
    print(message.author)
    print(f'The message's content was: {message.content}')
    '''
    # Allows the bot to send messages from commands to discord
    # This function processes the commands that have been registered to the bot and other groups
    # Without this coroutine, none of the commands will be triggered
    await bot.process_commands(message)

# Starting point for the bot to allow cogs to be loaded in.
if __name__=='__main__':
    # Iterate through the folder 'cogs' to find any files named tools
    cogs = ['cogs.tools']
    for cog in cogs:
        # Load the commands in each file to the bot
        bot.load_extension(cog)

# This allows the bot to start and connect to the discord api registering it.
# It would be best to keep the bot tokem in an env like I have shown below, but if that is not an option, just app the token below. -> bot.run("token")
bot.run(os.getenv('shush'))  