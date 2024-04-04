import enum, random, sys
from copy import deepcopy

# GAME MODES
class GameMode(enum.IntEnum):
  adventure = 1
  boss = 2
  arena = 3

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
        super().__init__(name, maxhp, maxhp, atk, defense, xp, gold)

class BossEnemy(Enemy):

    def __init__(self, name, maxhp, atk, defense, xp, gold, bonus):
        super().__init__(name, maxhp, maxhp, atk, defense, xp, gold)
        self.bonus = bonus

# ENEMIES
titan = PhysicalEnemy("Titan", 260, 25, 30, 100, 25)
dragon = BossEnemy("Dragon", 590, 95, 100, 550, 120)
dragongiant = BossEnemy("Giant Dragon", 780, 110, 115, 690, 210)

# DISCORD    
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
DISCORD_TOKEN = ("MTE5OTc3MTMyNTgyNTI4NjE3NA.Gj10YZ.V6SjkPlUyPXGShL90Gh-jE2R2rcNnuFxfn9A4E")
bot = commands.Bot(command_prefix="*", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to your Discord!")

bot.run(DISCORD_TOKEN)