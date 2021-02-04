import discord
from discord.ext import commands
import os
import requests
import json
import sys
import traceback
import datetime
import asyncio
import random
import tracemalloc


class GiveawayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='gcreate', aliases=['giveawaycreate', 'giveawaystart'])
    @commands.has_role("Giveaways")
    @commands.guild_only()
    async def gcreate(self, ctx, mins: int, *, prize: str):
        embed = discord.Embed(
            title='Giveaway!', description=f'{prize}', colour=random.randint(0, 16777216))
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins*60)
        embed.add_field(name='Ends At:', value=f'{end} UTC')
        embed.set_footer(text=f'Ends {mins} mintue(s) from now!')
        my_msg = await ctx.send(embed=embed)
        await my_msg.add_reaction('🎉')
        await asyncio.sleep(mins*60)
        new_msg = await ctx.channel.fetch_message(my_msg.id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        await ctx.send(f'Congratulations! {winner.mention} won {prize}')


def setup(bot):
    bot.add_cog(GiveawayCog(bot))
