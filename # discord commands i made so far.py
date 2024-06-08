# PULL
# @client.tree.command(name= "pull", description= "Pulls an artifact for 1500$.")
# async def pull(interaction: discord.Interaction):
#     quality = random.choice(artifacts_quality)
#     artifact = random.choice(artifacts)
#     em = discord.Embed(title= "Pulled Artifact", description= f"You have pulled *{quality} {artifact}*.", color= discord.Color.pink())
#     await interaction.response.send_message(embed= em)


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