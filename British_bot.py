# british_bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands #This lets you have bot commands for your bot
from discord.ext.commands import bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')#Variable token is now equal to the discord bot token

client = discord.Client()#Client object handles events and states while connected to the discord API

bot = commands.Bot(command_prefix='!')#this allows the bot to take in bot commands with !




#This is the random phrase part of the bot
@client.event
async def on_message(message):
    if message.author == client.user:#if author of the message equals the user, print the message.
        return 

    british_quotes = ['Cheers love the calvalry is here!', 'Bruv, you really init', 'fish and chips, bloody bloody arse'] #array of quotes to say
    
    if message.content == 'britian': #If the message sent is "britian", the bot will response
        await message.channel.send(random.choice(british_quotes)) #sends the response by picking a random phrase from the array




#This is the bot commands section
@bot.command(name='bruv')
async def brit_phrase(ctx):
    british_quotes = ['Cheers love the calvalry is here!', 'Bruv, you really init', 'fish and chips, bloody bloody arse']
    await ctx.send(random.choice(british_quotes))

@bot.command(name='god')
async def queen_photo(ctx):
    await ctx.send('mate', file=discord.File('queen.jpg'))


bot.run(TOKEN)
client.run(TOKEN)
