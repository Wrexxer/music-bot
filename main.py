import discord
from discord.ext import commands 
import os
import hikari

bot = hikari.GatewayBot(token='OTcyNTQ0NTA4MDE5NDkwODM3.Ynampw._S0QGNv67GdpxSUtOeTMMK48ROE')


from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='-')

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))



bot.run("OTcyNTQ0NTA4MDE5NDkwODM3.Ynampw._S0QGNv67GdpxSUtOeTMMK48ROE")


