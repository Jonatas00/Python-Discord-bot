import discord
from discord.ext import commands

class Gerais(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='hello', description='Comando que retorna Hello')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Olá, meu nome é Astêmio!")
