import discord
from discord.ext import commands
import os
import requests
import json
import random
from math import *
import cogs.lists
import numpy
from cogs.lists import colour
import datetime
import googletrans
import time

client = discord.Client()


class UtilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.trans = googletrans.Translator()


@commands.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix changed to {prefix}!')

    @commands.command(name="setstatus", hidden=True)
    @commands.is_owner()
    async def setstatus(self, ctx: commands.Context, *, text: str):
        await self.bot.change_presence(activity=discord.Game(text))

    @commands.command(name="vote", aliases=["upvote"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def vote(self, ctx):
        top_gg_vote_link = "[VOTE HERE!](https://top.gg/bot/746164033056538624/vote)"
        discordbotlist_vote_link = "[VOTE HERE!](https://discordbotlist.com/bots/cyanmaton/upvote)"
        embed = discord.Embed(
            title='Upvote Cyanmaton!', colour=random.randint(0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981))
        embed.add_field(name="top.gg",
                        value=f"{top_gg_vote_link}", inline=False)
        embed.add_field(name="discordbotlist.com",
                        value=f"{discordbotlist_vote_link}", inline=False)
        embed.set_footer(
            text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/802185231993405451/806674718647648286/y1rr1gmyvuc51.png")
        await ctx.send(embed=embed)

    @commands.command(name='userinfo', aliases=['useinfo', 'ui', 'user-info'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        roles = [role.mention for role in member.roles if role !=
                 ctx.guild.default_role]
        roletext = " ".join(roles)
        embed = discord.Embed(colour=random.randint(
            0, 16777216), timestamp=datetime.datetime.utcfromtimestamp(1611762981), type="rich")
        embed.add_field(name='**User-info**', value=f'''Username: {member.name}#{member.discriminator}
Tag: #{member.discriminator}
Nickname: {member.nick}
ID: `{member.id}` ''', inline=False)
        embed.add_field(name='**Roles**', value=f'{roletext}', inline=True)
        embed.add_field(name='**Other**', value=f'''Account Creation: {member.created_at.strftime('%B %e, %Y')}
Joined Server: {member.joined_at.strftime('%B %e, %Y')} ''', inline=True)
        embed.set_author(name=f'{member.name}#{member.discriminator}',
                         icon_url=member.avatar_url_as(format='png'))
        embed.set_thumbnail(url=member.avatar_url_as(format='png'))
        embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='serverinfo', aliases=["servinfo", "guildinfo"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            color=random.randint(0, 16777216),
            type="rich",
            timestamp=ctx.message.created_at
        )
        embed.add_field(name='**Outline**', value=f'''Owner: `{ctx.guild.owner}`
Region: `{ctx.guild.region}`
Date Created: `{ctx.guild.created_at.strftime('%B %e, %Y')}`
Boost Tier: `{ctx.guild.premium_tier}`
Verification: `{ctx.guild.verification_level}`

ID: {ctx.guild.id}''', inline=True)
        embed.add_field(name='**Server**', value=f'''Member Count: `{ctx.guild.member_count}`
Roles: `({len(ctx.guild.roles)})`
Channels: `({len(ctx.guild.channels)})`
Text: `({len(ctx.guild.text_channels)})`
Voice: `({len(ctx.guild.voice_channels)})`
''', inline=True)
        embed.set_author(name=f'{ctx.guild.name}',
                         icon_url=ctx.guild.icon_url_as(format='png'))
        embed.set_thumbnail(url=ctx.guild.icon_url_as(format='png'))
        await ctx.send(embed=embed)

    @commands.command(name='info', aliases=['information'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def info(self, ctx):
            title = 'Cyanmation Info:', description = 'Hi, I am Cyanmation, a small bot just trying to make its way to the big world of discord!', colour = 0x00FFFF, timestamp = datetime.datetime.utcfromtimestamp(1611762981))
        embed.set_footer(
            text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
        embed.add_field(name = '\uFEFF', value = "I can do basic moderation, have fun commands and more! Thank you for adding me to your server! If you have any questions run the command `csupport` for help and `chelp` for help!", inline = False)
        embed.add_field(name = "Server count",
                        value = f"{len(self.bot.guilds)}")
        embed.set_thumbnail(
            url = "https://images-ext-2.discordapp.net/external/A3Nv-QKts2NN-ckygcgd26TYtl2apR1g-qWDS_SbfCM/%3Fsize%3D1024/https/cdn.discordapp.com/icons/801972671310200852/4a3ee18d11ead8ec225fe5d0c5e6ceba.png")
        embed.add_field(
            name = "Invite", value = "[Here!](https://discord.com/api/oauth2/authorize?client_id=746164033056538624&permissions=2147483647&scope=bot)")
        embed.add_field(
            name = "Info", value = """Current version: `v2.0.0`
Owner: `Cyanomous`""")
        await ctx.send(embed = embed)

    @ commands.command(name = 'botcount', pass_context = True, aliases = ['botservers'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def botcount(self, ctx):
        await ctx.send(f"I'm in {len(self.bot.guilds)} servers!")

    @ commands.command(name = 'partners', pass_context = True, aliases = ['premiumservers'])
    async def partners(self, ctx):
        await ctx.send(f"Just join: https://discord.gg/8TpSsxb or else you are not an epic gamer like Spectrum, and if you wana be really big brain send messages in his server!")

    @ commands.command(name = 'serverlist', pass_context = True, aliases = ['servernames'], hidden = True)
    async def serverlist(self, ctx):
        guilds=[]
        for guild in client.guilds:
            guilds.append(
                f"**{guild.name}** - `{guild.id}` - {len(guild.members)}")
        guilds="\n".join([g.name for g in bot.guilds])
        embed=discord.Embed(title = "Server list", description = guildlist)
        await ctx.send(embed = embed)

    @ commands.command(name = 'avatar', aliases = ['profilepicture', 'av', 'profilepic', 'pfp', 'icon'])
    @ commands.cooldown(1, 5, commands.BucketType.user)
    @ commands.guild_only()
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member is None:
            member=ctx.author
        embed=discord.Embed(
            title = f'{member.name}#{member.discriminator}', colour = member.colour, type = "image")
        embed.set_image(url = member.avatar_url_as(format='png'))
        await ctx.send(content = None, embed = embed)

    @ commands.command(name = 'choose', aliases = ['pick', 'cho'])
    @ commands.guild_only()
    async def choose(self, ctx, *choices: commands.clean_content):
        if len(choices) < 2:
            return await ctx.send('Not enough choices to pick from.')

        await ctx.send(random.choice(choices))

    @ commands.command(name = 'google', aliases = ['googlewebsite', 'googleweb'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def google(self, ctx):
        embed=discord.Embed(title = "Google", url = "https://www.google.com/", colour = random.randint(0, 16777216),
                              description = "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.")
        await ctx.send(embed = embed)

    @ commands.command(name = 'docs', aliases = ['googledocs', 'googledoc'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def docs(self, ctx):
        embed=discord.Embed(title = "Google Docs", url = "https://docs.google.com/", colour = random.randint(0, 16777216),
                              description = "Create a new document and edit with others at the same time -- from your computer, phone or tablet. Get stuff done with or without an internet connection. Use Docs to edit Word files. Free from Google.")
        await ctx.send(embed = embed)

    @ commands.command(name = 'slides', aliases = ['googleslides', 'googleslide'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def slides(self, ctx):
        embed=discord.Embed(title = "Google Slides", url = "https://docs.google.com/presentation/", colour = random.randint(0, 16777216),
                              description = "Create a new presentation and edit with others at the same time. Get stuff done with or without an internet connection. Use Slides to edit PowerPoint files. Free from Google.")
        await ctx.send(embed = embed)

    @ commands.command(name = 'sheets', aliases = ['googlespreadsheets', 'googlesheets'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def sheets(self, ctx):
        embed=discord.Embed(title = "Google Sheets", url = "https://docs.google.com/spreadsheets/", colour = random.randint(0, 16777216),
                              description = "Create a new spreadsheet and edit with others at the same time -- from your computer, phone or tablet. Get stuff done with or without an internet connection. Use Sheets to edit Excel files. Free from Google.")
        await ctx.send(embed = embed)

    @ commands.command(name = 'googleforms', aliases = ['googleform'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def googleforms(self, ctx):
        embed=discord.Embed(title = "Google Forms", url = "https://docs.google.com/forms/", colour = random.randint(0, 16777216),
                              description = "Create a new survey on your own or with others at the same time. Choose from a variety of survey types and analyze results in Google Forms. Free from Google.")
        await ctx.send(embed = embed)

    @ commands.command(name = 'aboutgoogle', aliases = ['googleabout'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def aboutgoogle(self, ctx):
        embed=discord.Embed(title = "Google Sheets", url = "https://about.google/", colour = random.randint(0, 16777216),
                              description = "Stay up to date with Google company news and products. Discover stories about our culture, philosophy, and how Google technology is impacting others.")
        await ctx.send(embed = embed)

    @ commands.command(name = 'books', aliases = ['googlebooks', 'book'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def books(self, ctx):
        embed=discord.Embed(title = "Google Books", url = "https://books.google.ca/", colour = random.randint(0, 16777216),
                              description = "Google's comprehensive index of full-text books, and apparently also the world's most comprehensive index of full-text books! Pure amazment(spelling not included because my spelling is one of a kind)")
        embed.set_footer(text = "So good Cyanomous had to write it himself!")
        await ctx.send(embed = embed)

    @ commands.command(name = 'drive', aliases = ['googledrive'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def drive(self, ctx):
        embed=discord.Embed(title = "Google Drive", url = "https://drive.google.com/drive/", colour = random.randint(0, 16777216),
                              description = "Meet editor X I mean Google Drive, Google Drive is a way you can keep all your files backed up and safe! You get 15GB of storage for free!")
        embed.set_footer(
            text = "I mean, it's pretty good and also free!(wow, exclamation marks are fun! Cyanomous also wrote this!)")
        await ctx.send(embed = embed)

    @ commands.command(name = 'youtube', aliases = ['YouTube', 'Youtube'])
    @ commands.cooldown(1, 3, commands.BucketType.user)
    async def drive(self, ctx):
        embed=discord.Embed(title = "YouTube", url = "https://www.youtube.com/", colour = random.randint(0, 16777216),
                              description = "YouTube is one of a kind, it's amazing! If you don't use it you have never lived life to its fullest and should definitly try it out!")
        embed.set_thumbnail(
            url = "https://cdn.discordapp.com/attachments/787449167978823720/801966719501074433/YouTube_Ft_Cyanomous.png")
        embed.set_footer(
            text = "I don't get paid for saying this but I wish I did.")
        await ctx.send(embed = embed)

    @ commands.command(name = "ping")
    @ commands.cooldown(1, 2, commands.BucketType.user)
    async def ping(self, ctx: commands.Context):
        start_time=time.time()
        message=await ctx.send("Pinging...")
        end_time=time.time()
        await message.edit(content = f"Pong! `{round(self.bot.latency * 1000)}ms`\nAPI: `{round((end_time - start_time) * 1000)}ms`")

    @ commands.command(name = 'prefix', aliases = ['pref'])
    async def prefix(self, ctx):
        member=ctx.author
        embed=discord.Embed(title = 'Prefixes',
                              colour = member.random.randint(0, 16777216))
        embed.add_field(
            name = '\uFEFF', value = 'The prefixes for this bot are `c`, and `C`')
        await ctx.send(content = None, embed = embed)

    @ commands.command(name = 'servericon', aliases = ['servicon', 'sicon', 'serverpfp', 'ServerIcon'])
    @ commands.cooldown(1, 5, commands.BucketType.user)
    @ commands.guild_only()
    async def servericon(self, ctx):
        member=ctx.author
        # guild = ctx.server
        embed=discord.Embed(
            title = f'{ctx.guild.name}', colour = member.colour, type = "image")
        embed.set_image(url = ctx.guild.icon_url_as(format='png'))
        await ctx.send(content = None, embed = embed)

    @ commands.command(name = 'links', aliases = ['invitebot', 'botinvite', 'inv', 'invites', 'invite'])
    @ commands.cooldown(1, 2, commands.BucketType.user)
    async def links(self, ctx):
        embed=discord.Embed(
            title = 'Links', colour = random.randint(0, 16777216))
        embed.add_field(
            name = "Bot Invite", value = "[Add me here!](https://discord.com/api/oauth2/authorize?client_id=746164033056538624&permissions=2147483647&scope=bot)", inline = True)
        embed.add_field(
            name = "Beta Bot Invite", value = "[Add him here!](https://discord.com/api/oauth2/authorize?client_id=802247403960795210&permissions=2147483647&scope=bot)", inline = True)
        embed.add_field(
            name = "Support Server", value = "[Join here!](https://discord.gg/petEegPatJ)", inline = True)
        embed.add_field(
            name = "Website", value = "[My website!](https://cyanomous.github.io/)", inline = True)
        embed.add_field(
            name = "Email", value = "bot.cyanmaton@gmail.com", inline = True)
        await ctx.send(content = None, embed = embed)

    @ commands.command(name = 'support', aliases = ['peoplehelp', 'supportserver', 'INEEDHELP', 'helpserver', 'server'])
    @ commands.cooldown(1, 2, commands.BucketType.user)
    async def support(self, ctx):
        embed=discord.Embed(
            title = 'Support', description = "[Support Server](https://discord.gg/petEegPatJ)", colour = random.randint(0, 16777216))
        embed.add_field(
            name = "Link not working?", value = 'Copy and paste "https://discord.gg/petEegPatJ" into your browser!', inline = True)
        await ctx.send(content = None, embed = embed)
        await ctx.send("https://discord.gg/petEegPatJ")

    @ commands.command(name = 'translate')
    @ commands.cooldown(1, 1, commands.BucketType.user)
    async def translate(self, ctx, *, message: commands.clean_content):
        loop=self.bot.loop
        try:
            ret=await loop.run_in_executor(None, self.trans.translate, message)
        except Exception as e:
            return await ctx.send(f'An error occurred: {e.__class__.__name__}: {e}')

        embed=discord.Embed(title = 'Translated', colour = 0x4284F3)
        src=googletrans.LANGUAGES.get(ret.src, '(auto-detected)').title()
        dest=googletrans.LANGUAGES.get(ret.dest, 'Unknown').title()
        embed.add_field(name = f'From {src}',
                        value = ret.origin, inline = False)
        embed.add_field(name = f'To {dest}', value = ret.text, inline = False)
        await ctx.send(embed = embed)

    @ commands.command(name = 'add', aliases = ['addthings'])
    @ commands.cooldown(1, 2, commands.BucketType.user)
    @ commands.guild_only()
    async def add(self, ctx, whattoadd, *, whattoadd2):
        whattoadd=int(whattoadd)
        whattoadd2=int(whattoadd2)
        addedstuff=whattoadd + whattoadd2
        await ctx.send(f'The result is {addedstuff}!')

    @ commands.command(name = 'minus', aliases = ['minusthings', 'subtract'])
    @ commands.cooldown(1, 2, commands.BucketType.user)
    @ commands.guild_only()
    async def minus(self, ctx, whattominus, *, whattominus2):
        whattominus=int(whattominus)
        whattominus2=int(whattominus2)
        minusedstuff=whattominus - whattominus2
        await ctx.send(f'The result is {minusedstuff}!')

    @ commands.command(name = 'multiply')
    @ commands.cooldown(1, 2, commands.BucketType.user)
    @ commands.guild_only()
    async def multiply(self, ctx, whattomultiply, *, whattomultiply2):
        whattomultiply=int(whattomultiply)
        whattomultiply2=int(whattomultiply2)
        multiplystuff=whattomultiply * whattomultiply2
        await ctx.send(f'The result is {multiplystuff}!')

    @ commands.command(name = 'divide')
    @ commands.cooldown(1, 2, commands.BucketType.user)
    @ commands.guild_only()
    async def divide(self, ctx, whattodivide, *, whattodivide2):
        whattodivide=int(whattodivide)
        whattodivide2=int(whattodivide2)
        dividestuff=whattodivide / whattodivide2
        await ctx.send(f'The result is {dividestuff}!')

    @ commands.command(name = 'embed', aliases = ['makeembed', 'generateembed', 'emb'])
    @ commands.cooldown(1, 5, commands.BucketType.user)
    async def embed(self, ctx, title, description, footer, url):
        embed=discord.Embed()
        await ctx.send("Type the title for your embed! If you don't want a title send None")
        if title not in ('None', 'N/A', 'NA'):
            embed.title=title
        await ctx.send("Type the description for your embed! If you don't want a description send None")
        if description not in ('None', 'N/A', 'NA'):
            embed.description=description
        await ctx.send("Type the footer for your embed! If you don't want a title send None")
        if footer not in ('None', 'N/A', 'NA'):
            embed.set_footer(text = footer)
        if url not in ('None', 'N/A', 'NA'):
            embed.url=url
        await ctx.send(content = None, embed = embed)


def setup(bot):
    bot.add_cog(UtilityCog(bot))
