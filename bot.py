import os
import numpy as np
import sympy as sp
import cv2
import discord
from discord.ext import commands

c = commands.Bot(command_prefix='~')

k = os.environ.get('TEXTOKEN')
def convert(i):
    sp.preview(i, viewer='file', filename='o.png', euler=False)
    src = cv2.imread('o.png')
    _, alpha = cv2.threshold(cv2.cvtColor(~src, cv2.COLOR_BGR2GRAY), 64, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(~src)
    rgba = [b, g, r, alpha]
    dst = cv2.merge(rgba, 4)
    cv2.imwrite("o.png", dst)

@c.event
async def on_ready():
    print(1)

@c.event
async def on_message(message):
    if message.content.startswith('~'):
        print(f'received \"{message.content}\"\n')
        convert(message.content[1:len(message.content):1])
        channel = message.channel
        await channel.send(file=discord.File('o.png'))

c.run(k)
