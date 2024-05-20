# WHAT TO DO:
# • discord buttons => spravit okienko kde sa to bude hrat
# • commands z papiera
# • znamka: 1) ZA KOD 2) DOKUMENTACIA / PREZENTACIA - aku kniznicu sme pouzili, ako sme postupovali, skadial je co, co to robi, atd.

# list inv = [] z toho if x in inv, potom equip, else = u dont have that item
# alebo .equip potom vyber for i in range list vypis moznosti a vyber si z toho artefakt

# spravim class USER, potom spravim tam atributy, potom artefakt atributy, potom vytvorim USERA a jeho full atk (scitanie) atd., potom if artifact quality = gold atd. tak podla toho priradim artifact atk bonus atd.
# equip artefaktu = vymazat list a potom dosadit novy artefakt

# COLORS
red = 15548997
green = 5763719
darkaqua = 1146986
lightgrey = 9807270
vividpink = 15277667
pink = 15418782
purple = 10181046
yellow = 15844367
black = 2303786
white = 16777215

# IMPORTS  
import discord, random, datetime, asyncio
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import cooldown, BucketType
from discord.ui.view import ViewStore
from discord.components import Button, ButtonStyle
from collections import Counter

DISCORD_TOKEN = ("MTE5OTc3MTMyNTgyNTI4NjE3NA.G8qfnM.gY7c03PU4xyBG03bmfuKJd9sWG-rYh-l-GZhiQ")
client = commands.Bot(command_prefix=".", intents= discord.Intents.all())

class User:
    HP: int
    MaxHP: int
    RES: int
    registered: bool
    Money: int
    Lvl: int
    XP: int
    LvlUpXP: int
    Title: str

    BonusMoney: int
    BonusXP: int

    def __init__(self, hp, maxhp, res, money, lvl, xp, xptolvlup, registered, title, bonusmoney, bonusxp):
        self.HP = hp
        self.MaxHP = maxhp
        self.RES = res
        self.Money = money
        self.Lvl = lvl
        self.XP = xp
        self.LvlUpXP = xptolvlup
        self.registered = registered
        self.Title = title

        self.BonusMoney = bonusmoney
        self.BonusXP = bonusxp

class Pet:
    Name: str
    Type: str
    Price: int
    Happiness: int

    def __init__(self, name, atype, price, happiness):
        self.Name = name
        self.Type = atype
        self.Price = price
        self.Happiness = happiness

# PLAYER AND PET
player = User(30, 30, 10, 0, 1, 0, 50, True, "no title", 1, 1)
pet = Pet("Cat", "cat", 550, 100)

chicken = Pet("Chicken", "chicken", 300, 100)
duck = Pet("Duck", "duck", 350, 100)
pig = Pet("Pig", "pig", 450, 100)
rabbit = Pet("Rabbit", "rabbit", 450, 100)
dog = Pet("Dog", "dog", 550, 100)
cat = Pet("Cat", "cat", 550, 100)
horse = Pet("Horse", "horse", 700, 100)
wolf = Pet("Wolf", "wolf", 750, 100)
octopus = Pet("Octopus", "octopus", 850, 100)
eagle = Pet("Eagle", "eagle", 900, 100)
snake = Pet("Snake", "snake", 1000, 100)
shark = Pet("Shark", "shark", 1000, 100)
bear = Pet("Bear", "bear", 1100, 100)
lion = Pet("Lion", "lion", 1500, 100)
mini_dragon = Pet("Mini Dragon", "dragon_face", 2200, 100)
unicorn = Pet("Unicorn", "unicorn", 3800, 100)

# LEVEL UP FUNC
def LevelUpChecker():
    if player.XP >= player.LvlUpXP:
        lvl_up = True
        player.XP = (player.XP - player.LvlUpXP)
        player.Lvl += 1

        if player.Lvl <= 6:
            player.LvlUpXP = int(player.LvlUpXP * 2)
        elif player.Lvl <= 10:
            player.LvlUpXP = int(player.LvlUpXP * 1.5)
        elif player.Lvl > 10:
            player.LvlUpXP = int(player.LvlUpXP * 1.2)

        if player.Lvl % 10 == 0:
            player.Money = player.Lvl * 100
        elif player.Lvl % 5 == 0:
            player.Money = player.Lvl * 70
        else:
            player.Money = player.Lvl * 50
    else:
        lvl_up = False
    return player.XP, player.LvlUpXP, player.Lvl, player.Money, lvl_up

