import enum, random, sys
from copy import deepcopy

# DISCORD    
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

DISCORD_TOKEN = ("MTE5OTc3MTMyNTgyNTI4NjE3NA.G8qfnM.gY7c03PU4xyBG03bmfuKJd9sWG-rYh-l-GZhiQ")
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready!")

# .MINE
@bot.command(aliases = ["m", "mn"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def mine(ctx):

    mine_materials = ["stone", "rock", "diorite", "dirt", "iron", "coal", "copper", "granite", "chalk"]
    rare_mine_materials = ["diamond", "gold"]

    mine_luck = [discord.Embed(description = f"{ctx.author.mention} mined in a cave for so long and found a *{random.choice(rare_mine_materials)}*!", color = 1752220), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for few minutes and returned with *{random.choice(mine_materials)}* and *{random.choice(mine_materials)}*.", color = 3426654)]

    mine = random.choice(mine_luck)
    await ctx.send(embed = mine)
@mine.error
async def mine(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title = f"You are too tired to mine again!", description = f"Try again in {error.retry_after:.2f}s.", color = 10038562)
        await ctx.send(embed = em)

bot.run(DISCORD_TOKEN)