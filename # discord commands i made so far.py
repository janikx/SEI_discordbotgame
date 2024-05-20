# discord commands i made so far

import discord, random
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord.ui.view import ViewStore
from discord.components import Button, ButtonStyle

bot = commands.Bot(command_prefix=".", intents= discord.Intents.all())

@bot.command()
async def chop(ctx: commands.Context):
    await ctx.send(f"{ctx.author.mention} u can do this :>", view=MenuButtons())

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

    #    @chop.error
    #     async def chop(ctx, error):
    #         if isinstance(error, commands.CommandOnCooldown):
    #             em = discord.Embed(title = f"You are too tired to chop trees!", description = f"Try again in {error.retry_after:.2f}s.", color = 10038562)
    #             await ctx.send(embed = em)

# .START
@client.command(aliases = ["begin"])
async def start(ctx, member:discord.Member= None):
    if member == None:
        member = ctx.message.author
    em = discord.Embed(title= "Welcome to Charming RPG!", description= "Your adventure starts now. You can use .commands for a list of commands. Have fun!", color= discord.Color.pink(), timestamp= ctx.message.created_at)
    em.set_thumbnail(url= member.avatar)
    userstatus = "registered"
    await ctx.send(embed = em)

discord.Embed(description = f"{interaction.user.display_name} choped trees until they found *{random.choice(rare_chop_materials)}* with their scratched hands!", color = 1752220), discord.Embed(description = f"{interaction.user.display_name} choped down the trees and gained *{random.choice(chop_materials)}.*", color = 3426654), discord.Embed(description = f"{interaction.user.display_name} choped different trees and returned with *{random.choice(chop_materials)}* and *{random.choice(chop_materials)}*.", color = 3426654)
em.add_field(name= "Created At", value= member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))


hunt_luck = [discord.Embed(description = f"{interaction.user.mention} hunted monsters, lost {total_damage} HP and killed **{hunt1}**!", color = 3426654), discord.Embed(description = f"{interaction.user.mention} was attacked by **{hunt2} lost {total_damage} HP but got out of the fight alive.**", color = 3426654), discord.Embed(description = f"{interaction.user.mention} found **{hunt1}** and **{hunt2}** lost {total_damage} HP but killed them.", color = 3426654)]
            chances_hunt = [0.4, 0.3, 0.3]

            if em == discord.Embed(description = f"{interaction.user.mention} hunted monsters, lost {total_damage} HP and killed **{hunt1}**!", color = 3426654):
                player.HP = player.HP - total_damage
            elif em == discord.Embed(description = f"{interaction.user.mention} was attacked by **{hunt2} lost {total_damage} HP but got out of the fight alive.**", color = 3426654):
                player.HP = player.HP - total_damage
            elif em == discord.Embed(description = f"{interaction.user.mention} found **{hunt1}** and **{hunt2}** lost {total_damage} HP but killed them.", color = 3426654):
                player.HP = player.HP - total_damage

            if player.HP <= 0:
                em = hunt_luck + "You died!"random.choices(hunt_luck, chances_hunt)[0]

            em = hunt_em
            await interaction.response.edit_message(embed= em)