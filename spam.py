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
