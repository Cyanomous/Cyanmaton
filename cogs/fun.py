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
from cogs.lists import cowboy_sayings
from cogs.lists import roasts
from cogs.lists import colour
from cogs.lists import lenny_faces
import aiohttp
from cogs.lists import _8ballresponses


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="8ball", aliases=['advice', 'badadvice'])
    async def advice(self, ctx, *, question):
        e = discord.Embed(color=random.randint(0, 16777216))
        e.add_field(name="Your Question:", value=question, inline=False)
        e.add_field(name="The Answer:", value=random.choice(
            _8ballresponses), inline=False)
        await ctx.send(embed=e)

    @commands.command(name='person', aliases=['thispersondoesnotexist', 'personnotexist', 'this_person_does_not_exist', 'this-person-does-not-exist', 'Person'])
    @commands.guild_only()
    async def person(self, ctx):
        if message.author == client.user:
            return
        if message.author.bot:
            return
        embed = discord.Embed(
            title='This Person Doesn\'t Exist', url="https://thispersondoesnotexist.com", colour=random.randint(0, 16777216), type="image")
        embed.set_image(
            url=f"https://thispersondoesnotexist.com/image?cum={numpy.random.rand()}")
        await ctx.send(content=None, embed=embed)

    @commands.command(name='cat', aliases=['thiscatdoesnotexist', 'catnotexist', 'this_cat_does_not_exist', 'this-cat-does-not-exist', 'Cat'])
    @commands.guild_only()
    async def cat(self, ctx):
        embed = discord.Embed(
            title='This Cat Doesn\'t Exist', url="https://thiscatdoesnotexist.com/", colour=random.randint(0, 16777216), type="image")
        embed.set_image(
            url=f"https://thiscatdoesnotexist.com/?cum={numpy.random.rand()}")
        await ctx.send(content=None, embed=embed)

    @commands.command(name='startup', aliases=['thisstartupdoesnotexist', 'startupnotexist', 'this_startup_does_not_exist', 'this-startup-does-not-exist', 'Startup'])
    @commands.guild_only()
    async def startup(self, ctx):
        embed = discord.Embed(
            title='This Startup Doesn\'t Exist', url="https://thisstartupdoesnotexist.com", colour=random.randint(0, 16777216), type="image")
        embed.set_image(
            url=f"https://thisstartupdoesnotexist.com/?cum={numpy.random.rand()}")
        await ctx.send(content=None, embed=embed)

    @commands.command(name='horse', aliases=['thishorsedoesnotexist', 'horsenotexist', 'this_horse_does_not_exist', 'this-horse-does-not-exist', 'Horse'])
    @commands.guild_only()
    async def horse(self, ctx):
        embed = discord.Embed(
            title='This Horse Doesn\'t Exist', url="https://thishorsedoesnotexist.com", colour=random.randint(0, 16777216), type="image")
        embed.set_image(
            url=f"https://thishorsedoesnotexist.com/?cum={numpy.random.rand()}")
        await ctx.send(content=None, embed=embed)

    @commands.command(name='art', aliases=['thisartdoesnotexist', 'artwork', 'this_art_does_not_exist', 'this-art-does-not-exist', 'Art'])
    @commands.guild_only()
    async def art(self, ctx):
        embed = discord.Embed(
            title='This Art Doesn\'t Exist', url="https://thisartworkdoesnotexist.com", colour=random.randint(0, 16777216), type="image")
        embed.set_image(
            url=f"https://thisartworkdoesnotexist.com/?cum={numpy.random.rand()}")
        await ctx.send(content=None, embed=embed)

    @commands.command(name='cyan')
    @commands.cooldown(rate=60, per=1, type=commands.BucketType.user)
    async def cyan(self, ctx):
        embed = discord.Embed(
            title='Cyan', colour=0x00FFFF, type="image")
        embed.set_image(
            url=random.choice(['https://media.discordapp.net/attachments/768298303108415509/801645804250464296/Cyan.png', 'https://media.discordapp.net/attachments/768298303108415509/801648526429913118/cyan.png']))
        await ctx.send(content=None, embed=embed)

    @commands.command(name='googlesearch')
    async def googlesearch(self, ctx, *, googlequestion):
        await ctx.send(f'https://lmgtfy.app/?q={googlequestion}')

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send('Why hello!')

    @commands.command(name='cyantext', aliases=['ct'])
    async def cyantext(self, ctx, *, text_to_make_cyan):
        await ctx.send(f"""```yaml
{text_to_make_cyan}```""")

    @commands.command(name='epicgamer', aliases=['epic_gamer'])
    async def epicgamer(self, ctx):
        how_epic_gamer = random.randrange(0, 101)
        embed = discord.Embed(title="How Epic Gamer Robot", colour=random.randint(0, 16777216),
                              description=f"You are {how_epic_gamer}% epic gamer :video_game:, but I am 101%")
        embed.set_footer(
            text="I see that you have found me.")
        await ctx.send(embed=embed)

    @commands.command(name='howgenius', aliases=['howsmart', 'genius'])
    async def howgenius(self, ctx):
        how_genius = random.randrange(0, 101)
        embed = discord.Embed(title="How genius you are!", colour=random.randint(0, 16777216),
                              description=f"You are {how_genius}% genius :nerd:, but I am still smarter than you!")
        await ctx.send(embed=embed)

    @commands.command(name='howdumb', aliases=['howstupid', 'dumb'])
    async def howdumb(self, ctx):
        how_dumb = random.randrange(0, 101)
        embed = discord.Embed(title="How dumb you are!", colour=random.randint(0, 16777216),
                              description=f"You are {how_dumb}% dumb.")
        await ctx.send(embed=embed)

    @commands.command(name='howsimp', aliases=['simp'])
    async def howsimp(self, ctx):
        how_simp = random.randrange(0, 101)
        embed = discord.Embed(title="How simp!", colour=random.randint(0, 16777216),
                              description=f"You are {how_simp}% simp.")
        await ctx.send(embed=embed)

    @commands.command(name='trademark', aliases=['tm', 'r'])
    async def trademark(self, ctx, stufftotm):
        await ctx.send(random.choice(f'{stufftotm}™', f'{stufftotm}®'))

    @commands.command(name='owo')
    async def cyantext(self, ctx):
        await ctx.send(f'OwO')

    @commands.command(name='lennyface', aliases=['lenny'])
    async def lennyface(self, ctx):
        await ctx.send(random.choice(lenny_faces))

    @commands.command(name='cool')
    async def cool(self, ctx):
        await ctx.send('This bot is soooo cool! Smiley Face :smiley:')

    @commands.command(name='cowboysaying', aliases=['cowboysay', 'cowsaying', 'cowboysays', 'cosa', 'cowboysayings'])
    async def cowboysaying(self, ctx):
        await ctx.send(random.choice(cowboy_sayings))

    @commands.command(name='roast', aliases=['meanthing', 'roasts'])
    async def roast(self, ctx):
        await ctx.send(random.choice(roasts))

    @commands.command(name='bot')
    async def bot(self, ctx):
        await ctx.send('Yes, this is a bot!')

    @commands.command(name='iwant', aliases=['be_passive_aggressive', 'I_want', 'Iwant', 'whatIwant'])
    async def iwant(self, ctx):
        await ctx.send('If that\'s what you want :upside_down:')

    @commands.command(name='hewants', aliases=['he_passive_aggressive', 'he_wants', 'Hewants', 'whathewants'])
    async def iwant(self, ctx):
        await ctx.send('If that\'s what he wants :upside_down:')

    @commands.command(name='userwants', aliases=['passive_aggressive', 'Wants', 'wants'])
    async def userwants(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(f'If that\'s what {member.name} wants :upside_down:')

    @commands.command(name='smile')
    async def smile(self, ctx):
        await ctx.send(':smiley:')

    @commands.command(name='coin', aliases=["flip", "coinflip", 'Coin'])
    async def coin(self, ctx):
        await ctx.send(random.choice(["Heads!", "Tails!"]))

    @commands.command(name='yesno', aliases=["YesNo", "noyes", 'NoYes', 'yes/no'])
    async def yesno(self, ctx):
        await ctx.send(random.choice(["Yes!", "No!"]))

    @commands.command(name='number', aliases=["num"])
    async def number(self, ctx):
        await ctx.send(f"Your random number is {random.randint(0, 1000000001)}")

    @commands.command(name='dice', aliases=["roll", 'rd'])
    async def dice(self, ctx, dicenum):
        dicenum = int(dicenum)
        dicenum = dicenum + 1
        await ctx.send(f"You rolled a {random.randrange(0, dicenum)}")

    @commands.command(name='backwards', aliases=['reverse'])
    async def backwards(self, ctx, *, text):
        backwardstext = text[::-1]
        await ctx.send(f'{backwardstext}')

    @commands.command(name='say', aliases=['talk'])
    @commands.guild_only()
    async def say(self, ctx, *, whattosay):
        await ctx.send(f'''{whattosay}
**-{ctx.author}**''')

    @commands.command(hidden=True)
    async def cat(self, ctx):
        """Gives you a random cat."""
        async with ctx.session.get('https://api.thecatapi.com/v1/images/search') as resp:
            if resp.status != 200:
                return await ctx.send('No cat found :(')
            js = await resp.json()
            await ctx.send(embed=discord.Embed(title='Random Cat').set_image(url=js[0]['url']))
     
    @commands.command(name="spam")
    async def spam(self,ctx, member:discord.Member):
        rannge = range(1, 40)
        await ctx.channel.send('how many times to fuck this user chose 1-40')
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
                   int(msg.content) in rannge
        msg = await self.bot.wait_for("message", check=check)
        times = int(msg.content)
        while True:
            #await ctx.channel.send(f"haha i spam  {member.mention}!")
            await member.send( "hahahhaa  i spam you :D , i fuck you hahahah")
            times = times - 1
            time.sleep(2)
            if times == 0:
                break
      @commands.command(name="calculateage")
      async def calculate_age(self, ctx):
        # getting the current date
        now = datetime.datetime.now()
        current_day = int(now.strftime('%d'))
        current_month = int(now.strftime('%m'))
        current_year = int(now.strftime('%y')) + 2000
        await ctx.author.send('Type your age in this form : yyyymmdd')
        rannge = range(19500101, 20211231)

        def check(msg):
            return msg.author == ctx.author and \
                   int(msg.content) in rannge

        msg = await self.bot.wait_for("message", check=check)
        age = int(msg.content)
        user_year = int(age / 10000)
        user_month = int((age % 10000) / 100)
        user_day = int(age % 100)
        await ctx.author.send(f"Birthday : {user_day}  / {user_month} / {user_year}  ")
        await ctx.author.send(f"\nCurent date : {current_day} / {current_month} / {current_year}")
        # if birth date is greater then current birth_month
        # then donot count this month and add 30 to the date so
        # as to subtract the date and get the remaining days

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (user_day > current_day):
            current_month = current_month - 1
            current_day = current_day + month[user_month - 1]

        # if birth month exceeds current month, then
        # donot count this year and add 12 to the
        # month so that we can subtract and find out
        # the difference
        if (user_month > current_month):
            current_year = current_year - 1
            current_month = current_month + 12

        # calculate date, month, year
        calculated_date = current_day - user_day
        calculated_month = current_month - user_month
        calculated_year = current_year - user_year

        # print present age
        await ctx.author.send(f"you are {calculated_year}  years ")
        await ctx.author.send(f"        {calculated_month} month(s) and ")
        await ctx.author.send(f"        {calculated_date}   days old ")
        
def setup(bot):
    bot.add_cog(FunCog(bot))
