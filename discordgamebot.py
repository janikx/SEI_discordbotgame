# WHAT TO DO:
# • discord buttons => spravit okienko kde sa to bude hrat
# • commands z papiera
# • znamka: 1) ZA KOD 2) DOKUMENTACIA / PREZENTACIA - aku kniznicu sme pouzili, ako sme postupovali, skadial je co, co to robi, atd.

import random
from copy import deepcopy

# DISCORD    
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import cooldown, BucketType
from discord.ui.view import ViewStore
from discord.components import Button, ButtonStyle


DISCORD_TOKEN = ("MTE5OTc3MTMyNTgyNTI4NjE3NA.G8qfnM.gY7c03PU4xyBG03bmfuKJd9sWG-rYh-l-GZhiQ")
bot = commands.Bot(command_prefix=".", intents= discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot has connected as {bot.user.name} :)")
userstatus = "unregistered"

# .START
@bot.command(aliases = ["begin"])
async def start(ctx, member:discord.Member= None):
    if member == None:
        member = ctx.message.author
    em = discord.Embed(title= "Welcome to Charming RPG!", description= "Your adventure starts now. You can use .commands for a list of commands. Have fun!", color= discord.Color.pink(), timestamp= ctx.message.created_at)
    em.set_thumbnail(url= member.avatar)
    userstatus = "registered"
    await ctx.send(embed = em)

# .HELP
@bot.command()
async def commands(ctx):
    em=discord.Embed(title= "Charming RPG - Commands", description= "Here's the list of commands you can use!", color= 0x6803ab)
    em.add_field(name="Info", value=".userinfo .inventory", inline=False)
    em.add_field(name="Action", value=".chop .fight .mine", inline=False)
    em.add_field(name="Shop", value=".shop .buy .sell", inline=False)
    em.add_field(name="Artifacts", value=".crate .equip .artifacts", inline=False)
    await ctx.send(embed = em)

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

# ARTIFACTS
artifacts = ["Sword", "Shield", "Axe", "Wand", "Stick", "Ring", "Dagger", "Scythe", "Knife", "Bracelet", "Cape", "Belt", "Gloves"]
artifacts_quality = ["Broken", "Plain", "Iron", "Gold", "Diamond", "Magic", "Mystic", "Legendary"]

# class Artifact():
#     ATK = 
    
# # .ARTIFACTINFO
# @bot.command(aliases = ["ai", "arti"])
# async def artifactinfo(ctx, artifact: None):
#     em = discord.Embed(title="Currently equiped artifact", description=f"These are the stats of {current_artifact}.", color=0x6803ab)
#     em.add_field(name="ATK", value= f"{ATK}", inline=True)
#     em.add_field(name="HP", value= f"{HP}", inline=True)
#     em.add_field(name="Magic", value= f"{Magic}", inline=True)
#     em.add_field(name="Quality", value= f"{current_artifact_quality}", inline=True)
#     await ctx.send(embed = em)

# .COOLDOWNS .CD
@bot.command(aliases = ["cd", "cooldown"])
async def cooldowns(ctx):
    await ctx.send(embed = discord.Embed(title = f"Cooldowns", description = f":watch:Mine :watch:Chop :watch:Plant :watch:Hunt :watch:Boss", color = discord.Color.dark_gray()))

# .USERINFO .UI
@bot.command(aliases = ["ui", "user", "whois", "uinfo"])
async def userinfo(ctx, member:discord.Member= None):
    if member == None:
        member = ctx.message.author
    if userstatus == "registered":
        em = discord.Embed(title= "User Info", description= f"Here is the user info for user {member.name}", color= discord.Color.pink(), timestamp= ctx.message.created_at)
        em.set_thumbnail(url= member.avatar)
        em.add_field(name= "ID", value= member.id)
        em.add_field(name= "Name", value= member.name)
        em.add_field(name= "Created At", value= member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
        em.add_field(name= "Joined At", value= member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
        await ctx.send(embed = em)
    else:
        em = discord.Embed(title= "Unregistered!", description= "Please us command .start to use other commands. Thank you.", color= 10038562, timestamp= ctx.message.created_at)
        await ctx.send(embed = em)

# .SHUTDOWN
@bot.command(aliases = ["sd", "shut", "turnoff"])
async def shutdown(ctx, value):
    if value == "password":
        await ctx.send("The bot shutted down successfuly.")
        await bot.close()
    else:
        await ctx.send("You wrote the wrong password, try again.")

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