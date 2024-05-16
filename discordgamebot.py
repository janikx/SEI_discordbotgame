# WHAT TO DO:
# • discord buttons => spravit okienko kde sa to bude hrat
# • commands z papiera
# • znamka: 1) ZA KOD 2) DOKUMENTACIA / PREZENTACIA - aku kniznicu sme pouzili, ako sme postupovali, skadial je co, co to robi, atd.

# list inv = [] z toho if x in inv, potom equip, else = u dont have that item
# alebo .equip potom vyber for i in range list vypis moznosti a vyber si z toho artefakt

# spravim class USER, potom spravim tam atributy, potom artefakt atributy, potom vytvorim USERA a jeho full atk (scitanie) atd., potom if artifact quality = gold atd. tak podla toho priradim artifact atk bonus atd.

# equip artefaktu = vymazat list a potom dosadit novy artefakt

# IMPORTS  
import discord, random, datetime
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import cooldown, BucketType
from discord.ui.view import ViewStore
from discord.components import Button, ButtonStyle

DISCORD_TOKEN = ("MTE5OTc3MTMyNTgyNTI4NjE3NA.G8qfnM.gY7c03PU4xyBG03bmfuKJd9sWG-rYh-l-GZhiQ")
client = commands.Bot(command_prefix=".", intents= discord.Intents.all())

class User:
    ATK: int
    HP: int
    Magic: int
    registered: bool

    def __init__(self, atk, hp, magic, registered):
        self.ATK = atk
        self.HP = hp
        self.Magic = magic
        self.registered = registered

# USER
user = User(10, 30, 1, True)

# USER INVENTORY AND ARTIFACTS
inventory = []
artifacts_inv = []

@client.event
async def on_ready():
    print(f"Bot has connected as {client.user.name} :)")
    await client.tree.sync()

# START
@client.tree.command(name="start", description="Use START to play the game.")
async def start(interaction: discord.Interaction):
    em = discord.Embed(title= "Welcome to Charming RPG!", description= "Your adventure starts now. You can use /COMMANDS for a list of commands. Have fun!", color= discord.Color.pink(), timestamp=datetime.datetime.utcnow())
    em.set_thumbnail(url= interaction.user.avatar)
    registered = True
    await interaction.response.send_message(embed= em)

# HELP
@client.tree.command(name= "commands", description="Shows a list of all avaiable COMMANDS.")
async def commands(interaction: discord.Interaction):
    em= discord.Embed(title= "Charming RPG - Commands", description= f"{interaction.user.mention} here's the list of commands!", color= 0x6803ab)
    em.add_field(name="Info", value=".userinfo .inventory", inline=False)
    em.add_field(name="Action", value=".chop .fight .mine", inline=False)
    em.add_field(name="Shop", value=".shop .buy .sell", inline=False)
    em.add_field(name="Artifacts", value=".crate .equip .artifacts", inline=False)
    await interaction.response.send_message(embed= em, ephemeral= True)

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
hurt = ["1", "2", "3", "4", "5", "6", "7"]

animals = ["horse", "cat", "dog", "chicken", "duck", "pig", "wolf", "capybara", "eagle", "bear"]
boss_enemies = ["titan", "dragon", "ancient robot", "serpent"]

# ARTIFACTS
artifacts = ["Sword", "Shield", "Axe", "Wand", "Stick", "Ring", "Dagger", "Scythe", "Knife", "Bracelet", "Cape", "Belt", "Gloves"]
artifacts_quality = ["Broken", "Plain", "Iron", "Gold", "Diamond", "Magic", "Mystic", "Legendary"]

# class Artifact():
#     ATK = 
    
# ARTIFACTS
# @client.tree.command(name= "artifacts", description= "Menu to show artifacts.")
# async def artifacts(interaction: discord.Interaction):
#     em = discord.Embed(title="Currently equiped artifact", description=f"These are the stats of {current_artifact}.", color=0x6803ab)
#     em.add_field(name="ATK", value= f"{ATK}", inline=True)
#     em.add_field(name="HP", value= f"{HP}", inline=True)
#     em.add_field(name="Magic", value= f"{Magic}", inline=True)
#     em.add_field(name="Quality", value= f"{current_artifact_quality}", inline=True)
#     await interaction.response.send_message(embed= em)

