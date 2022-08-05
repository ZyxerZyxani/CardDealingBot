import sys
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random

#Spades
#Hearts
#Diamonds
#Clubs

client = commands.Bot(description="CardBot By Zyxer", command_prefix=".", pm_help = False)

z = 0

@client.event
async def on_ready():
    channel = client.get_channel(1005054480791904366)
    await channel.send("Hello, I will be your card dealer when requested to. I promise you can trust me and nothing is rigged.")

deck = []
x = int
n = '\n'
x = 0
while (x < 9):
    card = '{}S'.format(x + 2)
    deck.append(card)
    x = x + 1
clothed = 'QS'
deck.append(clothed)
clothed = 'KS'
deck.append(clothed)
clothed = 'AS'
deck.append(clothed)
clothed = 'JS'
deck.append(clothed)

x = 0
while (x < 9):
    card = '{}H'.format(x + 2)
    deck.append(card)
    x = x + 1
clothed = 'QH'
deck.append(clothed)
clothed = 'KH'
deck.append(clothed)
clothed = 'AH'
deck.append(clothed)
clothed = 'JH'
deck.append(clothed)

x = 0
while (x < 9):
    card = '{}D'.format(x + 2)
    deck.append(card)
    x = x + 1
clothed = 'QD'
deck.append(clothed)
clothed = 'KD'
deck.append(clothed)
clothed = 'AD'
deck.append(clothed)
clothed = 'JD'
deck.append(clothed)

x = 0
while (x < 9):
    card = '{}C'.format(x + 2)
    deck.append(card)
    x = x + 1
clothed = 'QC'
deck.append(clothed)
clothed = 'KC'
deck.append(clothed)
clothed = 'AC'
deck.append(clothed)
clothed = 'JC'
deck.append(clothed)

random.shuffle(deck)

cdeck = deck

@client.command(pass_context=True)
async def draw(ctx, x):
    y = int(x)
#    z = z + y
#    if z >= 52:
#        msg = "You are out of cards boys and gals"
#        return
#    else:
    msg = "{}".format(deck[:y])
    await ctx.message.author.send (msg)
#    msg = "{ctx.message.author.mention}".format
#    msg0 = format(msg)
    msg1 ="{} has drawn {} card(s).".format(ctx.message.author.mention, y)
    await ctx.message.channel.send(msg1)
    del deck[:y]

@client.command(pass_context=True)
async def drawu(ctx, x):
    y = int(x)
    msg = "{} drew {}".format(ctx.message.author.mention, deck[:y])
    await ctx.message.channel.send(msg)
    del deck[:y]

@client.command(pass_context=True)
async def putin(ctx, x, u):
    var = str(u)
    if var in deck:
        msg = "Whoa there silly, {} is already in the deck. Are you a cheater? Õ.o".format(u)
        await ctx.message.channel.send(msg)
    elif not var in deck and str.isdigit(x) and int(x) != 0 and var in cdeck:
        deck.insert(int(x)-1, u)
        msg = "{} put {} on place {} from the top of the deck".format(ctx.message.author.mention, u, x)
        await ctx.message.channel.send(msg)
    elif not var in deck and str.isdigit(x) and int(x) ==0 and var in cdeck:
        deck.append(u)
        msg = "{} put {} at the bottom of the deck".format(ctx.message.author.mention, u)
        await ctx.message.channel.send(msg)

    elif not var in deck and not str.isdigit(x) and var in cdeck:
        deck.append(var)
        msg = "{} put {} into the deck and shuffled it.".format(ctx.message.author.mention, u)
        random.shuffle(deck)
        await ctx.message.channel.send(msg)
    elif not var in cdeck:
        msg = "Whoa there silly, {} is not something that belongs in this deck. Please, get it away from me!".format(u)
        await ctx.message.channel.send(msg)
    else:
        msg = "I don't know what the fuck you wrote but this was not predicted. You have made me get a weird error. -sadface-"
        await ctx.message.channel.send(msg)

@client.command(pass_context=True)
async def sdeck(ctx):
    global deck
    deck = []
    x = int
    n = '\n'
    x = 0
    while (x < 9):
        card = '{}S'.format(x + 2)
        deck.append(card)
        x = x + 1
    clothed = 'QS'
    deck.append(clothed)
    clothed = 'KS'
    deck.append(clothed)
    clothed = 'AS'
    deck.append(clothed)
    clothed = 'JS'
    deck.append(clothed)
    
    x = 0
    while (x < 9):
        card = '{}H'.format(x + 2)
        deck.append(card)
        x = x + 1
    clothed = 'QH'
    deck.append(clothed)
    clothed = 'KH'
    deck.append(clothed)
    clothed = 'AH'
    deck.append(clothed)
    clothed = 'JH'
    deck.append(clothed)
    
    x = 0
    while (x < 9):
        card = '{}D'.format(x + 2)
        deck.append(card)
        x = x + 1
    clothed = 'QD'
    deck.append(clothed)
    clothed = 'KD'
    deck.append(clothed)
    clothed = 'AD'
    deck.append(clothed)
    clothed = 'JD'
    deck.append(clothed)
    
    x = 0
    while (x < 9):
        card = '{}C'.format(x + 2)
        deck.append(card)
        x = x + 1
    clothed = 'QC'
    deck.append(clothed)
    clothed = 'KC'
    deck.append(clothed)
    clothed = 'AC'
    deck.append(clothed)
    clothed = 'JC'
    deck.append(clothed)
    
    random.shuffle(deck)
    
    await client.say("The deck is now reset and shuffled.")
    return deck


#####################
@client.command(pass_context=True)
async def ldeck(ctx):
    msg = "{} cards left in the deck.".format(len(deck))
    await ctx.message.channel.send(msg)

@client.command(pass_context=True)
async def cdeck(ctx):
#    a = 1
#    while a <= z:
#        msg += "{}\n".format(deck[:a])
#        a += 1
    msg = "{}".format(deck)
    await ctx.message.channel.send(msg)

@client.command()
async def close(ctx, mirror):
    msg = mirror
    close(msg)

client.run('token')
