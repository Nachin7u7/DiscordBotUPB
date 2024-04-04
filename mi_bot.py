import discord
from discord.ext import commands
import requests

TOKEN = 'NO OLVIDAR EL TOKEN!'

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)


async def consulta_ninja_cat_api():
    url = 'https://catfact.ninja/fact?max_length=1000'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['fact']
    else:
        return 'No se pudo obtener un hecho de gatos en este momento. Inténtalo de nuevo más tarde.'


@bot.event
async def on_ready():
    print(f'{bot.user.name} ha iniciado sesión')


@bot.command()
async def enviar_mensaje(ctx, usuario: discord.User, *, mensaje: str):
    await usuario.send(mensaje)
    await ctx.send(f'Se ha enviado un mensaje a {usuario.name}')


@bot.command()
async def verificar(ctx):
    if discord.utils.get(ctx.author.roles, name='Admin'):
        await ctx.send('¡Eres un administrador!')
    else:
        await ctx.send('No eres un administrador.')


@bot.command()
async def anunciar(ctx, canal: discord.TextChannel, *, mensaje: str):
    await canal.send(mensaje)
    await ctx.send(f'Anuncio enviado al canal {canal.mention}')


@bot.command()
async def consulta_api(ctx):
    fact = await consulta_ninja_cat_api()
    await ctx.send(fact)


@bot.command()
async def fact_gato(ctx):
    fact = await consulta_ninja_cat_api()
    await ctx.send(fact)

bot.run(TOKEN)
