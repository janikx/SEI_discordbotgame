# WHAT TO DO:
# • commands z papiera
# • znamka: 1) ZA KOD 2) DOKUMENTACIA / PREZENTACIA - aku kniznicu sme pouzili, ako sme postupovali, skadial je co, co to robi, atd.

# spravim class USER, potom spravim tam atributy, potom artefakt atributy, potom vytvorim USERA a jeho full atk (scitanie) atd., potom if artifact quality = gold atd. tak podla toho priradim artifact atk bonus atd.
# equip artefaktu = vymazat list a potom dosadit novy artefakt

# COLORS
red = 15548997
darkgreen = 1146986
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
    BonusMoneyCount: int
    BonusXPCount: int

    def __init__(self, hp, maxhp, res, money, lvl, xp, xptolvlup, registered, title, bonusmoney, bonusxp, bonusmcount, bxpcount):
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
        self.BonusMoneyCount = bonusmcount
        self.BonusXPCount = bxpcount

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
player = User(30, 30, 10, 620, 1, 0, 50, True, "no title", 1.5, 1, 0, 0)
pet = Pet("Cat", "cat", 550, 100)

# START
@client.tree.command(name="start", description="Use START to play the game.")
async def start(interaction: discord.Interaction):
    em = discord.Embed(title= "Welcome to Charming RPG!", description= "Your adventure starts now. You can use /commands for a list of commands. Have fun!", color= pink, timestamp=datetime.datetime.utcnow())
    em.set_thumbnail(url= interaction.user.avatar)
    player.registered = True
    joined_the_game_time = datetime.datetime.utcnow()
    await interaction.response.send_message(embed= em)
    return joined_the_game_time

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

def FormatTime(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours}h {minutes}m {seconds}s"

# LEVEL UP FUNC
def LevelUpChecker():
    if player.XP >= player.LvlUpXP:
        lvl_up = True
        player.XP = (player.XP - player.LvlUpXP)
        player.Lvl += 1
        player.MaxHP += 2
        player.HP = player.MaxHP

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
    return player.XP, player.LvlUpXP, player.Lvl, player.Money, lvl_up, player.MaxHP, player.HP

@client.event
async def on_ready():
    print(f"Bot has connected as {client.user.name} :)")
    await client.tree.sync()

# HELP
@client.tree.command(name= "commands", description="Shows a list of all avaiable COMMANDS.")
async def commands(interaction: discord.Interaction):
    em= discord.Embed(title= "Charming RPG - Commands", description= f"{interaction.user.mention} here's the list of commands!", color= pink)
    em.add_field(name="Info :mag:", value="/userinfo /inventory - use, sell", inline=False)
    em.add_field(name="Action :pick:", value="/action - chop, mine, hunt", inline=False)
    em.add_field(name="Shop :shopping_cart:", value="/shop - pets, potions, titles", inline=False)
    em.add_field(name="Help :helmet_with_cross:", value="/commands /start", inline=False)
    await interaction.response.send_message(embed= em, ephemeral= True)

# LIST OF NEEDED VARIABLES
# MINE
mine_materials = ["<:rrock:1245417668534599790> rock", "<:diorite:1245418611099828224> diorite", "<:dirt:1245417662184689726> dirt", "<:iron:1245417676382404649> iron", "<:coal:1245417659512782970> coal", "<:copper:1245417677971918943> copper", "<:granite:1245419034128810005> granite", "<:chalk:1245417670136823848> chalk"]
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

# INVENTORY
inventory_items = []
inventory_mineitems = []
inventory_chopitems = []

class InventoryMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label= "Refresh inventory", style=discord.ButtonStyle.green)
    async def invrefresh(self, interaction: discord.Interaction, Button: discord.ui.Button):
        if len(inventory_items) == 0 and len(inventory_mineitems) == 0 and len(inventory_chopitems) == 0:
            em = discord.Embed(title= "Your inventory", description= f"No items.\n\nYour balance: **{player.Money}$**", color = darkgreen)
            await interaction.response.edit_message(embed= em)
        else:
            counter_items = Counter(inventory_items)
            inventory_items_dict = dict(counter_items)

            counter_mineitems = Counter(inventory_mineitems)
            mine_items_dict = dict(counter_mineitems)

            counter_chopitems = Counter(inventory_chopitems)
            chop_items_dict = dict(counter_chopitems)

            em = discord.Embed(title= "Your inventory", description= f"\n{interaction.user.mention}'s balance: **{player.Money}$**", color = darkgreen)
            em.add_field(name= "Items :backpack:", value= "\n".join([f"{count}x {item}" for item, count in counter_items.items()]), inline= False)
            em.add_field(name= "Mined Items :pick:", value= "\n".join([f"{count}x {item}" for item, count in counter_mineitems.items()]), inline= False)
            em.add_field(name= "Chopped Items :axe:", value= "\n".join([f"{count}x {item}" for item, count in counter_chopitems.items()]), inline= False)
            await interaction.response.edit_message(embed= em)

    @discord.ui.button(label= "Use", style=discord.ButtonStyle.green)
    async def invuse(self, interaction: discord.Interaction, Button: discord.ui.Button):
        class InvUseButtonMenu(discord.ui.View):
            def __init__(self):
                super().__init__(timeout = None)

            @discord.ui.button(label= "Cancel", style=discord.ButtonStyle.red)
            async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title= "Your Inventory - Usable", description= f"{interaction.user.mention} didn't want to use anything.", color= red)
                await interaction.response.edit_message(embed=em, view=None)
        
        counter_items = Counter(inventory_items)
        inventory_items_dict = dict(counter_items)
        em = discord.Embed(title= "Your Inventory - Usable", description= f"{interaction.user.mention}, which item do you want to use?\n" + "\n".join([f"{count}x {item}" for item, count in counter_items.items()]) + "\n\nTo use an item, ***itemname*** in chat", color= darkgreen)
        await interaction.response.edit_message(embed= em, view=InvUseButtonMenu())

        def check_message(m):
            return m.author == interaction.user and m.channel == interaction.channel
        used_item = "none"
        while used_item not in ["healing", "healing potion", "heal potion", "healpotion", "heal", "bonusgold", "bonus gold", "bonus gold potion", "bonusgold potion", "bonusgoldpotion", "goldpotion", "gold potion", "bonusxp", "bonus xp", "bonus xp potion", "bonusxp potion", "bonusxppotion", "xppotion", "xp potion"]:
            try:
                msg = await client.wait_for("message", check=check_message, timeout= 60.0)
                used_item = msg.content
                if used_item in ["healing", "healing potion", "heal potion", "healpotion", "heal"]:
                    if "<:healpotion:1245417680903733249> healing potion" in inventory_items:
                        player.HP = player.MaxHP
                        em = discord.Embed(title="Your Inventory - Usable", description=f"{interaction.user.mention} used a **<:healpotion:1245417680903733249> healing potion** and their HP is full *({player.HP} HP)*.", color= darkgreen)
                        inventory_items.remove("<:healpotion:1245417680903733249> healing potion")
                        await interaction.followup.send(embed= em)
                    else:
                        em = discord.Embed(title="Your Inventory - Usable", description=f"{interaction.user.mention}, you don't have a **<:healpotion:1245417680903733249> healing potion** in your inventory.", color= darkgreen)
                        await interaction.followup.send(embed= em)
                elif used_item in ["bonusgold", "bonus gold", "bonus gold potion", "bonusgold potion", "bonusgoldpotion", "goldpotion", "gold potion"]:
                    if "<:goldpotion:1245417684661702730> bonus gold potion" in inventory_items:
                        player.BonusMoneyCount = 30
                        player.BonusMoney = 1.5
                        em = discord.Embed(title="Your Inventory - Usable", description=f"{interaction.user.mention} used a **<:goldpotion:1245417684661702730> bonus gold potion** and their Money gain is boosted for *30x*.", color= darkgreen)
                        inventory_items.remove("<:goldpotion:1245417684661702730> bonus gold potion")
                        await interaction.followup.send(embed= em)
                    else:
                        em = discord.Embed(title="Your Inventory - Usable", description=f"{interaction.user.mention}, you don't have a **<:goldpotion:1245417684661702730> bonus gold potion** in your inventory.", color= darkgreen)
                        await interaction.followup.send(embed= em)
                elif used_item in ["bonusxp", "bonus xp", "bonus xp potion", "bonusxp potion", "bonusxppotion", "xppotion", "xp potion"]:
                    if "<:xppotion:1245417682199646290> bonus xp potion" in inventory_items:
                        player.BonusXPCount = 30
                        player.BonusXP = 1.5
                        em = discord.Embed(title="Your Inventory - Usable", description=f"{interaction.user.mention} used a **<:xppotion:1245417682199646290> bonus xp potion** and their XP gain is boosted for *30x*.", color= darkgreen)
                        inventory_items.remove("<:xppotion:1245417682199646290> bonus xp potion")
                        await interaction.followup.send(embed= em)
                    else:
                        em = discord.Embed(title="Your Inventory - Usable", description=f"{interaction.user.mention}, you don't have a **<:xppotion:1245417682199646290> bonus xp potion** in your inventory.", color= darkgreen)
                        await interaction.followup.send(embed= em)
                else:
                    em = discord.Embed(title="Your Inventory - Usable", description=f"{interaction.user.mention}, that item is not in your inventory.", color= darkgreen)
                    await interaction.followup.send(embed= em)
            except asyncio.TimeoutError:
                pass

    @discord.ui.button(label= "Sell", style=discord.ButtonStyle.blurple)
    async def invsell(self, interaction: discord.Interaction, Button: discord.ui.Button):
        class InvSellButtonMenu(discord.ui.View):
            def __init__(self):
                super().__init__(timeout = None)

            @discord.ui.button(label= "Confirm", style=discord.ButtonStyle.green)
            async def confirmbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                global inventory_chopitems, inventory_mineitems, player
                rarechop = inventory_chopitems.count(":apple: magic apple")
                raremine = inventory_mineitems.count(":gem: diamond")
                numofitems = int((len(inventory_chopitems)) + (len(inventory_mineitems)))
                totalmoney = int((((len(inventory_mineitems) - raremine) * 30) + (raremine * 55)) + (((len(inventory_chopitems) - rarechop) * 25) + (rarechop * 50)))
                
                inventory_chopitems.clear()
                inventory_mineitems.clear()
                player.Money += int(totalmoney * player.BonusMoney)
                if player.BonusMoneyCount == 0:
                    player.BonusMoney = 1
                else:
                    player.BonusMoneyCount -= 1
                
                em = discord.Embed(title= "Your Inventory - Sell", description= f"{interaction.user.mention} sold *{numofitems}* collected items and got **{totalmoney}$**", color= green)
                await interaction.response.edit_message(embed=em, view=None)

            @discord.ui.button(label= "Cancel", style=discord.ButtonStyle.red)
            async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title= "Your Inventory - Sell", description= f"{interaction.user.mention} didn't want to sell anything.", color= red)
                await interaction.response.edit_message(embed=em, view=None)

        counter_mineitems = Counter(inventory_mineitems)
        mine_items_dict = dict(counter_mineitems)

        counter_chopitems = Counter(inventory_chopitems)
        chop_items_dict = dict(counter_chopitems)

        em = discord.Embed(title= "Your Inventory - Sell", description= f"{interaction.user.mention}, do you want to sell these items?\n", color= darkgreen)
        em.add_field(name= "Mined Items :pick:", value= "\n".join([f"{count}x {item}" for item, count in counter_mineitems.items()]), inline= False)
        em.add_field(name= "Chopped Items :axe:", value= "\n".join([f"{count}x {item}" for item, count in counter_chopitems.items()]), inline= False)
        await interaction.response.edit_message(embed= em, view=InvSellButtonMenu())

@client.tree.command(name= "inventory", description= "Shows inventory of a player.")
async def inventory(interaction: discord.Interaction):
    if len(inventory_items) == 0 and len(inventory_mineitems) == 0 and len(inventory_chopitems) == 0:
        em = discord.Embed(title= "Your inventory", description= f"No items.\n\nYour balance: **{player.Money}$**", color = darkgreen)
    else:
        counter_items = Counter(inventory_items)
        inventory_items_dict = dict(counter_items)

        counter_mineitems = Counter(inventory_mineitems)
        mine_items_dict = dict(counter_mineitems)

        counter_chopitems = Counter(inventory_chopitems)
        chop_items_dict = dict(counter_chopitems)

        em = discord.Embed(title= "Your inventory", description= f"\n{interaction.user.mention}'s balance: **{player.Money}$**", color = darkgreen)
        em.add_field(name= "Items :backpack:", value= "\n".join([f"{count}x {item}" for item, count in counter_items.items()]), inline= False)
        em.add_field(name= "Mined Items :pick:", value= "\n".join([f"{count}x {item}" for item, count in counter_mineitems.items()]), inline= False)
        em.add_field(name= "Chopped Items :axe:", value= "\n".join([f"{count}x {item}" for item, count in counter_chopitems.items()]), inline= False)
    await interaction.response.send_message(embed= em, view= InventoryMenu())

