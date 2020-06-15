# import database
import discord
from discord.ext import commands
from discord.ext.commands import Bot

class UserInfo(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def get_user_info(self, ctx):
        msg = await ctx.author.send("Info gathering...")
        def check(message):
            return message.author == ctx.author and message.channel == msg.channel
        reply = await self.bot.wait_for('message', check=check)
        print(reply.content)
        await ctx.author.send("Cool Cool Cool.")

def setup(bot):
    bot.add_cog(UserInfo(bot))