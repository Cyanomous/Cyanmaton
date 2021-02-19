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
        await ctx.send(f'Congratulations! {winner.mention} won {prize}'
                       
    @commands.command(name="hungergames")
    async def hunger_games(self,ctx,emoji , seconds:int=False ,  number_of_winners: int=False):
        if (number_of_winners!=False and seconds!=False) :
            await ctx.send(" @here ")
            #end = datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds)
            embed= discord.Embed(title="HUNGER GAMES", description=f"There can only be **{number_of_winners}**  winners !")
            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar_url)
            #embed.add_field(name="Ends At : ",value= f"{end} UTC")
            embed.set_footer(text=f"Ends {seconds} seconds from now !")
            message = await ctx.send(embed=embed)
            reasons_of_dying = [" stepped into a field of poisonous mushrooms and had a horrible death ",
                                "got stomped by a rhyno , now serves as a carpet",
                                "got deleted from the database , now is a stranger",
                                "lost in the casino and owes a lot of money, now is a wanted person",
                                "forgot it is saturday and went to work , WASTED ! ",
                                "bought the wrong medicine from the drugstore, cheers! ",
                                "lost in pvp in csgo , what a noob! ",
                                "forgot to buy food in his/her way home , will be hungry soon, sad ! ",
                                "was a sitting tomato on a railway ,the sound he/she made was 'flie' ! ",
                                "stole money from the church and got busted by the police , naughty naughty!",
                                "slipped at the stairs because of cat shit , ewwww , gross! ",
                                "ate a lot of potato chips , now he/she is a potato chip , chip chip potato chip"]

            reasons_of_winning = ["stumbled upon gold , foot hurts , but worth it",
                                  "won all super mario levels , what a pro ! ",
                                  "inspired a lot of people and then ate a cake",
                                  "got selected among 10.000.000 people to be the new sex symbol",
                                  "won because he/she is a winner since birth",
                                  "says oblivion is better than skyrim and is absolutely right",
                                  "can beat every obstacle in life and he/she knows it "]

            try:

                await message.add_reaction(f"{emoji}")
            except:
                    await ctx.send(f"failed to add reaction")
            await asyncio.sleep(seconds)
            channel=ctx.channel
            new_msg = await self.bot.get_channel(channel.id).fetch_message(message.id)
            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(self.bot.user))
            winner_list = []
            while len(winner_list)<(number_of_winners) and len(winner_list)<(len(users)) :
                winner=random.choice(users)
                if winner not in winner_list:   #we don't want to get the same winner multiple times
                    winner_list.append(winner)
            counter = 0
            for i in users:
                if i not in winner_list:
                    counter=counter+1
                    embed = discord.Embed(title=(f"Round {counter}"),
                                          description=f"{i.mention}  {random.choice(reasons_of_dying)}")
                    embed.set_author(name=i.name,
                                     icon_url=i.avatar_url)
                    # embed.add_field(name="Ends At : ",value= f"{end} UTC")
                    embed.set_footer(text=f"{len(users)-counter} players remaining ")
                    await ctx.send(embed=embed)
                    await asyncio.sleep(2)
            for i in range(len(winner_list)):
                choicew=random.choice(reasons_of_winning)
                await ctx.send(f" {winner_list[i].mention} {choicew}  ")

        else:
            await ctx.send(""" ``Arguments not provided correctly.``
    **Correct argument form** : {custom_prefix}hungergames <emoji> <seconds> <number_of_winners>""")
     


def setup(bot):
    bot.add_cog(GiveawayCog(bot))
