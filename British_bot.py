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

bot = commands.Bot(command_prefix='!')#this allows the bot to take in bot commands with !




#This is the random phrase part of the bot
#@client.event
#async def on_message(message): #
    #if message.author == client.user: #if author of the message equals the user, print the message.
        #return 

    #keywords = ['britian', 'british', 'united kingdom', 'brit']
    #british_quotes = ['Cheers love the calvalry is here!', 'Bruv, you really init', 'fish and chips, bloody bloody arse'] #array of quotes to say
    

    #if any(keyword in message.content.lower() for keyword in keywords): #If the message sent is "britian", the bot will response
        #await message.channel.send(random.choice(british_quotes)) #sends the response by picking a random phrase from the array 




#This is the bot commands section
@bot.command(name='bruv')
async def brit_phrase(ctx):
    british_quotes = ['Cheers love the calvalry is here!', 'Bruv, you really init', 'fish and chips, bloody bloody arse']
    await ctx.send(random.choice(british_quotes))

@bot.command(name='god')
async def queen_photo(ctx):
    await ctx.send('mate', file=discord.File('queen.jpg'))


###################################################################
#voice_client is the instance when the bot is in the call
@bot.command(name='godsavethequeen')
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.author.voice.channel #creates channel variable
        await channel.connect() #connects bot to channel
    else:
        await ctx.send("You ain't in the bloody channel mate. Why would I join?")


@bot.command(name = 'traitor')
async def leave(ctx):
    await ctx.voice_client.disconnect()

#@bot.command(name = "real_music")
#async def play(ctx, url):
    #server = ctx.message.server
    #voice_client = client.voice_client_in(server)
    #player = await voice_client.create_ytdl_player(url)
    #players[server.id] = player
    #if url != "https://www.youtube.com/watch?v=D3dR7u7TPNo&ab_channel=Mandetriens":
        #await ctx.send("No other music shall be played on these isles except god save the queen!")
    #else:
        #player.start()

###################################################################


bot.run(TOKEN)
client.run(TOKEN)
