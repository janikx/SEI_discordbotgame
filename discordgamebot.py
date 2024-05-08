# WHAT TO DO:
# • discord buttons => spravit okienko kde sa to bude hrat
# • 
# • 
# • 

import random
from copy import deepcopy

# DISCORD    
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord.ui.view import ViewStore

DISCORD_TOKEN = ("MTE5OTc3MTMyNTgyNTI4NjE3NA.G8qfnM.gY7c03PU4xyBG03bmfuKJd9sWG-rYh-l-GZhiQ")
bot = commands.Bot(command_prefix=".", intents= discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot has connected as {bot.user.name} :)")

# LIST OF NEEDED VARIABLES

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
    ### chance 1:15 for a rare

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

# .USERINFO .UI
@bot.command(aliases = ["ui", "user"])
async def userinfo(ctx):
    embed = discord.Embed(title = f"User info", description = f"This is {ctx.author.name}'s profile <:xiaowhat:1198696436318093402>", color = discord.Color.pink())
    embed.add_field(name= "Level", value= "", inline= False)
    embed.add_field(name= "Currency", value= "")
    embed.add_field(name= "Start Date", value= "")
    embed.add_field(name= "Defeated monsters", value= "")
    embed.add_field(name= "Buddy", value= "", inline= False)
    # embed.set_thumbnail(url= ctx.author.author_url) ##### TO DO - neni .author_url

    await ctx.send(embed = embed)

# MENU, SCREEN
class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Chop", style=discord.ButtonStyle.blurple)
    async def menu1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("You clicked me.")

@bot.command()
async def chopping(ctx):
    view = Menu()
    await ctx.reply(view=view)

bot.run(DISCORD_TOKEN)