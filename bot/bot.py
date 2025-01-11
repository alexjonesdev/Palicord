# This example requires the 'message_content' intent.
#---==IMPORTS==---
import discord, logging.config, asyncio
from discord.ext import commands
from modules import rand

#---==CONFIGURATION==---
description = '''A bot service made from the discord.py library. Commands:'''
command_prefix = '!'
logging_config = 'logging.conf'
primary_logger = 'discord'

#---==INITIALIZATION==---
#Set up logging
logging.config.fileConfig(logging_config)
logger = logging.getLogger(primary_logger)

#Set up intents
intents = discord.Intents.default()
intents.message_content = True

#Set up the bot
bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)

#Load modules
logger.info('Loading modules...')
# bot.add_cog(rand.rand(bot))
logger.info('MODULE LOADED: random')
logger.info('Modules loaded.')

#---==EVENTS==---
@bot.event
async def on_ready():
    logger.info('Bot has logged in as %s:%s', bot.user.name, bot.user.id)

#Load the token from a file and log the bot in
f = open("bot.token", "r")
token = f.read()
f.close()

async def load_modules():
    logger.info('Loading modules...')
    await bot.load_extension('modules.rand')
    logger.info('MODULE LOADED: random')
    logger.info('Modules loaded.')

async def main():
    async with bot:
        await load_modules()
        print([c.name for c in bot.get_cog('rand').get_commands()])
        await bot.start(token)

asyncio.run(main())