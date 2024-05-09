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
@bot.command(aliases = ["ui", "user", "whois", "uinfo"])
async def userinfo(ctx, member:discord.Member= None):
    if member == None:
        member = ctx.message.author
    em = discord.Embed(title= "User Info", description= f"Here is the user info for user {member.name}", color= discord.Color.pink(), timestamp= ctx.message.created_at)
    em.set_thumbnail(url= member.avatar)
    em.add_field(name= "ID", value= member.id)
    em.add_field(name= "Name", value= member.name)
    # em.add_field(name= "Joined At", value= "")

    await ctx.send(embed = em)

# MENU, SCREEN
class MenuButtons(discord.ui.View):
    def __init__(self):
        super.__init__()
        self.add_item(discord.ui.Button(label="Chop"))
        self.add_item(discord.ui.Button(label="Mine"))

    @discord.ui.button(label="Chop", style=discord.ButtonStyle.blurple)
    async def chopbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        async def chop(ctx):
            chop_luck = [discord.Embed(description = f"{ctx.author.mention} choped trees until they found *{random.choice(rare_chop_materials)}* with their scratched hands!", color = 1752220), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{ctx.author.mention} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654)]
            chop = random.choice(chop_luck)
            await ctx.send(embed = chop)
        @chop.error
        async def chop(ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
                em = discord.Embed(title = f"You are too tired to chop trees!", description = f"Try again in {error.retry_after:.2f}s.", color = 10038562)
                await ctx.send(embed = em)

    @discord.ui.button(label="Mine", style=discord.ButtonStyle.blurple)
    async def minebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
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

bot.run(DISCORD_TOKEN)