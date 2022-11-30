"""
Example Discord bot using Discord.py 1.7.3
To run the newest features including app commands, modals, buttons, and more be sure to use Discord.py 2.0.0 or greater
Some library calls will need to be edited to suppor this change, so be sure to look at the breaking changes documentation here:
https://discordpy.readthedocs.io/en/stable/migrating.html
"""

import discord
from discord.ext import commands
from os import listdir
from os.path import dirname, abspath, join

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            allowed_mentions=discord.AllowedMentions(everyone=True),
			case_insensitive = True, 
			command_prefix = ["dpy "], 
			strip_after_prefix = True,
			intents = discord.Intents.all()
		)

    # Called on run sequence
    async def on_ready(self):
        print("Everything's all ready to go~", bot.user)
        # Change the presence of the bot allowing for a more dynamic look. Most people will put the bot's prefix and help command here
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Bot making'))

    async def startup(self):
        """Anything that needs to be ran on start"""
        await self.wait_until_ready()
        #await self.tree.sync()


    async def setup_hook(self):
        '''Initialize the cogs'''
        root_dir = dirname(abspath(__file__))
        cogs_dir = join(root_dir, "cogs")
        # Iterate through the folder 'cogs' to find any files named tools
        cogs = [f"cogs.{filename[:-3]}" for filename in listdir(cogs_dir) if filename.endswith(".py")]
        for cog in cogs:
            # Load the commands in each file to the bot
            await bot.load_extension(cog)
        
        self.loop.create_task(self.startup())

# Starting point for the bot to allow cogs to be loaded in.
if __name__=='__main__':
    bot = Bot()
    bot.remove_command('help')

    # This allows the bot to start and connect to the discord api registering it.
    # It would be best to keep the bot token in an env
    bot.run('')  