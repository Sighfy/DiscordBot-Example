"""
Example Discord bot using Discord.py 2.1.0
To run the newest features including app commands, modals, buttons, and more be sure to use Discord.py 2.0.0 or greater
Some library calls will need to be edited to suppor this change, so be sure to look at the breaking changes documentation here:
https://discordpy.readthedocs.io/en/stable/migrating.html
"""

import discord
from discord.ext import commands
from os import listdir
from os.path import dirname, abspath, join, splitext
from json import load

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
        # Usually not a good idea to handle tree syncing automatically on start.
        # This can easily be moved to a different function in another cog.
        # I recomend creating a sync, unsync, and resync command.
        # But for now, this will do for the example.
        # Disclaimer: It can take 24hours for slash commands to populate. Many times its only a few minutes, but keep this in mind.
        print("syncing tree")
        await self.tree.sync()


    async def setup_hook(self):
        '''Initialize the cogs'''
        # Iterate through the folder 'cogs' to find any files named tools
        cogs = [f"cogs.{filename[:-3]}" for filename in listdir(cogs_dir) if filename.endswith(".py")]
        for cog in cogs:
            # Load the commands in each file to the bot
            await bot.load_extension(cog)
        # allow an area for startup tasks to be created
        self.loop.create_task(self.startup())

# These two functions below serve as the config loader
def cred(file: str) -> dict:
    with open(join(config_dir, file), "r") as f:
        return load(f)

def load_config() -> dict:
    config = dict()
    for file in listdir(config_dir):
        filename, ext = splitext(file)
        if ext == ".json":
            config[filename] = cred(file)
    return config

# Starting point for the bot to allow cogs to be loaded in.
if __name__=='__main__':
    bot = Bot()

    #create the directory locations
    root_dir = dirname(abspath(__file__))
    cogs_dir = join(root_dir, "cogs")
    config_dir = join(root_dir, "config")
    
    # How to load the config into the bot to be used to the token
    # - Create a folder in the current directory called config
    # - Create token.json and add your bot token in the file
    bot.config = load_config()

    # We will be making our own help menu, remove the default
    bot.remove_command('help')

    # This allows the bot to start and connect to the discord api registering it.
    # It would be best to keep the bot token in an env
    bot.run(token=bot.config["config"]["token"])  