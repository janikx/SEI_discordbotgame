from collections import Counter
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def count_items(ctx):
    my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    counter = Counter(my_list)

    # Construct the message string
    message = '\n'.join([f"{item}: {count}" for item, count in counter.items()])

    # Send the message
    await ctx.send(message)

bot.run('YOUR_BOT_TOKEN')
