import discord
from discord.ext import commands
import random
import libLoja
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True


description = '''Eu sou o Edymilson, o bot das crônicas de Módeg.
Eu posso ser um pouco sarcástico, mas sempre ajudarei quando precisar.'''
bot = commands.Bot(command_prefix='ed/', description=description)
textoDeAjuda = '''

Eu sou o Edymilson, o bot das crônicas de Módeg.
Eu posso ser um pouco sarcástico, mas sempre ajudarei quando precisar.
Você pode me pedir ajuda usando prefixo (ed/) e me informando o comando que deseja que eu execute.



* rolar NdN
Rola um determinado número de dados. Exemplo de uso: ed/rolar 1d6

* Escolha opção 1, opção 2, opção n
Permite aos jogadores deixar uma escolha a cargo do Edymilson. Exemplo de uso: ed/escolha matar perdoar

* ping
Mostra a latência do Bot com o servidor. Exemplo de uso: ed/ping

* produtos
Mostra o estoque de produtos de uma loja. Exemplo de uso: ed/produtos

'''

@bot.event
async def on_ready():
    print('Entrou como')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ajuda(ctx):
    await ctx.send(textoDeAjuda)

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

@bot.command()
async def entrou(ctx, member: discord.Member):
    await ctx.send('{0.name} chegou em {0.joined_at}, yaaaay...'.format(member))

@bot.command()
async def loja(ctx):
    await ctx.send(tabulate(libLoja.samplingLoja(), headers=['Item','Quantidade','Preço'], tablefmt='plain', stralign='right'))

@bot.command()
async def teste(ctx):
    await ctx.send(description)

@bot.command()
async def ping(ctx):
    latencia = bot.latency
    await ctx.send(str(round(latencia)) + ' ms')

@bot.group()
async def legal(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Não, {0.subcommand_passed} não é legal'.format(ctx))


bot.run('NzExMzE2MzkyMDE1NTYwNzYz.XsBPLQ.DOChTB_Mfn48ACSlB8FsnTEntb0')