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
from discord.components import Button, ButtonStyle

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
class MenuWithButtons(discord.ui.View):
    def __init__(self):
        super.__init__()
        self.add_item(discord.ui.Button(label="Chop"))

    @discord.ui.button(label="Chop", style=discord.ButtonStyle.blurple)
    async def chopbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hiii")

@bot.command()
async def chop(ctx: commands.Context):
    await ctx.send(f"{ctx.author.mention} u can do this :>", view=MenuWithButtons())


bot.run(DISCORD_TOKEN)