"""
"ARandomBot" Discord Bot source code. This is public and can be changed by anyone.
Contributions are welcome and can be PR'd to the main repository or run the bot 
yourself for your own purposes!

@knvtva
"""


import discord
import platform
import os
import random



from discord.ext import commands, tasks
from Utils.Config import ReadConfigFile
from Utils.Logger import logger

# Call ReadConfigFile
Config = ReadConfigFile.ReadJSONFile()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print("-----------------------------------------------")
    logger.info(f"Successfully logged in as {bot.user.name}")
    logger.info(f"discord.py API version: {discord.__version__}")
    logger.info(f"Python version: {platform.python_version()}")
    logger.info(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-----------------------------------------------")

    status_task.start()

@tasks.loop(minutes=1.0)
async def status_task():
    statues = ["ARandomBot is watching you.", "@knvtva", "woahoahwaohwoahdiscordbottt"]

    await bot.change_presence(activity=discord.activity.Game(random.choice(statues)))
                              
                           
bot.run(Config['token'])