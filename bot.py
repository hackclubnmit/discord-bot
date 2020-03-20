import os
import database
import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot

# start the discord client
client = discord.Client()

# quickstart the firestore database
db = database.initdb()

# bot prefix, for eg h!hello
bot = commands.Bot(command_prefix='h!')


@bot.event
async def on_ready():
    '''
    Prints next line to terminal after
    establishing connnection to Discord's API.
    '''
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="HackClubBot | h!help"))


@bot.command()
@commands.has_role('Core')
async def load(ctx, extension):
    ''' 
    Role Specific : Core only
    Loads a module in /cogs directory
    '''
    await ctx.send(f"Loaded cog: {extension}")
    bot.load_extension(f'cogs.{extension}')


@bot.command()
@commands.has_role('Core')
async def unload(ctx, extension):
    ''' 
    Role Specific : Core only
    Unloads a module in /cogs directory
    '''
    await ctx.send(f"Unloaded cog: {extension}")
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
@commands.has_role('Core')
async def reload(ctx, extension):
    '''
    Role Specific : Core only 
    Reloads a module in /cogs directory
    '''
    await ctx.send(f"Reloaded cog: {extension}")
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


for filename in os.listdir("cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


with open("token.txt", "r") as f:
    token = f.readline().split('\n')[0]

bot.run(token)