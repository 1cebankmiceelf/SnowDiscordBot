import os
import discord

import pinger
from discord.ext import commands
from time import sleep
clienter = discord.Client()
my_secret = os.environ['tokey']
magicw = ("Informer","informer")



@clienter.event
async def on_ready():
    print('it seems that I sided with the rasta {0.user}'.format(clienter) + '!')


@clienter.event
async def on_message(message):
    if message.author == clienter.user:
        return
#Display help menu
    if message.content.startswith('$help'):
        embedVar = discord.Embed(title="My Name is Daddy snow", description="Me I go Blame mon, Here is How to use me!", color=0x00ff00)
        embedVar.add_field(name="$help", value="Displays this menu", inline=False)
        embedVar.add_field(name="$start(In Dev)", value="Start the Docker Instance on me PI you will never know where it is!", inline=False)
        embedVar.add_field(name="???",value="Mystery Command? maybe try sending his #1 hit single?",inline=False)
        await message.channel.send(embed=embedVar)
#Start the Docker instance
    elif message.content.startswith('$start'):
        
        dm = discord.Embed(title="Why wo ee",description="Quick! Instance Expires after 30 mins mon")
        dm.add_field(name="http://<ipadddress>:<portnumber>",value="Good luck Tective mon", inline=False)
        
        await message.channel.send(embed=discord.Embed(title="Done!",description="Check Your Dm Mon"))
#secret command 
    elif message.content.startswith(magicw):
        await message.channel.send("Did Somebody say Informer?")
        sleep(1)
        await message.channel.send("https://www.youtube.com/watch?v=TSffz_bl6zo")
    else:
        message.channel.send(embed=discord.Embed(title="want to use me mone?", descriprtion="Try Typing $help"))


pinger.keep_alive()
clienter.run(os.getenv('tokey'))
            