@client.event
async def on_ready():
    print(f"Bot has connected as {client.user.name} :)")
    await client.tree.sync()

# START
@client.tree.command(name="start", description="Use START to play the game.")
async def start(interaction: discord.Interaction):
    em = discord.Embed(title= "Welcome to Charming RPG!", description= "Your adventure starts now. You can use /COMMANDS for a list of commands. Have fun!", color= discord.Color.pink(), timestamp=datetime.datetime.utcnow())
    em.set_thumbnail(url= interaction.user.avatar)
    player.registered = True
    joined_the_game_time = datetime.datetime.utcnow()
    await interaction.response.send_message(embed= em)
    return joined_the_game_time

# HELP
@client.tree.command(name= "commands", description="Shows a list of all avaiable COMMANDS.")
async def commands(interaction: discord.Interaction):
    em= discord.Embed(title= "Charming RPG - Commands", description= f"{interaction.user.mention} here's the list of commands!", color= 0x6803ab)
    em.add_field(name="Info :mag:", value=".userinfo .inventory", inline=False)
    em.add_field(name="Action :pick:", value=".chop .fight .mine", inline=False)
    em.add_field(name="Shop :shopping_cart:", value=".shop .buy .sell", inline=False)
    em.add_field(name="Artifacts :crystal_ball:", value=".crate .equip .artifacts", inline=False)
    await interaction.response.send_message(embed= em, ephemeral= True)

# LIST OF NEEDED VARIABLES
# MINE
mine_materials = [":rock: rock", ":: diorite", ":: dirt", ":: iron", ":: coal", ":: copper", ":: granite", ":: chalk"]
rare_mine_materials = [":gem: diamond"]

# CHOP
chop_materials = [":wood: wood", ":herb: stick", ":leaves: leaf", ":green_apple: apple"]
rare_chop_materials = [":apple: magic apple"]

# PLANT
plants = ["tulip", "dandelion", "rose", "buttercup", "camellia", "columbine", "dahlia"]
rare_plants = ["fire lily", "orchid", "jade vine"]

# ENTITIES
enemies = [":zombie: zombie", ":skull: skeleton", ":spider: spider", ":ghost: ghost", ":vampire: vampire", ":man_mage: witch", ":supervillain: supervillain", ":ogre: demon", ":troll: troll", ":genie: bad genie", ":mermaid: evil mermaid", ":t_rex: t-rex"]
boss_enemies = ["Titan", "Dragon", "Ancient robot", "Serpent"]
pets = ["chicken", "duck", "pig", "rabbit", "dog", "cat", "horse", "wolf", "octopus", "eagle", "snake", "shark", "bear", "lion", "minidragon", "unicorn"]

# ARTIFACTS
artifacts = ["Sword", "Shield", "Axe", "Wand", "Stick", "Ring", "Dagger", "Scythe", "Knife", "Bracelet", "Cape", "Belt", "Gloves"]
artifacts_quality = ["Broken", "Plain", "Iron", "Gold", "Diamond", "Magic", "Mystic", "Legendary"]

# ARTIFACTS
artifacts_inv = []
# @client.tree.command(name= "artifacts", description= "Menu to show artifacts.")
# async def artifacts(interaction: discord.Interaction):
#     em = discord.Embed(title="Currently equiped artifact", description=f"These are the stats of {current_artifact}.", color=0x6803ab)
#     em.add_field(name="HP", value= f"{HP}", inline=True)
#     em.add_field(name="ATK", value= f"{ATK}", inline=True)
#     em.add_field(name="Quality", value= f"{current_artifact_quality}", inline=True)
#     await interaction.response.send_message(embed= em)

# INVENTORY
inventory_items = []

@client.tree.command(name= "inventory", description= "Shows inventory of a player.")
async def inventory(interaction: discord.Interaction):
    if len(inventory_items) == 0:
        em = discord.Embed(title= "Your inventory", description= "Your inventory is empty.", color = 1146986)
        await interaction.response.send_message(embed= em)
    else:
        counter = Counter(inventory_items)
        inventory_dictionary = dict(counter)
        em = discord.Embed(title= "Your inventory", description= '\n'.join([f"{item}: {count}" for item, count in counter.items()]), color = 1146986)
        await interaction.response.send_message(embed= em)

