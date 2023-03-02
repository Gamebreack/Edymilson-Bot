import discord
from discord.ext import commands
import random
import libLoja
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True

intents = discord.Intents.default()
intents.message_content = True

description = '''Eu sou o Edymilson, o bot das crônicas de Módeg.
Eu posso ser um pouco sarcástico, mas sempre ajudarei quando precisar.'''
bot = commands.Bot(command_prefix='ed/', intents=intents, description=description)
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

@bot.command(description='Abre uma seleção de itens do comerciante local')
async def loja(ctx):
    await ctx.send(tabulate(libLoja.samplingLoja(), headers=['Item','Quantidade','Preço'], tablefmt='plain', stralign='right'))

bot.run('NzExMzE2MzkyMDE1NTYwNzYz.XsBPLQ.DOChTB_Mfn48ACSlB8FsnTEntb0')