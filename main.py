import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    
    channel = bot.get_channel(1272482868370608182) 
    if channel:
        await channel.send("I'm online and ready to go!")

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.event
async def on_message(message):
    if message.content == bot.command_prefix:
        commands_list = "\n".join([f"!{command}" for command in bot.commands])
        await message.channel.send(f"Available commands:\n{commands_list}")
    else:
        await bot.process_commands(message)

bot.run('BOT_TOKEN')