# USERINFO
@client.tree.command(name="userinfo", description="Shows information about any user.")
async def userinfo(interaction: discord.Interaction, member: discord.Member= None):
    if member == None:
        member = interaction.user
    em = discord.Embed(title= "User Info", description= f"Here is the user info for user {member.name} :bust_in_silhouette:", color= discord.Color.pink(), timestamp= datetime.datetime.utcnow())
    em.set_thumbnail(url= member.avatar)
    em.add_field(name= "Info :mag:", value= f"Name: **{interaction.user.mention}**\nTitle: **{player.Title}**\nID: *{member.id}*")
    em.add_field(name= "Game status :video_game:", value= f":hearts: HP: **{player.HP}/{player.MaxHP}**\n:money_with_wings: Balance: **{player.Money}$**\n:chart_with_upwards_trend: Level: **{player.Lvl}**\nXP: **{player.XP} / {player.LvlUpXP} xp**")
    if pet.Type == "-":
        pet_type = f"{pet.Type}"
    else:
        pet_type = f":{pet.Type}: {pet.Type}"
    em.add_field(name= "Pet :paw_prints:", value= f"Name: **{pet.Name}**\nType: *{pet_type}*\nHappiness: *{pet.Happiness} / 100*")
    await interaction.response.send_message(embed= em)

# SHUTDOWN
@client.tree.command(name="shutdown", description="Shuts down the bot.")
async def shutdown(interaction: discord.Interaction):
    ListOfAdmins = [532640698114113556]
    if interaction.user.id in ListOfAdmins:# (my ID, no one except me can use this)
        await interaction.response.send_message(content= f"*The **{client.user.name}** shutted down successfuly.*", ephemeral= True)
        await client.close()
    else:
        await interaction.response.send_message(content= f"*You do not have a permission to use this.*", ephemeral= True)
        

