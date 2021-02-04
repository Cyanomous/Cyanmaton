import discord
from discord.ext import commands
import os
import requests
import json
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


def setup(bot):
    bot.add_cog(HelpCog(bot))