# USERINFO
@client.tree.command(name="userinfo", description="Shows information about any user.")
async def userinfo(interaction: discord.Interaction, member: discord.Member= None):
    if member == None:
        member = interaction.user
    em = discord.Embed(title= "User Info", description= f":bust_in_silhouette: Here is the user info for user {member.name}", color= discord.Color.pink(), timestamp= datetime.datetime.utcnow())
    em.set_thumbnail(url= member.avatar)
    em.add_field(name= "Info :mag:", value= f"- Name: **{member.mention}**\n- Title: **{player.Title}**\nID: *{member.id}*", inline= False)
    em.add_field(name= "Game status :video_game:", value= f":hearts: HP: **{player.HP}/{player.MaxHP}**\n:money_with_wings: Balance: **{player.Money}$**\n:chart_with_upwards_trend: Level: **{player.Lvl}**\nXP: **{player.XP} / {player.LvlUpXP} xp**")
    if pet.Type == "-":
        pet_type = f"{pet.Type}"
    else:
        pet_type = f":{pet.Type}: {pet.Type}"
    em.add_field(name= "Pet :paw_prints:", value= f"Name: **{pet.Name}**\nType: *{pet_type}*\nHappiness: *{pet.Happiness} / 100*")
    await interaction.response.send_message(embed= em)

# DAILY n' WEEKLY
@client.tree.command(name="daily", description="Claim a reward every 24h.")
@app_commands.checks.cooldown(1, 86400)
async def daily(interaction: discord.Interaction):
    player.Money += 100
    em = discord.Embed(title= "Daily reward :money_with_wings:", description= f"{interaction.user.mention} claimed their daily **100$**!", color = purple)
    await interaction.response.send_message(embed= em)

@daily.error
async def actionmenu_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    retry_after = FormatTime(error.retry_after)
    em = discord.Embed(title= "Daily reward :money_with_wings:", description= f"{interaction.user.mention}, you have already *claimed* your daily reward! Return after **{retry_after}**.", color = red)
    await interaction.response.send_message(embed= em)

@client.tree.command(name="weekly", description="Claim a reward every-week.")
@app_commands.checks.cooldown(1, 604800)
async def weekly(interaction: discord.Interaction):
    player.Money += 1000
    em = discord.Embed(title= "Weekly reward :money_with_wings:", description= f"{interaction.user.mention} claimed their weekly **1000$**!", color = purple)
    await interaction.response.send_message(embed= em)

@weekly.error
async def actionmenu_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    retry_after = FormatTime(error.retry_after)
    em = discord.Embed(title= "Weekly reward :money_with_wings:", description= f"{interaction.user.mention}, you have already *claimed* your weekly reward! Return after **{retry_after}**.", color = red)
    await interaction.response.send_message(embed= em)