# USERINFO
@client.tree.command(name="userinfo", description="Shows information about any user.")
async def userinfo(interaction: discord.Interaction, member: discord.Member= None):
    if member == None:
        member = interaction.user
    em = discord.Embed(title= "User Info", description= f"Here is the user info for user {member.name}", color= discord.Color.pink(), timestamp= datetime.datetime.utcnow())
    em.set_thumbnail(url= member.avatar)
    em.add_field(name= "ID", value= member.id)
    em.add_field(name= "Name", value= member.name)
    em.add_field(name= "Created At", value= member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
    em.add_field(name= "Joined At", value= interaction.user.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
    await interaction.response.send_message(embed= em)

# .PULL
# @client.tree.command(name= "pull", description= "Pulls an artifact once in 24h.")
# async def pull(interaction: discord.Interaction):
#     quality = random.choice(artifacts_quality)
#     artifact = random.choice(artifacts)
#     em = discord.Embed(title= "Pulled Artifact", description= f"You have pulled *{quality} {artifact}*.", color= discord.Color.pink())
#     await interaction.response.send_message(embed= em)

# SHUTDOWN
@client.tree.command(name="shutdown", description="Shuts down the bot.")
async def shutdown(interaction: discord.Interaction):
    await interaction.response.send_message(content="The bot shutted down successfuly.")
    await client.close()

# MENU, SCREEN
class MenuButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label="Chop", style=discord.ButtonStyle.blurple)
    async def chopbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
            
            choprare = random.choice(rare_chop_materials)
            chop1 = random.choice(chop_materials)
            chop2 = random.choice(chop_materials)

            chop_luck = [discord.Embed(description = f"{interaction.user.mention} choped trees until they found **{choprare}** with their scratched hands!", color = 1752220), discord.Embed(description = f"{interaction.user.mention} choped down the trees and gained **{chop1}.**", color = 3426654), discord.Embed(description = f"{interaction.user.mention} choped different trees and returned with **{chop1}** and **{chop2}**.", color = 3426654)]
            chances_mine = [0.05, 0.65, 0.3]

            chop = random.choices(chop_luck, chances_mine)[0]
            await interaction.response.edit_message(embed= chop)
            
            if chop1 not in inventory:
                inventory.append(chop1)
            
            if chop2 not in inventory:
                inventory.append(chop2)
            
            if choprare not in inventory:
                inventory.append(choprare) 

    @discord.ui.button(label= "Mine", style= discord.ButtonStyle.blurple)
    async def minebutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
            mine_luck = [discord.Embed(description = f"{interaction.user.mention} mined in a cave for so long and found a **{random.choice(rare_mine_materials)}**!", color = 3426654), discord.Embed(description = f"{interaction.user.mention} mined in a cave for a while and found **{random.choice(mine_materials)}.**", color = 3426654), discord.Embed(description = f"{interaction.user.mention} mined in a cave for few minutes and returned with **{random.choice(mine_materials)}** and **{random.choice(mine_materials)}**.", color = 3426654)]
            chances_chop = [0.05, 0.65, 0.3]

            mine = random.choices(mine_luck, chances_chop)[0]
            await interaction.response.edit_message(embed= mine)

    @discord.ui.button(label= "Hunt", style= discord.ButtonStyle.blurple)
    async def huntbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
            hunt_luck = [discord.Embed(description = f"{interaction.user.mention} hunted monsters and killed **{random.choice(enemies)}**!", color = 3426654), discord.Embed(description = f"{interaction.user.mention} was attacked by **{random.choice(enemies)} lost {random.choice(hurt)} HP but got out of the fight alive.**", color = 3426654), discord.Embed(description = f"{interaction.user.mention} found **{random.choice(enemies)}** and **{random.choice(enemies)}** and killed them.", color = 3426654)]
            chances_hunt = [0.3, 0.4, 0.3]

            hunt = random.choices(hunt_luck, chances_hunt)[0]
            await interaction.response.edit_message(embed= hunt)

@client.tree.command(name= "action", description= "Menu to do perform an ACTION")
async def actionmenu(interaction: discord.Interaction):
    em = discord.Embed(description= "What action do you want to make?", color = 1146986)
    await interaction.response.send_message(embed= em, view= MenuButtons())

client.run(DISCORD_TOKEN)