import discord, keyConfig
from discord.ext import commands

from riotwatcher import LolWatcher
lol_watcher = LolWatcher(keyConfig.RiotKey)

class Elo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='elo')
    async def show_elo(self, ctx, *nomeinvocador):
        region = 'br1'
        nomeinvocador = " ".join(nomeinvocador)
        invocadorDados = lol_watcher.summoner.by_name(region, nomeinvocador)
        rank = lol_watcher.league.by_summoner(region, invocadorDados['id'])
        summonerName = invocadorDados['name']
        
        if len(rank) == 0:
            rankedStatus = (f"O player {summonerName} não jogou nas filas SOLOQ OU FLEX")
        else:
            divisao = rank[0]['rank']
            fila = rank[0]['queueType']
            elo = rank[0]['tier']
            if fila == 'RANKED_SOLO_5x5':
                fila = 'SoloQ'
            elif fila == 'RANKED_FLEX_SR':
                fila = 'FLEX'
            rankedStatus = (f"O player {summonerName} está {elo} {divisao} na {fila}")

            eloEmbed = discord.Embed(
                title = summonerName,
                description = rankedStatus,
                colour = 16753920
            )

            eloEmbed.set_thumbnail(url=(f'https://ddragon.leagueoflegends.com/cdn/11.14.1/img/profileicon/{invocadorDados["profileIconId"]}.png'))
            eloEmbed.set_image(url='https://e0.pxfuel.com/wallpapers/134/516/desktop-wallpaper-league-of-legends-player-avatar-icon-logo-league-of-legend-freljord-logo-legend-logo.jpg')
            await ctx.send(embed = eloEmbed)
