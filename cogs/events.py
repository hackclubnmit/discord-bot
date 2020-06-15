import discord
from discord.ext import commands
from discord.ext.commands import Bot

class Events(commands.Cog):
    '''
    All Discord API events are defined here
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        '''
        Prints next line to terminal after
        establishing connnection to Discord's API.
        '''
        print('We have logged in as {0.user}'.format(self.bot))
        await self.bot.change_presence(activity=discord.Game(name="HackClubBot | h!help"))

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member):
        channel = await member.create_dm()
        # Start User info collection for registration
        message = "Hi"
        await channel.send(message)


def setup(bot):
    bot.add_cog(Events(bot))

    