# SHUTDOWN
@client.tree.command(name="shutdown", description="Shuts down the bot.")
async def shutdown(interaction: discord.Interaction):
    ListOfAdmins = [532640698114113556]
    if interaction.user.id in ListOfAdmins:# (my ID, no one except me can use this)
        await interaction.response.send_message(content= f"*The **{client.user.name}** shutted down successfully.*", ephemeral= True)
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

            if pet.Happiness <= 0:
                pet.Happiness = 0
            else:
                happiness_lower = [0, 10, 12, 14]
                chances_happiness_lower = [0.6, 0.2, 0.15, 0.05]
                pet.Happiness = int(pet.Happiness - ((random.choices(happiness_lower, chances_happiness_lower)[0])))

            player.Money = player.Money + earned_money
            player.XP = player.XP + earned_xp

            if player.BonusXPCount == 0:
                player.BonusXP = 1
            else:
                player.BonusXPCount -= 1
            if player.BonusMoneyCount == 0:
                player.BonusMoney = 1
            else:
                player.BonusMoneyCount -= 1

            lvl_up_checker = LevelUpChecker()
            player.XP = lvl_up_checker[0]
            player.LvlUpXP = lvl_up_checker[1]
            player.Lvl = lvl_up_checker[2]
            player.Money = lvl_up_checker[3]
            lvl_up = lvl_up_checker[4]
            player.MaxHP = lvl_up_checker[5]
            player.HP = lvl_up_checker[6]

            em = random.choices(chop_luck, chances_mine)[0]
            if lvl_up == True:
                await interaction.response.edit_message(embed= discord.Embed(title= ":axe: Chopping...", description = em + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*\n \n**Oh.. You're now level {player.Lvl}! :chart_with_upwards_trend:**", color= 3426654))
            else:
                await interaction.response.edit_message(embed= discord.Embed(title= ":axe: Chopping...", description = em + f"\n \n*Balance:* **+ {earned_money}$**" + f"\n*+ {earned_xp} xp*", color= 3426654))

            if em == f"{interaction.user.mention} choped trees until they found **{choprare}** with their scratched hands!":
                inventory_chopitems.append(choprare)
            if em == f"{interaction.user.mention} choped down the trees and gained **{chop1}.**":
                inventory_chopitems.append(chop1)
            if em == f"{interaction.user.mention} choped different trees and returned with **{chop1}** and **{chop2}**.":
                inventory_chopitems.append(chop1)
                inventory_chopitems.append(chop2)

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
            chances_mine = [0.05, 0.65, 0.3]

            if pet.Happiness <= 0:
                pet.Happiness = 0
            else:
                happiness_lower = [0, 10, 12, 14]
                chances_happiness_lower = [0.6, 0.2, 0.15, 0.05]
                pet.Happiness = int(pet.Happiness - ((random.choices(happiness_lower, chances_happiness_lower)[0])))

            player.Money = player.Money + earned_money
            player.XP = player.XP + earned_xp

            if player.BonusXPCount == 0:
                player.BonusXP = 1
            else:
                player.BonusXPCount -= 1
            if player.BonusMoneyCount == 0:
                player.BonusMoney = 1
            else:
                player.BonusMoneyCount -= 1

            lvl_up_checker = LevelUpChecker()
            player.XP = lvl_up_checker[0]
            player.LvlUpXP = lvl_up_checker[1]
            player.Lvl = lvl_up_checker[2]
            player.Money = lvl_up_checker[3]
            lvl_up = lvl_up_checker[4]
            player.MaxHP = lvl_up_checker[5]
            player.HP = lvl_up_checker[6]

            em = random.choices(mine_luck, chances_mine)[0]
            if lvl_up == True:
                await interaction.response.edit_message(embed= discord.Embed(title= ":pick: Mining...", description= em + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*\n \n**Oh.. You're now level {player.Lvl}! :chart_with_upwards_trend:**", color = 3426654))
            else:
                await interaction.response.edit_message(embed= discord.Embed(title= ":pick: Mining...", description= em + f"\n \n*Balance:* **+ {earned_money}$**\n*+ {earned_xp} xp*", color = 3426654))

            if em == f"{interaction.user.mention} mined in a cave for so long and found a **{minerare}**!":
                inventory_mineitems.append(minerare)
            if em == f"{interaction.user.mention} mined in a cave for a while and found **{mine1}.**":
                inventory_mineitems.append(mine1)
            if em == f"{interaction.user.mention} mined in a cave for few minutes and returned with **{mine1}** and **{mine2}**.":
                inventory_mineitems.append(mine1)
                inventory_mineitems.append(mine2)

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

            if pet.Happiness <= 0:
                pet.Happiness = 0
            else:
                happiness_lower = [1, 2, 3, 4, 5]
                chances_happiness_lower = [0.2, 0.3, 0.3, 0.1, 0.1]
                pet.Happiness = int(pet.Happiness - ((random.choices(happiness_lower, chances_happiness_lower)[0])))

            if player.BonusXPCount == 0:
                player.BonusXP = 1
            else:
                player.BonusXPCount -= 1
            if player.BonusMoneyCount == 0:
                player.BonusMoney = 1
            else:
                player.BonusMoneyCount -= 1

            lvl_up_checker = LevelUpChecker()
            player.XP = lvl_up_checker[0]
            player.LvlUpXP = lvl_up_checker[1]
            player.Lvl = lvl_up_checker[2]
            player.Money = lvl_up_checker[3]
            lvl_up = lvl_up_checker[4]
            player.MaxHP = lvl_up_checker[5]
            player.HP = lvl_up_checker[6]

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

    @discord.ui.button(label= "Quick heal", style= discord.ButtonStyle.green)
    async def quickhealbutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        if "<:healpotion:1245417680903733249> healing potion" not in inventory_items:
            em = discord.Embed(title="<:healpotion:1245417680903733249> Quick heal", description=f"{interaction.user.mention}, you don't have a **<:healpotion:1245417680903733249> healing potion** in your inventory.", color= pink)
            await interaction.response.edit_message(embed= em)
        else:
            player.HP = player.MaxHP
            em = discord.Embed(title="<:healpotion:1245417680903733249> Quick heal", description=f"{interaction.user.mention} used a **<:healpotion:1245417680903733249> healing potion** and their HP is full *({player.HP} HP)*.", color= pink)
            inventory_items.remove("<:healpotion:1245417680903733249> healing potion")
            await interaction.response.edit_message(embed= em)

@client.tree.command(name= "action", description= "Menu to do perform an ACTION")
async def actionmenu(interaction: discord.Interaction):
    em = discord.Embed(title= "Action", description= f"{interaction.user.mention}, what action do you want to make?", color = darkaqua)
    await interaction.response.send_message(embed= em, view= ActionMenu())

@app_commands.checks.cooldown(1, 5.0)
@actionmenu.error
async def actionmenu_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    retry_after = FormatTime(error.retry_after)
    em = discord.Embed(title= "Action", description= f"{interaction.user.mention}, you cannot use this command right now. Try again in {retry_after}", color = red)
    await interaction.response.edit_message(embed= em, ephemeral= True)

# SHOPMENU - titles, pets, potions(healing, bonus gold, bonus xp, bonus atk when boss fight)
class ShopMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label= "Pets", style=discord.ButtonStyle.blurple)
    async def petbuybutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        em = discord.Embed(
    title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**",
    description=(
        f"{interaction.user.mention} here is the offer:\n\n"
        f"- :{chicken.Type}: *{chicken.Name}* - **{chicken.Price}$**\n"
        f"- :{duck.Type}: *{duck.Name}* - **{duck.Price}$**\n"
        f"- :{pig.Type}: *{pig.Name}* - **{pig.Price}$**\n"
        f"- :{rabbit.Type}: *{rabbit.Name}* - **{rabbit.Price}$**\n"
        f"- :{dog.Type}: *{dog.Name}* - **{dog.Price}$**\n"
        f"- :{cat.Type}: *{cat.Name}* - **{cat.Price}$**\n"
        f"- :{horse.Type}: *{horse.Name}* - **{horse.Price}$**\n"
        f"- :{wolf.Type}: *{wolf.Name}* - **{wolf.Price}$**\n"
        f"- :{octopus.Type}: *{octopus.Name}* - **{octopus.Price}$**\n"
        f"- :{eagle.Type}: *{eagle.Name}* - **{eagle.Price}$**\n"
        f"- :{snake.Type}: *{snake.Name}* - **{snake.Price}$**\n"
        f"- :{shark.Type}: *{shark.Name}* - **{shark.Price}$**\n"
        f"- :{bear.Type}: *{bear.Name}* - **{bear.Price}$**\n"
        f"- :{lion.Type}: *{lion.Name}* - **{lion.Price}$**\n"
        f"- :{mini_dragon.Type}: *{mini_dragon.Name}* - **{mini_dragon.Price}$**\n"
        f"- :{unicorn.Type}: *{unicorn.Name}* - **{unicorn.Price}$**\n\n"
        f"Your balance: **{player.Money}$**\n"
        ":warning: To buy a pet, type ***buy petname*** in chat\n"
        ":warning: If you buy a pet your current pet will be automatically released to the wild"
    ),
    color=vividpink
)

        await interaction.response.edit_message(embed= em)

        def check_message(m):
            return m.author == interaction.user and m.channel == interaction.channel
        try:
            msg = await client.wait_for("message", check=check_message, timeout= None)
            petbuymsg = msg.content.lower()
            global pet
            if petbuymsg in ["buy chicken", "buy chick"]:
                pet = chicken
            elif petbuymsg == "buy duck":
                pet = duck
            elif petbuymsg == "buy pig":
                pet = pig
            elif petbuymsg in ["buy rabbit", "buy bunny"]:
                pet = rabbit
            elif petbuymsg in ["buy dog", "buy doggy", "buy puppy"]:
                pet = dog
            elif petbuymsg in ["buy cat", "buy kitty", "buy kitten"]:
                pet = cat
            elif petbuymsg in ["buy horse", "buy pony"]:
                pet = horse
            elif petbuymsg == "buy wolf":
                pet = wolf
            elif petbuymsg == "buy octopus":
                pet = octopus
            elif petbuymsg == "buy eagle":
                pet = eagle
            elif petbuymsg == "buy snake":
                pet = snake
            elif petbuymsg == "buy shark":
                pet = shark
            elif petbuymsg == "buy bear":
                pet = bear
            elif petbuymsg == "buy lion":
                pet = lion
            elif petbuymsg in ["buy dragon", "buy mini dragon"]:
                pet = mini_dragon
            elif petbuymsg == "buy unicorn":
                pet = unicorn
            else:
                await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**", description= "Invalid pet. Please try again.", color= red))
                return
            
            if pet:
                class PetShopMenu(discord.ui.View):
                    def __init__(self):
                        super().__init__(timeout = None)

                    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
                    async def confirmbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                        global pet, player
                        if player.Money < pet.Price:
                            moneyshort = int(pet.Price - player.Money)
                            em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**", description=f"{interaction.user.mention}, you don't have enough money for **:{pet.Type}: {pet.Name}** :(\n \nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color= red)
                            await interaction.response.edit_message(embed= em, view=None)
                        else:
                            player.Money = int(player.Money - pet.Price)
                            em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**", description=f"{interaction.user.mention} bought their *cutie*, **:{pet.Type}: {pet.Name}.**\n \nYour balance: **{player.Money}$**\n*— {pet.Price}$*", color= green)
                            await interaction.response.edit_message(embed= em, view=None)

                    @discord.ui.button(label= "Cancel", style=discord.ButtonStyle.red)
                    async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                        em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**", description= f"{interaction.user.mention} did not buy a pet.", color= vividpink)
                        await interaction.response.edit_message(embed=em, view=None)

                em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**", description= f"{interaction.user.mention}, are you sure you want to buy **:{pet.Type}: {pet.Name}**?", color= vividpink)
                await interaction.followup.send(embed= em, view=PetShopMenu())

        except asyncio.TimeoutError:
            await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Pets :paw_prints:**", description= f"{interaction.user.mention} did not want to buy anything.", color= vividpink), ephemeral=True)

    @discord.ui.button(label= "Potions", style=discord.ButtonStyle.blurple)
    async def potionbuybutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        em = discord.Embed(
    title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**",
    description=(
        f"{interaction.user.mention} here is the offer:\n\n"
        "- <:healpotion:1245417680903733249> *healing potion* - **5$**\n"
        "- <:healpotion:1245417680903733249> *healing potion* 10x - **40$**\n"
        "*(max-outs your HP)*\n\n"
        "- <:xppotion:1245417682199646290> *bonus xp potion* - **80$**\n"
        "- <:xppotion:1245417682199646290> *bonus xp potion* 10x - **675$**\n"
        "*(gives you 30 times bonus XP)*\n\n"
        "- <:goldpotion:1245417684661702730> *bonus gold potion* - **80$**\n"
        "- <:goldpotion:1245417684661702730> *bonus gold potion* 10x - **675$**\n"
        "*(gives you 30 times bonus Money)*\n\n"
        f"Your balance: **{player.Money}$**\n"
        ":warning: To buy a potion, type ***buy potionname*** in chat"
    ),
    color=vividpink
)
        await interaction.response.edit_message(embed= em)

        potionbuymsg = "none"
        while potionbuymsg not in ["buy healing", "buy healing potion", "buy heal potion", "buy healing 10", "buy healing potion 10", "buy heal potion 10", "buy healpotion 10", "buy healingpotion 10", "buy xp", "buy xp potion", "buy xppotion", "buy bonus xp", "buy bonusxp", "buy bonus xp potion", "buy bonusxppotion", "buy xp 10", "buy xp potion 10", "buy xppotion 10", "buy bonus xp 10", "buy bonusxp 10", "buy bonus xp potion 10", "buy bonusxppotion 10", "buy bonusgold", "buy bonus gold potion", "buy gold potion", "buy bonusgoldpotion", "buy bonusgold potion", "buy bonusgold 10", "buy bonus gold potion 10", "buy gold potion 10", "buy bonusgold potion 10", "buy bonusgoldpotion 10", "buy healing 10x", "buy healing potion 10x", "buy heal potion 10x", "buy healpotion 10x", "buy healingpotion 10x", "buy xp 10x", "buy xp potion 10x", "buy xppotion 10x", "buy bonus xp 10x", "buy bonusxp 10x", "buy bonus xp potion 10x", "buy bonusxppotion 10x", "buy bonusgold 10x", "buy bonus gold potion 10x", "buy gold potion 10x", "buy bonusgold potion 10x", "buy bonusgoldpotion 10x"]:
            def check_message(m):
                return m.author == interaction.user and m.channel == interaction.channel
            try:
                msg = await client.wait_for("message", check=check_message, timeout= None)
                potionbuymsg = msg.content.lower()
                global inventory_items
                if potionbuymsg in ["buy healing", "buy healing potion", "buy heal potion"]:
                    potion = "<:healpotion:1245417680903733249> healing potion"
                elif potionbuymsg in ["buy healing 10", "buy healing potion 10", "buy heal potion 10", "buy healpotion 10", "buy healingpotion 10", "buy healing 10x", "buy healing potion 10x", "buy heal potion 10x", "buy healpotion 10x", "buy healingpotion 10x"]:
                    potion = "<:healpotion:1245417680903733249> healing potion 10"
                elif potionbuymsg in ["buy xp", "buy xp potion", "buy xppotion", "buy bonus xp", "buy bonusxp", "buy bonus xp potion", "buy bonusxppotion"]:
                    potion = "<:xppotion:1245417682199646290> bonus xp potion"
                elif potionbuymsg in ["buy xp 10", "buy xp potion 10", "buy xppotion 10", "buy bonus xp 10", "buy bonusxp 10", "buy bonus xp potion 10", "buy bonusxppotion 10", "buy xp 10x", "buy xp potion 10x", "buy xppotion 10x", "buy bonus xp 10x", "buy bonusxp 10x", "buy bonus xp potion 10x", "buy bonusxppotion 10x"]:
                    potion = "<:xppotion:1245417682199646290> bonus xp potion 10"
                elif potionbuymsg in ["buy bonusgold", "buy bonus gold potion", "buy gold potion", "buy bonusgoldpotion", "buy bonusgold potion"]:
                    potion = "<:goldpotion:1245417684661702730> bonus gold potion"
                elif potionbuymsg in ["buy bonusgold 10", "buy bonus gold potion 10", "buy gold potion 10", "buy bonusgold potion 10", "buy bonusgoldpotion 10", "buy bonusgold 10x", "buy bonus gold potion 10x", "buy gold potion 10x", "buy bonusgold potion 10x", "buy bonusgoldpotion 10x"]:
                    potion = "<:goldpotion:1245417684661702730> bonus gold potion 10"

                if player:
                    class PotionShopMenu(discord.ui.View):
                        def __init__(self):
                            super().__init__(timeout = None)

                        @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
                        async def confirmbutton(self, interaction: discord.Interaction, button: discord.ui.Button):

                            if potionbuymsg in ["buy healing", "buy healing potion", "buy heal potion"]:
                                healprice = 5
                                if player.Money >= healprice:
                                    inventory_items.append("<:healpotion:1245417680903733249> healing potion")
                                    player.Money = int(player.Money - healprice)
                                    em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention} bought a **<:healpotion:1245417680903733249> healing potion.**\n \nYour balance: **{player.Money}$**\n*— {healprice}$*", color= green)
                                    await interaction.response.edit_message(embed= em, view=None)
                                else:
                                    moneyshort = int(healprice - player.Money)
                                    await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention}, you don't have enough money for **healing potion** :(\n\nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color=red))
                                    return
                            elif potionbuymsg in ["buy healing 10", "buy healing potion 10", "buy heal potion 10", "buy healpotion 10", "buy healingpotion 10", "buy healing 10x", "buy healing potion 10x", "buy heal potion 10x", "buy healpotion 10x", "buy healingpotion 10x"]:
                                tenhealprice = 40
                                if player.Money >= tenhealprice:
                                    for _ in range(10):
                                        inventory_items.append("<:healpotion:1245417680903733249> healing potion")
                                    player.Money = int(player.Money - tenhealprice)
                                    em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention} bought 10 **<:healpotion:1245417680903733249> healing potions.**\n \nYour balance: **{player.Money}$**\n*— {tenhealprice}$*", color= green)
                                    await interaction.response.edit_message(embed= em, view=None)
                                else:
                                    moneyshort = int(tenhealprice - player.Money)
                                    await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention}, you don't have enough money for **10 healing potions** :(\n\nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color=red))
                                    return
                            elif potionbuymsg in ["buy xp", "buy xp potion", "buy xppotion", "buy bonus xp", "buy bonusxp", "buy bonus xp potion", "buy bonusxppotion"]:
                                xpprice = 80
                                if player.Money >= xpprice:
                                    inventory_items.append("<:xppotion:1245417682199646290> bonus xp potion")
                                    player.Money = int(player.Money - xpprice)
                                    em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention} bought a **<:xppotion:1245417682199646290> bonus xp potion.**\n \nYour balance: **{player.Money}$**\n*— {xpprice}$*", color= green)
                                    await interaction.response.edit_message(embed= em, view=None)
                                else:
                                    moneyshort = int(xpprice - player.Money)
                                    await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention}, you don't have enough money for **XP potion** :(\n\nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color=red))
                                    return
                            elif potionbuymsg in ["buy xp 10", "buy xp potion 10", "buy xppotion 10", "buy bonus xp 10", "buy bonusxp 10", "buy bonus xp potion 10", "buy bonusxppotion 10", "buy xp 10x", "buy xp potion 10x", "buy xppotion 10x", "buy bonus xp 10x", "buy bonusxp 10x", "buy bonus xp potion 10x", "buy bonusxppotion 10x"]:
                                tenxpprice = 675
                                if player.Money >= tenxpprice:
                                    for _ in range(10):
                                        inventory_items.append("<:xppotion:1245417682199646290> bonus xp potion")
                                    player.Money = int(player.Money - tenxpprice)
                                    em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention} bought 10 **<:xppotion:1245417682199646290> bonus xp potions.**\n \nYour balance: **{player.Money}$**\n*— {tenxpprice}$*", color= green)
                                    await interaction.response.edit_message(embed= em, view=None)
                                else:
                                    moneyshort = int(tenxpprice - player.Money)
                                    await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention}, you don't have enough money for **10 XP potions** :(\n\nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color=red))
                                    return
                            elif potionbuymsg in ["buy bonusgold", "buy bonus gold potion", "buy gold potion", "buy bonusgoldpotion", "buy bonusgold potion"]:
                                goldprice = 80
                                if player.Money >= goldprice:
                                    inventory_items.append("<:goldpotion:1245417684661702730> bonus gold potion")
                                    player.Money = int(player.Money - goldprice)
                                    em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention} bought a **<:goldpotion:1245417684661702730> bonus gold potion.**\n \nYour balance: **{player.Money}$**\n*— {goldprice}$*", color= green)
                                    await interaction.response.edit_message(embed= em, view=None)
                                else:
                                    moneyshort = int(goldprice - player.Money)
                                    await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention}, you don't have enough money for **Bonus Gold potion** :(\n\nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color=red))
                                    return
                            elif potionbuymsg in ["buy bonusgold 10", "buy bonus gold potion 10", "buy gold potion 10", "buy bonusgold potion 10", "buy bonusgoldpotion 10", "buy bonusgold 10x", "buy bonus gold potion 10x", "buy gold potion 10x", "buy bonusgold potion 10x", "buy bonusgoldpotion 10x"]:
                                tengoldprice = 675
                                if player.Money >= tengoldprice:
                                    for _ in range(10):
                                        inventory_items.append("<:goldpotion:1245417684661702730> bonus gold potion")
                                    player.Money = int(player.Money - tengoldprice)
                                    em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention} bought 10 **<:goldpotion:1245417684661702730> bonus gold potions.**\n \nYour balance: **{player.Money}$**\n*— {tengoldprice}$*", color= green)
                                    await interaction.response.edit_message(embed= em, view=None)
                                else:
                                    moneyshort = int(tengoldprice - player.Money)
                                    await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description=f"{interaction.user.mention}, you don't have enough money for **10 Bonus Gold potions** :(\n\nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color=red))
                                    return
                            
                        @discord.ui.button(label= "Cancel", style=discord.ButtonStyle.red)
                        async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                            global player
                            em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description= f"{interaction.user.mention} did not buy a potion.", color= vividpink)
                            await interaction.response.edit_message(embed=em, view=None)

                    if potionbuymsg in ["buy healing", "buy healing potion", "buy heal potion", "buy healing 10", "buy healing potion 10", "buy heal potion 10", "buy healpotion 10", "buy healingpotion 10", "buy xp", "buy xp potion", "buy xppotion", "buy bonus xp", "buy bonusxp", "buy bonus xp potion", "buy bonusxppotion", "buy xp 10", "buy xp potion 10", "buy xppotion 10", "buy bonus xp 10", "buy bonusxp 10", "buy bonus xp potion 10", "buy bonusxppotion 10", "buy bonusgold", "buy bonus gold potion", "buy gold potion", "buy bonusgoldpotion", "buy bonusgold potion", "buy bonusgold 10", "buy bonus gold potion 10", "buy gold potion 10", "buy bonusgold potion 10", "buy bonusgoldpotion 10", "buy healing 10x", "buy healing potion 10x", "buy heal potion 10x", "buy healpotion 10x", "buy healingpotion 10x", "buy xp 10x", "buy xp potion 10x", "buy xppotion 10x", "buy bonus xp 10x", "buy bonusxp 10x", "buy bonus xp potion 10x", "buy bonusxppotion 10x", "buy bonusgold 10x", "buy bonus gold potion 10x", "buy gold potion 10x", "buy bonusgold potion 10x", "buy bonusgoldpotion 10x"]:
                        em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description= f"{interaction.user.mention}, are you sure you want to buy **{potion}**?", color= vividpink)
                        await interaction.followup.send(embed= em, view=PotionShopMenu())
                    else:
                        em = (discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description="Invalid potion. Please try again.", color= vividpink))
                        await interaction.followup.send(embed= em)

            except asyncio.TimeoutError:
                await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Potions :test_tube:**", description= f"{interaction.user.mention} did not want to buy anything.", color= vividpink), ephemeral=True)

    @discord.ui.button(label= "Titles", style=discord.ButtonStyle.blurple)
    async def titlebuybutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        em = discord.Embed(
    title="**:shopping_cart: CHARMING SHOP - Titles :identification_card:**",
    description=(
        f"{interaction.user.mention} here are the obtainable titles:\n\n"
        "- title 1 - :baby_bottle: *Novice* - **1$**\n"
        "- title 2 - :loudspeaker: *Dummy* - **150$**\n"
        "- title 3 - :adhesive_bandage: *Rogue* - **300$**\n"
        "- title 4 - :dash: *Goofy* - **300$**\n"
        "- title 5 - :archery: *Precise Hunter* - **500$**\n"
        "- title 6 - :briefcase: *Workaholic* - **600$**\n"
        "- title 7 - :milky_way: *Wanderer* - **950$**\n"
        "- title 8 - :wing: *Guardian Angel* - **1000$**\n"
        "- title 9 - :drum: *Memelord* - **1069$**\n"
        "- title 10 - :wine_glass: *Gourmet* - **2000$**\n"
        "- title 11 - :sunglasses: *Smart Head* - **2700$**\n"
        "- title 12 - :alien: *Sus* - **2900$**\n"
        "- title 13 - :crystal_ball: *Pathfinder* - **3000$**\n"
        "- title 14 - :chains: *Deadly Warden* - **4020$**\n"
        "- title 15 - :ocean: *Balanced* - **8888$**\n"
        "- title 16 - :cloud: *Assasin* - **8900$**\n"
        "- title 17 - :glowing_star: *Star Seeker* - **9200$**\n"
        "- title 18 - :fire: *Ember Warrior* - **9999$**\n"
        "- title 19 - :comet: *Dynamic* - **10500$**\n"
        "- title 20 - :knife: *Blade Dancer* - **12000$**\n"
        "- title 21 - :leaves: *Nature's Child* - **13200$**\n"
        "- title 22 - :cloud_tornado: *Phantom* - **15000$**\n"
        "- title 23 - :zap: *Master of Lightning* - **17770$**\n"
        "- title 24 - :crown: *Eternal Champion* - **20500$**\n"
        "- title 25 - :mount_fuji: *The Almighty* - **30000$**\n\n"
        ":warning: To buy a potion, type ***buy title number*** in chat\n"
        ":warning: If you buy a title, your current one will be overwritten"), color=vividpink)
        await interaction.response.edit_message(embed= em)

        def check_message(m):
            return m.author == interaction.user and m.channel == interaction.channel
        try:
            msg = await client.wait_for("message", check=check_message, timeout= None)
            titlebuymsg = msg.content.lower()
            global player

            if titlebuymsg in ["buy title 1", "buy title1", "buy title one"]:
                titleprice = 1
                titlebuy = "🍼 Novice"
            elif titlebuymsg in ["buy title 2", "buy title2", "buy title two"]:
                titleprice = 150
                titlebuy = "📢 Dummy"
            elif titlebuymsg in ["buy title 3", "buy title3", "buy title three"]:
                titleprice = 300
                titlebuy = "🩹 Rogue"
            elif titlebuymsg in ["buy title 4", "buy title4", "buy title four"]:
                titleprice = 300
                titlebuy = "💨 Goofy"
            elif titlebuymsg in ["buy title 5", "buy title5", "buy title five"]:
                titleprice = 500
                titlebuy = "🏹 Precise Hunter"
            elif titlebuymsg in ["buy title 6", "buy title6", "buy title six"]:
                titleprice = 600
                titlebuy = "💼 Workaholic"
            elif titlebuymsg in ["buy title 7", "buy title7", "buy title seven"]:
                titleprice = 950
                titlebuy = "🌌 Wanderer"
            elif titlebuymsg in ["buy title 8", "buy title8", "buy title eight"]:
                titleprice = 1000
                titlebuy = "🪽 Guardian Angel"
            elif titlebuymsg in ["buy title 9", "buy title9", "buy title nine"]:
                titleprice = 1069
                titlebuy = "🥁 Memelord"
            elif titlebuymsg in ["buy title 10", "buy title10", "buy title ten"]:
                titleprice = 2000
                titlebuy = "🍷 Gourmet"
            elif titlebuymsg in ["buy title 11", "buy title11", "buy title eleven"]:
                titleprice = 2700
                titlebuy = "😎 Smart Head"
            elif titlebuymsg in ["buy title 12", "buy title12", "buy title twelve"]:
                titleprice = 2900
                titlebuy = "👽 Sus"
            elif titlebuymsg in ["buy title 13", "buy title13", "buy title thirteen"]:
                titleprice = 3000
                titlebuy = "🔮 Pathfinder"
            elif titlebuymsg in ["buy title 14", "buy title14", "buy title fourteen"]:
                titleprice = 4020
                titlebuy = "⛓️ Deadly Warden"
            elif titlebuymsg in ["buy title 15", "buy title15", "buy title fifteen"]:
                titleprice = 8888
                titlebuy = "🌊 Balanced"
            elif titlebuymsg in ["buy title 16", "buy title16", "buy title sixteen"]:
                titleprice = 8900
                titlebuy = "☁️ Assasin"
            elif titlebuymsg in ["buy title 17", "buy title17", "buy title seventeen"]:
                titleprice = 9200
                titlebuy = "🌟 Star Seeker"
            elif titlebuymsg in ["buy title 18", "buy title18", "buy title eighteen"]:
                titleprice = 9999
                titlebuy = "🔥 Ember Warrior"
            elif titlebuymsg in ["buy title 19", "buy title19", "buy title nineteen"]:
                titleprice = 10500
                titlebuy = "☄️ Dynamic"
            elif titlebuymsg in ["buy title 20", "buy title20", "buy title twenty"]:
                titleprice = 12000
                titlebuy = "🔪 Blade Dancer"
            elif titlebuymsg in ["buy title 21", "buy title21", "buy title twentyone"]:
                titleprice = 13200
                titlebuy = "🍃 Nature's Child"
            elif titlebuymsg in ["buy title 22", "buy title22", "buy title twentytwo"]:
                titleprice = 15000
                titlebuy = "🌪️ Phantom"
            elif titlebuymsg in ["buy title 23", "buy title23", "buy title twentythree"]:
                titleprice = 17770
                titlebuy = "⚡ Master of Lightning"
            elif titlebuymsg in ["buy title 24", "buy title24", "buy title twentyfour"]:
                titleprice = 20500
                titlebuy = "👑 Eternal Champion"
            elif titlebuymsg in ["buy title 25", "buy title25", "buy title twentyfive"]:
                titleprice = 30000
                titlebuy = "🗻 The Almighty"
            
            if player:
                class TitleShopMenu(discord.ui.View):
                    def __init__(self):
                        super().__init__(timeout = None)

                    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
                    async def confirmbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                        if player.Money >= titleprice:
                            player.Title = titlebuy
                            player.Money = int(player.Money - titleprice)
                            em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Titles :identification_card:**", description=f"{interaction.user.mention} bought a **{titlebuy}** title.\n \nYour balance: **{player.Money}$**\n*— {titlebuy}$*", color= green)
                            await interaction.response.edit_message(embed= em, view=None)
                        else:
                            moneyshort = int(titleprice - player.Money)
                            await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Titles :identification_card:**", description=f"{interaction.user.mention}, you don't have enough money for **{titlebuy}** title :(\n\nYour balance: **{player.Money}$**\nYou are *{moneyshort}$* short!", color=red))
                            return
                        
                    @discord.ui.button(label= "Cancel", style=discord.ButtonStyle.red)
                    async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                        global player
                        em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Titles :identification_card:**", description= f"{interaction.user.mention} remains as {player.Title}.", color= vividpink)
                        await interaction.response.edit_message(embed=em, view=None)
                
                if titlebuymsg in ["buy title 1", "buy title one"]:
                    em = discord.Embed(title="**:shopping_cart: CHARMING SHOP - Titles :identification_card:**", description= f"{interaction.user.mention}, are you sure you want to buy **{titlebuy}** title?", color= vividpink)
                    await interaction.followup.send(embed= em, view=TitleShopMenu())
                else:
                    em = (discord.Embed(title="**:shopping_cart: CHARMING SHOP - Titles :identification_card:**", description="Invalid title. Please try again.", color= vividpink))
                    await interaction.followup.send(embed= em)

        except asyncio.TimeoutError:
            await interaction.followup.send(discord.Embed(title="**:shopping_cart: CHARMING SHOP - Titles :identification_card:**", description= f"{interaction.user.mention} did not want to buy anything.", color= vividpink), ephemeral=True)

