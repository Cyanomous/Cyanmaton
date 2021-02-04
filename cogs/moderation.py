import discord
from discord.ext import commands
import os
import requests
import json
import time
from math import *
import time
import asyncio
from datetime import datetime
import dateparser

client = discord.Client()


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='highrole', aliases=['top_role', 'toprole', 'high_role'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(title='Highest role for:',
                              description=member.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))
        embed.add_field(
            name='\uFEFF', value=f'The highest role for {member.display_name} is {member.top_role.name}')
        await ctx.send(content=None, embed=embed)

    @commands.command(name='perms', aliases=['permissions'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.author

        perms = '\n'.join(
            perm for perm, value in member.guild_permissions if value)

        embed = discord.Embed(title='Permissions for:',
                              description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))
        embed.add_field(name='\uFEFF', value=perms)
        await ctx.send(content=None, embed=embed)

    @commands.command(name='addrole', aliases=['roleadd'], pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, user: discord.Member, *, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(f"Hey {ctx.author.name}, I have sucesfully given {user.name} the role {role.name}!")

    @commands.command(name='removerole', aliases=['remrole', 'rem', 'remove'], pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, user: discord.Member, *, role: discord.Role):
        await user.remove_roles(role, reason=None, atomic=True)
        await ctx.send(f"Hey {ctx.author.name}, I have sucesfully removed the role {role.name} from {user.name}!")


def setup(bot):
    bot.add_cog(ModerationCog(bot))
