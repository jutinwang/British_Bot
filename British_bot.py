# british_bot.py
################################################################
# british_bot.py essential imports
import os
import random
import youtube_dl
import discord
#This keeps your discord bot token safe
from dotenv import load_dotenv

#This lets you have bot commands for your bot
from discord.ext import commands 
from discord.ext.commands import bot
################################################################
#Stuff for spotify api
import spotipy #u
from spotipy.oauth2 import SpotifyClientCredentials #nu
import json #u 
import requests #u
from spotify import oauth #u
from urllib.parse import urlencode #u
################################################################
#client_credentials_manager = SpotifyClientCredentials(client_id= "205fc2ce85c7473cb414eeba372b2d08", client_secret="f719ccc187e94385ab2baae48534f699")
#sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')#Variable token is now equal to the discord bot token

moment = discord.Client()#Client object handles events and states while connected to the discord API

client = commands.Bot(command_prefix='!')#this allows the bot to take in bot commands with !
players = {}


#This is the bot commands section
###################################################################
#says a random british phrase
@client.command(name='bruv')
async def brit_phrase(ctx):
    british_quotes = ['Cheers love the calvalry is here!', 'Bruv, you really init', 'fish and chips, bloody bloody arse', 'Flood the cowling, plenty of it',
    "They lost the plot.", "I haven't seen that in donkey's years.", "Quit your whinging!", "He's such a chav.", "You have thrown a spanner in the works.", "Lets have a chinwag.",
    "I am chuffed to bits.", "That's manky."]
    await ctx.send(random.choice(british_quotes))

#sends image of the queen with a small image 
@client.command(name='god')
async def queen_photo(ctx):
    god_images = ['queen.jpg', 'queen_sitting.jpg', 'fake_smile.jpg', 'swag.jpg', 'bruh.jpg', 'whatdat.jpg']
    await ctx.send('mate', file=discord.File(random.choice(god_images)))

###################################################################
#voice_client is the instance when the bot is in the call
#joins the call
@client.command(name='arise')
async def join(ctx):
    if ctx.message.author.voice: #.voice returns if they are in voice call or not
        channel = ctx.author.voice.channel #creates channel variable where .author is the person who summoned the bot, .voice checks if you're in a call and .channel to say where the invite to join came from
        await channel.connect() #connects bot to channel
    else:
        await ctx.send("You ain't in the bloody channel mate. Why would I join?")

#leaves the call
@client.command(name = 'traitor')
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 

    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("cheers, later bruv")
    else:
        await ctx.send("The only channel I'm in right now is the english channel")

#plays the UK national anthem
@client.command(name='godsavethequeen')
async def play(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    source = await discord.FFmpegOpusAudio.from_probe("good_music.mp3", method='fallback')
    voice.play(source)
###################################################################
#This commands uses an arguement to output a certain response
#This program tells you the relation between the country and the UK
@client.command(name="country")
async def history(ctx, country):
    #Arrays with all the countries
    colonies = ["Afghanistan","Antigua and Barbuda","Australia","Bahamas","Bahrain","Barbados","Belize","Botswana","Brunei","Canada","Cyprus","Dominica","Egypt",
                "Fiji","Gambia","Ghana","Grenada","India","Iraq","Jamaica","Jordan","Kenya","Kiribati","Kuwait","Lesotho","Malawi","Malaysia","Maldives","Malta","Mauritius",
                "Myanmar", "Nauru","New_Zealand","Nigeria","Pakistan","Qatar","St_lucia","Saint_Kitts","St_Vincent","Seychelles",
                "Sierra_leone","Soliman_islands","South_Africa","Sri_Lanka","Sudan" ,"Swaziland","Tanzania","Tonga","Trinidad","Tuvalu","Uganda","UAE","United_States","Vanuatu","Yemen","Zambia","Zimbabwe"]
    twenty_two = ["Andorra", "Belarus", "Bolivia", "Burundi", "CAR", "Chad", "Republic_Congo", "Guatemala", "Ivory_Coast", "Kyrgyzstan", "Liechtenstein", "Luxembourg", "Mali", "Marshall_Islands", "Monaco", 
                 "Mongolia", "Paraguay", "Sao_Tome", "Sweden", "Tajikistan", "Uzbekistan", "Vatican"]
   #if statement for all the different options 
    if country in colonies:
        await ctx.send("Britian has colonized that country before")
    elif country in twenty_two:
        await ctx.send("This country has not been invaded by Britian ever")
    else:
        await ctx.send("We have invaded this country before (I think we won too)")

#This sends a flag emoji of Great Britian
@client.command(name="pride")
async def flag(ctx):
    await ctx.send(":flag_gb:" + "Britiania Rules The Waves" + ":flag_gb:")

#This is the spotify api integration
#This displays the top 50 UK songs on the charts
@client.command(name="ukmusic")
async def playlist(ctx):
    #Authortization for API usage
    headers = {
        "Authorization": "Bearer {}".format(oauth)
        }
    #These create the link that the program fetches (The playlist)
    endpoint = "https://api.spotify.com/v1/playlists/37i9dQZEVXbLnolsZ8PSNw"
    data = urlencode({"market": "GB"})
    lookup_url = f"{endpoint}?{data}"
    #This prints what the link looks like and the status code (200 if it works correctly)
    print (lookup_url)
    r = requests.get(lookup_url, headers = headers)
    print (r.status_code)

    #This prints out the playlist 
    await ctx.send("Here is what the good people of Britiania are listening to on Spotify")
    em = discord.Embed(title = "Song - Artist - Album\n")

    allTracks = ""
    
    for item in range(int(tracks)):
        allTracks += item['track']['name'] + ' - ' + item['track']['artists'][0]['name'] + ' - ' + item['track']['album']['name'] + '\n'

    await ctx.send(allTracks)


client.run(TOKEN) 