@client.tree.command(name= "shop", description= "CHARMING SHOP.")
async def actionmenu(interaction: discord.Interaction):
    em = discord.Embed(title= ":shopping_cart: Welcome to *the* **CHARMING SHOP**:sparkles:", description= f"{interaction.user.mention}, what are you looking for?", color = vividpink)
    await interaction.response.send_message(embed= em, view= ShopMenu())

# PETMENU
class PetMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label= "Change name", style=discord.ButtonStyle.blurple)
    async def petnamebutton(self, interaction: discord.Interaction, Button: discord.ui.Button):
        class NameButtonMenu(discord.ui.View):
            def __init__(self):
                super().__init__(timeout = None)

            @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
            async def confirmbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                if pet.Name == "no pet":
                    em = discord.Embed(title= "Pet name change", description= f"{interaction.user.mention}, you cannot change a name of an non-existend pet. Buy one in **:shopping_cart: CHARMING SHOP :sparkles:**", color= red)
                    await interaction.response.edit_message(embed= em, view=None)
                else:
                    em = discord.Embed(title= "Pet name change", description= f"{interaction.user.mention}, type a name which you want your pet to be called. Answer within 60 seconds.\n*Note: The name of your pet can be only changed three times in 24 hours.*", color= yellow)
                    await interaction.response.edit_message(embed= em, view=None)
                    def check_message(m):
                        return m.author == interaction.user and m.channel == interaction.channel
                    try:
                        msg = await client.wait_for("message", check=check_message, timeout=60.0)
                        pet.Name = msg.content
                        em = discord.Embed(title="Pet name changed!", description=f"{interaction.user.mention}'s pet is now named **:{pet.Type}: {pet.Name}**.", color= green)
                        await interaction.followup.send(embed= em)
                    except asyncio.TimeoutError:
                        await interaction.followup.send(discord.Embed(title= "Pet name change", description= f"{interaction.user.mention}, you took too long to respond!", color= red))

            @discord.ui.button(label= "Cancel", style=discord.ButtonStyle.red)
            async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title= "Pet name change", description= f"Pet name change cancelled. **:{pet.Type}: {pet.Name}** will keep its original name.", color= yellow)
                await interaction.response.edit_message(embed=em, view=None)

        em = discord.Embed(title= "Pet name change :grey_question:", description= f"{interaction.user.mention}, are you sure you want to change your pet's name?", color= yellow)
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
        em = discord.Embed(title= "Pet info", description= f"**{interaction.user.mention}'s companion**\n \nName: **{pet_name}**\nHappiness: **{pet.Happiness} / 100**", color = yellow)
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