import discord
from discord.ext import commands 

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
```
General commands:
-help - displays al the available commands
-play - play a song
-queue - shows the current queue
-skip - skip the current song
-clear - stops the music and clears the queue
-leave - disconnects the bot from the voice channel
-pause - pauses the current song or resumes is if it is paused
-resume - resumes the current song
```
"""
        self.text_channel_text = []
    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)
    
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)
    
    @commands.command(name="help", aliases=["h", "hl"], help="Display all the available comands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
