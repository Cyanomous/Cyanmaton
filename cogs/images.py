import discord
from discord.ext import commands
import os
import numpy
import requests
import json
import random
import json
import sys
import traceback
import importlib
from math import *
from cogs.lists import colour
import aiohttp
import datetime
from cogs.lists import poke_images
from cogs.lists import slap_images
from cogs.lists import punch_images
from cogs.lists import sleep_images
from cogs.lists import nou_images


class ImagesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="pat")
    async def pat(self, ctx, user: discord.Member = None):
        if user is None:
            return await ctx.send(f"Provide a person to {ctx.command.name} please!")
        embed = discord.Embed(
            title='A Nice Pat', description=f"**{ctx.author}** gently pats **{user.display_name}** on the head.", colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url="https://media1.tenor.com/images/8c1a53522a74129607b870910ac288f9/tenor.gif?itemid=7220650")
        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="empathy")
    async def empathy(self, ctx):
        embed = discord.Embed(
            title='Empathy Banana', description=f"Don't worry **{ctx.author}** Empathy Banana is here for you.", colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url="https://media.discordapp.net/attachments/802185231993405451/804415975533051945/Empathy_Banana.png?width=585&height=585")
        embed.set_footer(
            text=f"{ctx.author.name} summoned Empathy Banana", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="poke")
    async def poke(self, ctx, user: discord.Member = None):
        if user is None:
            return await ctx.send(f"Provide a person to {ctx.command.name} please!")
        embed = discord.Embed(
            title='Poke!', description=f"**{ctx.author}** pokes **{user.display_name}**.", colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url=random.choice(poke_images))
        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="slap")
    async def slap(self, ctx, user: discord.Member = None):
        if user is None:
            return await ctx.send(f"Provide a person to {ctx.command.name} please!")
        embed = discord.Embed(
            title='Hard slap.', description=f"**{ctx.author}** slaps **{user.display_name}**.", colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url=random.choice(slap_images))
        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="punch")
    async def punch(self, ctx, user: discord.Member = None):
        if user is None:
            return await ctx.send(f"Provide a person to {ctx.command.name} please!")
        embed = discord.Embed(
            title='Punched.', description=f"**{ctx.author}** punches **{user.display_name}**.", colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url=random.choice(punch_images))
        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="sleep")
    async def sleep(self, ctx, user: discord.Member = None):
        if user is None:
            return await ctx.send(f"Provide someone who wants too {ctx.command.name} please!")
        embed = discord.Embed(
            title='Go to sleep.', description=f"**{user.display_name}** you should go to sleep.", colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url=random.choice(sleep_images))
        embed.set_footer(
            text=f"{ctx.author.name} wants you to go to sleep.", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="notworking")
    async def notworking(self, ctx):
        embed = discord.Embed(
            title='Its not working', description=f"Not working?", colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url=('https://media.discordapp.net/attachments/802185231993405451/805564909537984512/its-not-working.png?width=584&height=584'))
        embed.set_footer(
            text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="nou")
    async def nou(self, ctx):
        embed = discord.Embed(
            title='NoU', colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_image(
            url=random.choice(nou_images))
        embed.set_footer(
            text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ImagesCog(bot))
