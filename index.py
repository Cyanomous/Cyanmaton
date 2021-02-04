import discord
from discord.ext import commands
import os
import requests
import json
import sys
import traceback
import secret
import sys
from secret import TOKEN
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

os.chdir("C:\\Users\\justi_jtw\\Bot\\Cyanmaton")


def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


initial_extensions = ['cogs.fun',
                      'cogs.help',
                      'cogs.moderation',
                      'cogs.utility',
                      'cogs.economy',
                      'cogs.images',
                      'cogs.giveaway',
                      'jishaku']

bot = commands.Bot(command_prefix=get_prefix,
                   description='Just a Cyan Automaton', intents=intents)


@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = 'c', 'C'
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await guild.text_channels[0].send(f'Hello thank you for adding me to your server, you are the {len(bot.guilds)}th server that I am in! To ger started send `c!help`')


@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help")
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [
                self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(
                    command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)


bot.help_command = MyHelp()

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

    @commands.Cog.listener()
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing permission(s). You need "{error.missing_perms}" to use this command.')
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f'Your arguments are not correct. Use "chelp {ctx.invoked_with}" to see how to use it, or join our support server so we can help you there, https://discord.gg/petEegPatJ.')
            print(error)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'You are missed an required argument. Make sure to add `{error.param}` if you are going to use this command!')
        elif isinstance(error, commands.NotOwner):
            await ctx.send("You are not the owner sorry!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'I am missing "{error.missing_perms}" permission(s), please give me what I am missing so I can run commands properly!')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'You are on a cooldown, try again later')
        else:
            await ctx.send(f'Join our support server if this error keeps on happening and report it there "<https://discord.gg/petEegPatJ>"')
            await ctx.send(f"""The error, ```py
    {error}```""")

    @bot.event
    async def on_ready():
        print(f'We have logged in as {client.user}'.format(client))
        print(sys.version)
        print(discord.__version__)

    bot.run(TOKEN)
