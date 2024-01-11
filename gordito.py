import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

ideas=["y un dato curioso la contaminacion causa distintas emfermedades como: bronquitis, asma, alergias, entre otras. Muertes y problemas de higiene en las zonas donde el agua está contaminada y no tienen acceso al agua potable", "Pérdida de biodiversidad marina Esta es una de las peores consecuencias de la contaminación y desgraciadamente las especies que más sufren estas consecuencias son aquellas que ya están en peligro de extinción", "La contaminación por la agricultura es la principal causa de contaminación de las aguas. Cuando los químicos de pesticidas, herbicidas y fertilizantes entran en el agua subterránea, terminan en el agua potable, lo que a su vez produce consecuencias devastadoras para la salud, como el Síndrome del Bebé Azul"]
@bot.command(description='For when you wanna settle the score some other way')
async def presidente(ctx):
    """Chooses between multiple choices."""
    await ctx.send("el presidente de chile es gabriel boric",random.choice(ideas))
@bot.command(description='For when you wanna settle the score some other way')
async def dia(ctx):
    """Chooses between multiple choices."""
    await ctx.send("hoy es 11-01-2024",random.choice(ideas))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """este bot es cool?"""
    await ctx.send('Yes, the bot is cool.')
@presidente.command(name='bot')
async def _bot(ctx):
    """el presidente de chile es gabriel boric"""
    await ctx.send('gabriel boric')
@dia.command(name='bot')
async def _bot(ctx):
    """hoy es 11-01-2024"""
    await ctx.send('')



bot.run('MTE4NzUzMTgwMjczNTI4NDM3NQ.GasnO2.bJA4iWSyjYxECNw9059KMvA3yj8ua1riaPvkKQ')
