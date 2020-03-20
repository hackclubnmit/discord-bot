## Hack Club NMIT Discord Bot

A discord bot with some club specific features.

## Requirements

- [A Discord Account](https://discordapp.com/)
- [Python 3.6 and up](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) 
- [Pip](https://pypi.org/project/pip/)
- [Firestore DB](https://firebase.google.com/docs/firestore/quickstart)

## Setup 

1. Setup the bot by following this guide : [RealPython](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)

2. Place the token in token.txt

3. Install the dependencies:
`pip install -r --user requirements.txt`

4. Set up Firestore and initialize the SDK: [Here](https://firebase.google.com/docs/firestore/quickstart) and [Here](https://firebase.google.com/docs/admin/setup#initialize-sdk)

5. Start the bot: `python bot.py`

## Theory

To help you get started on understanding and contributing to this project.

- Python Guides : 
    - [Arch Wiki](https://wiki.archlinux.org/index.php/Python#See_also)
    - [Derek Banas YT](https://www.youtube.com/watch?v=H1elmMBnykA)
    - [Sentdex YT](https://www.youtube.com/watch?v=eXBD2bB9-RA&list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln)
    - [Real Python](https://realpython.com/)

- Discord API Guides:
    - [Official Docs (Important)](https://discordpy.readthedocs.io/en/latest/index.html)
    - [Real Python Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/)
    - [Lucas's Updated YT Tutorial](https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ)

- [Firebase Guide](https://firebase.google.com/docs/firestore)

## What are cogs?

[Documentation Explanation](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html)

Cogs is a special feature which lets you  distribute functions/commands of the bot in different files.

In every module part of the cog, the commands, listeners, etc are wrapped in a class.

So why do this?
Cogs allow you to load and unload modules.
So say for example, your bot was just a single file called `bot.py`, if you made any changes to the file, to make it work on the bot, you would've had to kill the script and start it again. This can cause inconvenience to the users of the bot who are using different features of the bot.
So if you had cogs, you could just unload the module, make the changes, and load it back, leaving the rest of the bot unaffected.

Syntax for a cog:

In file `example.py`

```py
import discord
from discord.ext import commands
from discord.ext.commands import Bot

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")
    

def setup(bot):
    bot.add_cog(Example(bot)) 
```

So if you had this `example.py` file, you could load this module using the command `h!load example` as described in `bot.py` without having to kill the entire script.

## Contributing

- Fork the Repo
- Create a seperate branch (say `test`)
- Make changes
- Create a PR
