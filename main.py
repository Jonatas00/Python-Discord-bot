import discord, keyConfig
from discord.ext import commands
from comandos.lol import *
from comandos.gerais import *

bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

bot.add_cog(Elo(bot))
bot.add_cog(Gerais(bot))

@bot.event
async def on_ready():
    print("Online e operante!")

bot.run(keyConfig.discordKey)
