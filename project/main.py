import discord
from discord.ext import commands
import random
from yolo import saver
from fact import fact
intents = discord.Intents.default()
intents.message_content = True
fact_list = ["The first computer mouse: Made of wood", "18% of total emissions comes from operating our homes.", "LED light bulbs use up to 80% less energy than traditional incandescent bulbs"]

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def energy(ctx, org=0):
    await ctx.send(f'Please also insert people BTU{bot.user}')
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            await attachments.save("image/"+attachments.filename)
            
            await ctx.send(saver(attachments.filename, org))
            
    else:
        await ctx.send("Images not found!")


@bot.command()
async def fact(ctx):
    fact = random.choices(fact_list,k=1)
    await ctx.send(fact)







bot.run("MTIxODIxNjQwMTQwODM2NDU5NA.GRA1J4.cokG-AXi89G1F6MHUXofCMqrsksRv_qycq0TuI")           








