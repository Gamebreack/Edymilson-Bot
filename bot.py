import libLoja
import variables
import privateKeys
import discord
from discord.ext import commands
import random
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='ed/', intents=intents, description=variables.description)

@bot.event
async def on_ready():
    print('Entrou como')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ajuda(ctx):
    await ctx.send(variables.textoDeAjuda)

@bot.command()
async def rolar(ctx, dice):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send(str(ctx.message.author.nick) + '. Tenta de novo...')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(str(ctx.message.author.nick) + ' rolou ' + result)

@bot.command(description='Para quando você não sabe o que fazer. Seu idiota...')
async def escolha(ctx, *choices: str):
    await ctx.send(random.choice(choices) + '... E na próxima escolha você mesmo ' + str(ctx.message.author.nick))

@bot.command(description='Abre uma seleção de itens do comerciante local')
async def loja(ctx):
    await ctx.send(tabulate(libLoja.samplingLoja(), headers=['Item','Quantidade','Preço'], tablefmt='plain', stralign='right'))

bot.run(privateKeys.discordToken)