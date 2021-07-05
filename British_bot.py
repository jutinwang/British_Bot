# british_bot.py
import os
import random
import youtube_dl
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import requests
from spotify import oauth
from urllib.parse import urlencode

#client_credentials_manager = SpotifyClientCredentials(client_id= "205fc2ce85c7473cb414eeba372b2d08", client_secret="f719ccc187e94385ab2baae48534f699")
#sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


import discord
#This keeps your discord bot token safe
from dotenv import load_dotenv

#This lets you have bot commands for your bot
from discord.ext import commands 
from discord.ext.commands import bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')#Variable token is now equal to the discord bot token

moment = discord.Client()#Client object handles events and states while connected to the discord API

client = commands.Bot(command_prefix='!')#this allows the bot to take in bot commands with !
players = {}


#This is the bot commands section
###################################################################
@client.command(name='bruv')
async def brit_phrase(ctx):
    british_quotes = ['Cheers love the calvalry is here!', 'Bruv, you really init', 'fish and chips, bloody bloody arse', 'Flood the cowling, plenty of it']
    await ctx.send(random.choice(british_quotes))

@client.command(name='god')
async def queen_photo(ctx):
    god_images = ['queen.jpg', 'queen_sitting.jpg', 'fake_smile.jpg']
    await ctx.send('mate', file=discord.File(random.choice(god_images)))

###################################################################
#voice_client is the instance when the bot is in the call
@client.command(name='arise')
async def join(ctx):
    if ctx.message.author.voice: #.voice returns if they are in voice call or not
        channel = ctx.author.voice.channel #creates channel variable where .author is the person who summoned the bot, .voice checks if you're in a call and .channel to say where the invite to join came from
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
        await ctx.send("The only channel I'm in right now is the english channel")

@client.command(name='godsavethequeen')
async def play(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    source = await discord.FFmpegOpusAudio.from_probe("good_music.mp3", method='fallback')
    voice.play(source)
###################################################################
@client.command(name="country")
async def history(ctx, country):
    colonies = ["Afghanistan","Antigua and Barbuda","Australia","Bahamas","Bahrain","Barbados","Belize","Botswana","Brunei","Canada","Cyprus","Dominica","Egypt",
                "Fiji","Gambia","Ghana","Grenada","India","Iraq","Jamaica","Jordan","Kenya","Kiribati","Kuwait","Lesotho","Malawi","Malaysia","Maldives","Malta","Mauritius",
                "Myanmar", "Nauru","New_Zealand","Nigeria","Pakistan","Qatar","St_lucia","Saint_Kitts","St_Vincent","Seychelles",
                "Sierra_leone","Soliman_islands","South_Africa","Sri_Lanka","Sudan" ,"Swaziland","Tanzania","Tonga","Trinidad","Tuvalu","Uganda","UAE","United_States","Vanuatu","Yemen","Zambia","Zimbabwe"]
    twenty_two = ["Andorra", "Belarus", "Bolivia", "Burundi", "CAR", "Chad", "Republic_Congo", "Guatemala", "Ivory_Coast", "Kyrgyzstan", "Liechtenstein", "Luxembourg", "Mali", "Marshall_Islands", "Monaco", 
                 "Mongolia", "Paraguay", "Sao_Tome", "Sweden", "Tajikistan", "Uzbekistan", "Vatican"]
   
    if country in colonies:
        await ctx.send("Britian has colonized that country before")
    elif country in twenty_two:
        await ctx.send("This country has not been invaded by Britian ever")
    else:
        await ctx.send("We have invaded this country before (I think we won too)")

@client.command(name="pride")
async def flag(ctx):
    await ctx.send(":flag_gb:" + "Britiania Rules The Waves" + ":flag_gb:")

@client.command(name="ukmusic")
async def playlist(ctx):
    headers = {
        "Authorization": "Bearer {}".format(oauth)
        }
    endpoint = "https://api.spotify.com/v1/playlists/37i9dQZEVXbLnolsZ8PSNw"
    data = urlencode({"market": "GB"})
    lookup_url = f"{endpoint}?{data}"
    print (lookup_url)
    r = requests.get(lookup_url, headers = headers)
    print (r.status_code)

    await ctx.send("Here is what the good people of Britiania are listening to on Spotify")
    await ctx.send("Song - Artist - Album\n")

    for item in r.json()['tracks']['items']:
        await ctx.send(
            item['track']['name'] + ' - ' +
            item['track']['artists'][0]['name'] + ' - ' +
            item['track']['album']['name']
    )

client.run(TOKEN) 
