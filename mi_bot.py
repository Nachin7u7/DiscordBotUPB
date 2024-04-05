import discord
from discord.ext import commands
import requests

TOKEN = 'TOKEN AQUI NO OLVIDAR!!!'

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
    embed = discord.Embed(title="Mensaje Enviado",
                          description=f'Se ha enviado un mensaje a {usuario.mention}', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)


@bot.command()
async def verificar(ctx):
    if discord.utils.get(ctx.author.roles, name='Admin'):
        embed = discord.Embed(
            title="Verificación", description="¡Eres un administrador! :crown:", color=0x00ff00)
    else:
        embed = discord.Embed(
            title="Verificación", description="No eres un administrador.", color=0xff0000)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)


@bot.command()
async def anunciar(ctx, canal: discord.TextChannel, *, mensaje: str):
    await canal.send(embed=discord.Embed(title="Anuncio", description=mensaje, color=0x00ff00))
    embed = discord.Embed(
        title="Anuncio", description=f'Anuncio enviado al canal {canal.mention}', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)


@bot.command()
async def consulta_api(ctx):
    fact = await consulta_ninja_cat_api()
    embed = discord.Embed(
        title="Consulta API", description=f'**Hecho de gatos:**\n\n*{fact}*', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)


@bot.command()
async def fact_gato(ctx):
    fact = await consulta_ninja_cat_api()
    embed = discord.Embed(title="Hecho de gatos",
                          description=f'\n\n*{fact}*', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)

bot.run(TOKEN)
