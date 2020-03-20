import time
import database
import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Reputation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Core')
    async def giverep(self, ctx, arg):
        '''
        Role Specific : Core only
        Calls giveCredits function to update 
        the rep value in firestore DB
        '''
        check = database.giveCredits(arg)
        if (check == True):
            ts = time.gmtime()
            print(time.strftime("[%Y-%m-%d %H:%M:%S]", ts) + f" Gave {arg} credits")
            await ctx.send(f"Gave reputation to {arg}")
        else:
            await ctx.send(f"Error!")

    @commands.command()
    @commands.has_role('Core')
    async def getrep(self, ctx, arg):
        '''
        Role Specific : Core only
        Calls getCredits function to retrieve 
        the rep value in firestore DB
        '''
        rep = database.getCredits(arg)
        if(rep >= 0):
            ts = time.gmtime()
            print(time.strftime("[%Y-%m-%d %H:%M:%S]", ts) + f' Reputation of {arg}: {rep}')
            await ctx.send(f"Reputation of {arg} : {rep}") 
        else:
            ts = time.gmtime()
            print(time.strftime("[%Y-%m-%d %H:%M:%S]", ts) + f' User "{arg}" : No such document!')
            await ctx.send(f"No records found. Contact DB Dudes")


def setup(bot):
    bot.add_cog(Reputation(bot))