# discord commands i made so far
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord.ui.view import ViewStore
from discord.components import Button, ButtonStyle

bot = commands.Bot(command_prefix=".", intents= discord.Intents.all())

# MINE
mine_materials = ["stone", "rock", "diorite", "dirt", "iron", "coal", "copper", "granite", "chalk"]
rare_mine_materials = ["diamond"]

# CHOP
chop_materials = ["wood", "stick", "leaf", "apple"]
rare_chop_materials = ["golden apple"]

# PLANT
plants = ["tulip", "dandelion", "rose", "buttercup", "camellia", "columbine", "dahlia"]
rare_plants = ["fire lily", "orchid", "jade vine"]

# ENTITIES
enemies = ["zombie", "skeleton", "spider", "corpse", "ghost", "vampire", "witch", "demon"]
animals = ["horse", "cat", "dog", "chicken", "duck", "pig", "wolf", "capybara", "eagle", "bear"]
boss_enemies = ["titan", "dragon", "ancient robot", "serpent"]

# .MINE .M .MN
@bot.command(aliases = ["m", "mn"])
@commands.cooldown(1, 600, commands.BucketType.user)
async def mine(ctx):

    mine_luck = [discord.Embed(description = f"{ctx.author.mention} mined in a cave for so long and found a *{random.choice(rare_mine_materials)}*!", color = 1752220), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for few minutes and returned with *{random.choice(mine_materials)}* and *{random.choice(mine_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for few minutes and returned with *{random.choice(mine_materials)}* and *{random.choice(mine_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for few minutes and returned with *{random.choice(mine_materials)}* and *{random.choice(mine_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} mined in a cave for a while and found *{random.choice(mine_materials)}.*", color = 3426654)]
    # chance 1:15 for a rare

    mine = random.choice(mine_luck)
    await ctx.send(embed = mine)
@mine.error
async def mine(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title = f"You are too tired to mine!", description = f"Try again in {error.retry_after:.2f}s.", color = 10038562)
        await ctx.send(embed = em)

# .CHOP .CH .C
@bot.command(aliases = ["c", "ch"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def chop(ctx):

    chop_luck = [discord.Embed(description = f"{ctx.author.mention} choped trees until they found *{random.choice(rare_chop_materials)}* with their scratched hands!", color = 1752220), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654)]

    chop = random.choice(chop_luck)
    await ctx.send(embed = chop)
@chop.error
async def chop(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title = f"You are too tired to chop trees!", description = f"Try again in {error.retry_after:.2f}s.", color = 10038562)
        await ctx.send(embed = em)

# .COOLDOWNS .CD
@bot.command(aliases = ["cd", "cooldown"])
async def cooldowns(ctx):
    await ctx.send(embed = discord.Embed(title = f"Cooldowns", description = f":watch:Mine :watch:Chop :watch:Plant :watch:Hunt :watch:Boss", color = discord.Color.dark_gray()))