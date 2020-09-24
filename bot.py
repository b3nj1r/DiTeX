import discord
from discord.ext import commands
import os
c = commands.Bot(command_prefix='.')

k = os.environ.get('TEXTOKEN')

@c.event
async def on_ready():
    print('ready')

c.run(k)