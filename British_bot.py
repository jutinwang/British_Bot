# british_bot.py
import os
import random
import youtube_dl

import discord
#This keeps your discord bot token safe
from dotenv import load_dotenv

#This lets you have bot commands for your bot
from discord.ext import commands 
from discord.ext.commands import bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')#Variable token is now equal to the discord bot token

#client = discord.Client()#Client object handles events and states while connected to the discord API

client = commands.Bot(command_prefix='!')#this allows the bot to take in bot commands with !


#This is the bot commands section
###################################################################
@client.command(name='bruv')
async def brit_phrase(ctx):
    british_quotes = ['Cheers love the calvalry is here!', 'Bruv, you really init', 'fish and chips, bloody bloody arse']
    await ctx.send(random.choice(british_quotes))

@client.command(name='god')
async def queen_photo(ctx):
    god_images = ['queen.jpg', 'queen_sitting.jpg', 'fake_smile.jpg']
    await ctx.send('mate', file=discord.File(random.choice(god_images)))


###################################################################
#voice_client is the instance when the bot is in the call
@client.command(name='godsavethequeen')
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.author.voice.channel #creates channel variable
        await channel.connect() #connects bot to channel
    else:
        await ctx.send("You ain't in the bloody channel mate. Why would I join?")


@client.command(name = 'traitor')
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("cheers, later bruv")
    else:
        await ctx.send("bruv")

###################################################################


client.run(TOKEN)
