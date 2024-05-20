import discord
import random
import asyncio

class PetMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Change name", style=discord.ButtonStyle.blurple)
    async def namebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        class NameButtonMenu(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)

            @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
            async def cancelbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title="Pet name change", description="Pet name change successfully cancelled.", color=15548997)
                await interaction.response.edit_message(embed=em, view=None)

            @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
            async def confirmbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
                if pet.Name == "no pet":
                    em = discord.Embed(title="Pet name change", description=f"{interaction.user.mention}, you cannot change the name of a non-existent pet. Buy one in **:shopping_cart: CHARMING SHOP :sparkles:**", color=15548997)
                    await interaction.response.edit_message(embed=em, view=None)
                else:
                    em = discord.Embed(title="Pet name change", description=f"{interaction.user.mention}, type a name which you want your pet to be called. Answer within 60 seconds.", color=15844367)
                    await interaction.response.edit_message(embed=em, view=None)
                    def check_message(m):
                        return m.author == interaction.user and m.channel == interaction.channel
                    try:
                        msg = await client.wait_for("message", check=check_message, timeout=60.0)
                        pet.Name = msg.content
                        em = discord.Embed(title="Pet name changed!", description=f"{interaction.user.mention}'s pet is now named **:{pet.Type}: {pet.Name}**.", color=15844367)
                        await interaction.followup.send(embed=em)
                    except asyncio.TimeoutError:
                        await interaction.followup.send(discord.Embed(title="Pet name change", description=f"{interaction.user.mention} took too long to respond!", color=15844367), ephemeral=True)

        em = discord.Embed(title="Pet name change :grey_question:", description=f"{interaction.user.mention}, are you sure you want to change your pet's name?", color=15844367)
        await interaction.response.edit_message(embed=em, view=NameButtonMenu())

    @discord.ui.button(label="Play", style=discord.ButtonStyle.blurple)
    async def playbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        earned_happiness = random.randint(5, 9)
        if pet.Name == "no pet":
            pet.Happiness = 0
            em = discord.Embed(title="No pet :()", description=f"{interaction.user.mention}, you can't play with a pet because you don't have one. Purchase one in **:shopping_cart: CHARMING SHOP :sparkles:**", color=15548997)
        else:
            if (pet.Happiness + earned_happiness) >= 100:
                pet.Happiness = 100
            else:
                pet.Happiness += earned_happiness
            em = discord.Embed(title="Happiness increased", description=f"You played with **:{pet.Type}: {pet.Name}** and it had so much fun.\n*Happiness:* **+ {earned_happiness}**", color=15844367)
        await interaction.response.edit_message(embed=em)

    @discord.ui.button(label="Feed", style=discord.ButtonStyle.blurple)
    async def feedbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        earned_happiness = random.randint(15, 20)
        if pet.Name == "no pet":
            pet.Happiness = 0
            em = discord.Embed(title="No pet :()", description=f"{interaction.user.mention}, you don't have any pet to be fed. Purchase one in **:shopping_cart: CHARMING SHOP :sparkles:**", color=15548997)
        else:
            if (pet.Happiness + earned_happiness) >= 100:
                pet.Happiness = 100
            else:
                pet.Happiness += earned_happiness
            em = discord.Embed(title="Happiness increased", description=f"You fed **:{pet.Type}: {pet.Name}** and it was extremely happy.\n*Happiness:* **+ {earned_happiness}**", color=15844367)
        await interaction.response.edit_message(embed=em)

    @discord.ui.button(label="Pet info", style=discord.ButtonStyle.green)
    async def petbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        if pet.Type == "no pet":
            pet_name = pet.Type
        else:
            pet_name = f":{pet.Type}: {pet.Name}"
        em = discord.Embed(title="Pet info", description=f"**{interaction.user.mention}'s companion**\n\nName: **{pet_name}**\nHappiness: **{pet.Happiness} / 100**", color=15844367)
        await interaction.response.edit_message(embed=em)

@client.tree.command(name="petmenu", description="Menu to check up on your sweet pet.")
async def petmenu(interaction: discord.Interaction):
    if pet.Type == "no pet":
        pet_type = pet.Type
    else:
        pet_type = f":{pet.Type}: {pet.Name}"
    em = discord.Embed(title="Pet info", description=f"**{interaction.user.mention}'s companion**\n\nName: **{pet_type}**\nHappiness: **{pet.Happiness} / 100**", color=15844367)
    await interaction.response.send_message(embed=em, view=PetMenu())