# ACTIONMENU
class ActionMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label= "Chop", style=discord.ButtonStyle.blurple) # kazdych 10 minut
    async def chopbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
            choprare = random.choice(rare_chop_materials)
            chop1 = random.choice(chop_materials)
            chop2 = random.choice(chop_materials)
            while chop2 == chop1:
                chop2 = random.choice(chop_materials)
            earned_xp = random.randint(15, 25) * player.BonusXP
            earned_money = random.randint(10, 25) * player.BonusMoney
            chop_luck = [f"{interaction.user.mention} choped trees until they found **{choprare}** with their scratched hands!",f"{interaction.user.mention} choped down the trees and gained **{chop1}.**",f"{interaction.user.mention} choped different trees and returned with **{chop1}** and **{chop2}**."]
            chances_mine = [0.05, 0.65, 0.3]

            player.Money = player.Money + earned_money
            player.XP = player.XP + earned_xp

            lvl_up_checker = LevelUpChecker()
            player.XP = lvl_up_checker[0]
            player.LvlUpXP = lvl_up_checker[1]
            player.Lvl = lvl_up_checker[2]
            player.Money = lvl_up_checker[3]
            lvl_up = lvl_up_checker[4]

            em = random.choices(chop_luck, chances_mine)[0]
            if lvl_up == True:
                await interaction.response.edit_message(embed= discord.Embed(title= ":axe: Chopping...", description = em + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*\n \n**Oh.. You're now level {player.Lvl}! :chart_with_upwards_trend:**", color= 3426654))
            else:
                await interaction.response.edit_message(embed= discord.Embed(title= ":axe: Chopping...", description = em + f"\n \n*Balance:* **+ {earned_money}$**" + f"\n*+ {earned_xp} xp*", color= 3426654))

            if em == f"{interaction.user.mention} choped trees until they found **{choprare}** with their scratched hands!":
                inventory_items.append(choprare)
            if em == f"{interaction.user.mention} choped down the trees and gained **{chop1}.**":
                inventory_items.append(chop1)
            if em == f"{interaction.user.mention} choped different trees and returned with **{chop1}** and **{chop2}**.":
                inventory_items.append(chop1)
                inventory_items.append(chop2)

    @discord.ui.button(label= "Mine", style= discord.ButtonStyle.blurple) # kazdu pol hodinu
    async def minebutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
            minerare = random.choice(rare_mine_materials)
            mine1 = random.choice(mine_materials)
            mine2 = random.choice(mine_materials)
            while mine2 == mine1:
                mine2 = random.choice(mine_materials)
            earned_xp = random.randint(25, 35) * player.BonusXP
            earned_money = random.randint(25, 35) * player.BonusMoney
            mine_luck = [f"{interaction.user.mention} mined in a cave for so long and found a **{minerare}**!",f"{interaction.user.mention} mined in a cave for a while and found **{mine1}.**",f"{interaction.user.mention} mined in a cave for few minutes and returned with **{mine1}** and **{mine2}**."]
            chances_chop = [0.05, 0.65, 0.3]

            player.Money = player.Money + earned_money
            player.XP = player.XP + earned_xp

            lvl_up_checker = LevelUpChecker()
            player.XP = lvl_up_checker[0]
            player.LvlUpXP = lvl_up_checker[1]
            player.Lvl = lvl_up_checker[2]
            player.Money = lvl_up_checker[3]
            lvl_up = lvl_up_checker[4]

            em = random.choices(mine_luck, chances_chop)[0]
            if lvl_up == True:
                await interaction.response.edit_message(embed= discord.Embed(title= ":pick: Mining...", description= em + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*\n \n**Oh.. You're now level {player.Lvl}! :chart_with_upwards_trend:**", color = 3426654))
            else:
                await interaction.response.edit_message(embed= discord.Embed(title= ":pick: Mining...", description= em + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*", color = 3426654))

            if em == f"{interaction.user.mention} mined in a cave for so long and found a **{minerare}**!":
                inventory_items.append(minerare)
            if em == f"{interaction.user.mention} mined in a cave for a while and found **{mine1}.**":
                inventory_items.append(mine1)
            if em == f"{interaction.user.mention} mined in a cave for few minutes and returned with **{mine1}** and **{mine2}**.":
                inventory_items.append(mine1)
                inventory_items.append(mine2)

    @discord.ui.button(label= "Hunt", style= discord.ButtonStyle.blurple) # kazdu minutu
    async def huntbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
            hunt1 = random.choice(enemies)
            hunt2 = random.choice(enemies)
            while hunt1 == hunt2:
                hunt2 = random.choice(enemies)
            
            damage = [1, 2, 3, 4, 5, 6]
            critical_damage = int(player.MaxHP * ( 1/3 ))
            chances_damage = [0.25, 0.2, 0.2, 0.15, 0.13, 0.07]
            total_damage = random.choices(damage, chances_damage)[0]
            earned_money = random.randint(15, 30) * player.BonusMoney
            extra_money = random.randint(40, 50) * player.BonusMoney
            earned_xp = random.randint(5, 9) * player.BonusXP

            hunt_luck = [f"{interaction.user.mention} hunted monsters, lost *{total_damage} HP* and killed **{hunt1}**!",f"{interaction.user.mention} was attacked by **{hunt2}** lost *{critical_damage} HP* but got out of the fight alive.",f"{interaction.user.mention} found **{hunt1}** and **{hunt2}** lost *{total_damage} HP* but killed them."]
            chances_hunt = [0.53, 0.05, 0.42]
            hunt_result = random.choices(hunt_luck, chances_hunt)[0]
            player.XP = player.XP + earned_xp

            lvl_up_checker = LevelUpChecker()
            player.XP = lvl_up_checker[0]
            player.LvlUpXP = lvl_up_checker[1]
            player.Lvl = lvl_up_checker[2]
            player.Money = lvl_up_checker[3]
            lvl_up = lvl_up_checker[4]

            if lvl_up == True:
                if hunt_result == f"{interaction.user.mention} hunted monsters, lost *{total_damage} HP* and killed **{hunt1}**!":
                    player.HP = player.HP - total_damage
                    player.Money = player.Money + earned_money
                    em = discord.Embed(title= ":archery: Hunting...", description = f"{interaction.user.mention} hunted monsters, lost *{total_damage} HP* and killed **{hunt1}**!" + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*\n \n**Oh.. You're now level {player.Lvl}! :chart_with_upwards_trend:**", color = 3426654)
                elif hunt_result == f"{interaction.user.mention} was attacked by **{hunt2}** lost *{critical_damage} HP* but got out of the fight alive.":
                    player.HP = player.HP - total_damage
                    player.Money = player.Money + extra_money
                    em = discord.Embed(title= ":archery: Hunting...", description = f"{interaction.user.mention} was attacked by **{hunt2}** lost *{critical_damage} HP* but got out of the fight alive." + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*\n \n**Oh.. You're now level {player.Lvl}! :chart_with_upwards_trend:**", color = 3426654)
                elif hunt_result == f"{interaction.user.mention} found **{hunt1}** and **{hunt2}** lost *{total_damage} HP* but killed them.":
                    player.HP = player.HP - total_damage
                    player.Money = player.Money + earned_money
                    em = discord.Embed(title= ":archery: Hunting...", description = f"{interaction.user.mention} found **{hunt1}** and **{hunt2}** lost *{total_damage} HP* but killed them." + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*\n \n**Oh.. You're now level {player.Lvl}! :chart_with_upwards_trend:**", color = 3426654)
                if player.HP <= 0:
                    player.HP = 0
                    em = discord.Embed(title= "Hunting...", description= f"{interaction.user.mention} was attacked by {hunt2} and it was fatal." + f"\n**They died and lost all their XP :(**", color = 3426654)
            else:
                if hunt_result == f"{interaction.user.mention} hunted monsters, lost *{total_damage} HP* and killed **{hunt1}**!":
                    player.HP = player.HP - total_damage
                    player.Money = player.Money + earned_money
                    em = discord.Embed(title= ":archery: Hunting...", description = f"{interaction.user.mention} hunted monsters, lost *{total_damage} HP* and killed **{hunt1}**!" + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*", color = 3426654)
                elif hunt_result == f"{interaction.user.mention} was attacked by **{hunt2}** lost *{critical_damage} HP* but got out of the fight alive.":
                    player.HP = player.HP - total_damage
                    player.Money = player.Money + extra_money
                    em = discord.Embed(title= ":archery: Hunting...", description = f"{interaction.user.mention} was attacked by **{hunt2}** lost *{critical_damage} HP* but got out of the fight alive." + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*", color = 3426654)
                elif hunt_result == f"{interaction.user.mention} found **{hunt1}** and **{hunt2}** lost *{total_damage} HP* but killed them.":
                    player.HP = player.HP - total_damage
                    player.Money = player.Money + earned_money
                    em = discord.Embed(title= ":archery: Hunting...", description = f"{interaction.user.mention} found **{hunt1}** and **{hunt2}** lost *{total_damage} HP* but killed them." + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*", color = 3426654)
                if player.HP <= 0:
                    player.HP = 0
                    em = discord.Embed(title= "Hunting...", description= f"{interaction.user.mention} was attacked by {hunt2} and it was fatal." + f"\n**They died and lost all their XP :(**", color = 3426654)

            await interaction.response.edit_message(embed= em)

    # @discord.ui.button(label= "Boss Hunt", style= discord.ButtonStyle.red) # kazdych 24 hodin
    # async def bossbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
    #         boss = random.choice(boss_enemies)
    #         em = discord.Embed(title= f"{boss} appeared!!!", description= "")
    #         damage = [1, 2, 3, 4, 5, 6]
    #         critical_damage = 
    #         chances_damage = [0.25, 0.2, 0.2, 0.15, 0.13, 0.07]
    #         total_damage = random.choices(damage, chances_damage)[0]
    #         earned_money = random.randint(200, 300)

    #         boss_fight = []
    #         chances_hunt = [0.53, 0.05, 0.42]
    #         boss_result = random.choices(boss_fight, chances_hunt)[0]

    #         await interaction.response.edit_message(embed= em)

@client.tree.command(name= "action", description= "Menu to do perform an ACTION")
async def actionmenu(interaction: discord.Interaction):
    em = discord.Embed(title= "Action", description= f"{interaction.user.mention}, what action do you want to make?", color = 3447003)
    await interaction.response.send_message(embed= em, view= ActionMenu())

# SHOPMENU - titles, pets, potions(healing, bonus gold, bonus xp, bonus atk when boss fight)
class ShopMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label= "Pets", style=discord.ButtonStyle.green)
    async def petbuybutton(self, interaction: discord.Interaction, Button: discord.ui.Button):

        em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**", description=f"{interaction.user.mention} here is the offer:\n \n- :{chicken.Type}: *{chicken.Name}* - **{chicken.Price}$**\n- :{duck.Type}: *{duck.Name}* - **{duck.Price}$**\n- :{pig.Type}: *{pig.Name}* - **{pig.Price}$**\n- :{rabbit.Type}: *{rabbit.Name}* - **{rabbit.Price}$**\n- :{dog.Type}: *{dog.Name}* - **{dog.Price}$**\n- :{cat.Type}: *{cat.Name}* - **{cat.Price}$**\n- :{horse.Type}: *{horse.Name}* - **{horse.Price}$**\n- :{wolf.Type}: *{wolf.Name}* - **{wolf.Price}$**\n- :{octopus.Type}: *{octopus.Name}* - **{octopus.Price}$**\n- :{eagle.Type}: *{eagle.Name}* - **{eagle.Price}$**\n- :{snake.Type}: *{snake.Name}* - **{snake.Price}$**\n- :{shark.Type}: *{shark.Name}* - **{shark.Price}$**\n- :{bear.Type}: *{bear.Name}* - **{bear.Price}$**\n- :{lion.Type}: *{lion.Name}* - **{lion.Price}$**\n- :{mini_dragon.Type}: *{mini_dragon.Name}* - **{mini_dragon.Price}$**\n- :{unicorn.Type}: *{unicorn.Name}* - **{unicorn.Price}$**\n \nYour balance: **{player.Money}$**", color=15277667)
        await interaction.response.edit_message(embed= em)

    @discord.ui.button(label= "Potions", style=discord.ButtonStyle.green)
    async def potionbuybutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        em = discord.Embed(title= "**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description = f"{interaction.user.mention} here is the offer:\n- :dog: *Dog* - **300$**\n- :cat: *Cat* - **300$**\nYour balance: **{player.Money}$**", color = 15277667)
        await interaction.response.edit_message(embed= em)

    @discord.ui.button(label= "Titles", style=discord.ButtonStyle.green)
    async def titlebuybutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        em = discord.Embed(title= "**:shopping_cart: CHARMING SHOP - Titles :identification_card:**", description = f"{interaction.user.mention} here is the offer:\n- :dog: *Dog* - **300$**\n- :cat: *Cat* - **300$**\nYour balance: **{player.Money}$**", color = 15277667)
        await interaction.response.edit_message(embed= em)

# PULL
# @client.tree.command(name= "pull", description= "Pulls an artifact for 1500$.")
# async def pull(interaction: discord.Interaction):
#     quality = random.choice(artifacts_quality)
#     artifact = random.choice(artifacts)
#     em = discord.Embed(title= "Pulled Artifact", description= f"You have pulled *{quality} {artifact}*.", color= discord.Color.pink())
#     await interaction.response.send_message(embed= em)

@client.tree.command(name= "shop", description= "CHARMING SHOP.")
async def actionmenu(interaction: discord.Interaction):
    em = discord.Embed(title= ":shopping_cart: Welcome to *the* **CHARMING SHOP**:sparkles:", description= f"{interaction.user.mention}, what are you looking for?", color = vividpink)
    await interaction.response.send_message(embed= em, view= ShopMenu())

# PETMENU
class PetMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label= "Change name", style=discord.ButtonStyle.blurple)
    async def namebutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        class NameButtonMenu(discord.ui.View):
            def __init__(self):
                super().__init__(timeout = None)

            @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
            async def confirmbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                if pet.Name == "no pet":
                    em = discord.Embed(title= "Pet name change", description= f"{interaction.user.mention}, you cannot change a name of an non-existend pet. Buy one in **:shopping_cart: CHARMING SHOP :sparkles:**", color= 15548997)
                    await interaction.response.edit_message(embed= em, view=None)
                else:
                    em = discord.Embed(title= "Pet name change", description= f"{interaction.user.mention}, type a name which you want your pet to be called. Answer within 60 seconds.", color= 15844367)
                    await interaction.response.edit_message(embed= em, view=None)
                    def check_message(m):
                        return m.author == interaction.user and m.channel == interaction.channel
                    try:
                        msg = await client.wait_for("message", check=check_message, timeout=60.0)
                        pet.Name = msg.content
                        em = discord.Embed(title="Pet name changed!", description=f"{interaction.user.mention}'s pet is now named **:{pet.Type}: {pet.Name}**.", color= 15844367)
                        await interaction.followup.send(embed= em)
                    except asyncio.TimeoutError:
                        await interaction.followup.send(discord.Embed(title= "Pet name change", description= f"{interaction.user.mention} took too long to respond!", color= 15844367), ephemeral=True)

            @discord.ui.button(label= "Cancel", style=discord.ButtonStyle.red)
            async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title= "Pet name change", description= f"Pet name change successfuly cancelled. :{pet.Type}: {pet.Name} will keep its original name.", color=15548997)
                await interaction.response.edit_message(embed=em, view=None)

        em = discord.Embed(title= "Pet name change :grey_question:", description= f"{interaction.user.mention}, are you sure you want to change your pet's name?*", color= 15844367)
        await interaction.response.edit_message(embed= em, view=NameButtonMenu())

    @discord.ui.button(label= "Play", style=discord.ButtonStyle.blurple)
    async def playbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        earned_happiness = random.randint(5, 9)
        if pet.Happiness == 100:
            em = discord.Embed(title="Full of happiness", description=f"**:{pet.Type}: {pet.Name}** does not want to play right now. Play with it later.", color=yellow)
        else:
            if (pet.Happiness + earned_happiness) >= 100:
                pet.Happiness = 100
                em = discord.Embed(title="Happiness increased", description=f"You played with **:{pet.Type}: {pet.Name}** and it had so much fun.\n*Happiness:* **+ {earned_happiness}**", color=yellow)
            elif pet.Name == "no pet":
                pet.Happiness = 0
                em = discord.Embed(title="No pet :()", description=f"{interaction.user.mention}, you can't play with a pet because you don't have one. Purchase one in **:shopping_cart: CHARMING SHOP :sparkles:**", color=red)
            else:
                pet.Happiness = pet.Happiness + earned_happiness
                em = discord.Embed(title="Happiness increased", description=f"You played with **:{pet.Type}: {pet.Name}** and it had so much fun.\n*Happiness:* **+ {earned_happiness}**", color=yellow)
        await interaction.response.edit_message(embed= em)

    @discord.ui.button(label= "Feed", style=discord.ButtonStyle.blurple)
    async def feedbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        earned_happiness = random.randint(15, 20)
        if pet.Happiness == 100:
            em = discord.Embed(title="Full of happiness", description=f"**:{pet.Type}: {pet.Name}** is not hungry. Feed it later.", color= yellow)
        else:
            if (pet.Happiness + earned_happiness) >= 100:
                pet.Happiness = 100
                em = discord.Embed(title="Happiness increased", description=f"You fed **:{pet.Type}: {pet.Name}** and it was extremely happy.\n*Happiness:* **+ {earned_happiness}**", color= yellow)
            elif pet.Name == "no pet":
                pet.Happiness = 0
                em = discord.Embed(title="No pet :()", description=f"{interaction.user.mention}, you don't have any pet to be fed. Purchase one in **:shopping_cart: CHARMING SHOP :sparkles:**", color= red)
            else:
                pet.Happiness = pet.Happiness + earned_happiness
                em = discord.Embed(title="Happiness increased", description=f"You fed **:{pet.Type}: {pet.Name}** and it was extremely happy.\n*Happiness:* **+ {earned_happiness}**", color= yellow)
        await interaction.response.edit_message(embed= em)

    @discord.ui.button(label= "Pet info", style=discord.ButtonStyle.gray)
    async def petbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        if pet.Type == "no pet":
            pet_name = f"{pet.Type}"
        else:
            pet_name = f":{pet.Type}: {pet.Name}"
        em = discord.Embed(title= "Pet info", description= f"**{interaction.user.mention}'s companion**\n \nName: **{pet_name}**\nHappiness: **{pet.Happiness} / 100**", color = 15844367)
        await interaction.response.edit_message(embed= em)

@client.tree.command(name= "petmenu", description= "Menu to check up on your sweet pet.")
async def petmenu(interaction: discord.Interaction):
    if pet.Type == "-":
        pet_type = f"{pet.Type}"
    else:
        pet_type = f":{pet.Type}: {pet.Name}"
    em = discord.Embed(title= "Pet info", description= f"**{interaction.user.mention}'s companion**\n \nName: **{pet_type}**\nHappiness: **{pet.Happiness} / 100**", color = yellow)
    await interaction.response.send_message(embed= em, view= PetMenu())

client.run(DISCORD_TOKEN)