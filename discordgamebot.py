import enum, random, sys
from copy import deepcopy

# BASIC CLASSES
class Entity():
  
    def __init__(self, name, hp, maxhp, atk, defense, xp, gold):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.attack = atk
        self.defense = defense
        self.xp = xp
        self.gold = gold

    def fight(self, other): # NEDOKONCENE
        defense = min(other.defense, 19)
        chancetohit = random.randint(0, 20-defense)
        if chancetohit:
            damage = self.attack
        else:
            damage = 0
        other.hp -= damage
        return (self.attack, other.hp <= 0) # fatal dmg

class Character(Entity):
   
    def __init__(self, name, hp, maxhp, atk, defense, ch, chn, level, xp, gold, inventory, mode, user_id):
        super().__init__(name, hp, maxhp, atk, defense, xp, gold)
        self.chakra = ch
        self.level = level
        self.chakranature = chn

        self.inventory = inventory

        self.mode = mode
        self.user_id = user_id

class Enemy(Entity):

    def __init__(self, name, maxhp, atk, defense, xp, gold):
        super().__init__(name, maxhp, maxhp, atk, defense, xp, gold)

# ENEMY CLASSES 
class MagicalEnemy(Enemy):

    def __init__(self, name, maxhp, atk, defense, xp, gold, magic):
        super().__init__(name, maxhp, maxhp, atk, defense, xp, gold)
        self.magic = magic

class PhysicalEnemy(Enemy):

    def __init__(self, name, maxhp, atk, defense, xp, gold):
        super().__init__(name, maxhp, atk, defense, xp, gold)

class BossEnemy(Enemy):

    def __init__(self, name, maxhp, atk, defense, xp, gold, bonus):
        super().__init__(name, maxhp, atk, defense, xp, gold)
        self.bonus = bonus


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