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
import aiohttp
import datetime
from cogs.lists import beg_people

os.chdir("The file path to where you store index.py don't include index.py")


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 1000
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)
    return True


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)
    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return user


async def get_bank_data():
    with open("bank.json", "r") as f:
        return json.load(f)


class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="balance", aliases=['bal'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def balance(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        total_bal = bank_amt + wallet_amt
        embed = discord.Embed(
            title=f"{ctx.author.name}'s balance", colour=random.randint(0, 16777216))
        embed.add_field(name="**Wallet**:", value=wallet_amt, inline=False)
        embed.add_field(name="**Bank**:", value=bank_amt, inline=False)
        embed.add_field(name="**Total Bal**:", value=total_bal, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="beg", aliases=['begging'])
    @commands.cooldown(1, 40, commands.BucketType.user)
    async def beg(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        beg_earnings = random.randrange(1, 501)
        await ctx.send(f"**{random.choice(beg_people)}** has given {beg_earnings} to {ctx.author.mention}!!")

        users[str(user.id)]["wallet"] += beg_earnings
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    @commands.command(name="withdraw", aliases=['with'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def withdraw(self, ctx, amount=None):
        if amount == None:
            await ctx.send("Please enter the amount you want to withdraw")
            return

        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        beg_earnings = random.randrange(1, 501)
        await ctx.send(f"**{random.choice(beg_people)}** has given {beg_earnings} to {ctx.author.mention}!!")

        users[str(user.id)]["wallet"] += beg_earnings
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)


def setup(bot):
    bot.add_cog(EconomyCog(bot))
