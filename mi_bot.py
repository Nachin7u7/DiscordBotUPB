import discord
from discord.ext import commands
import requests
import asyncio

TOKEN = 'tu_token_de_discord'

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Función para obtener el webhook de un canal específico
async def get_webhook(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        webhooks = await channel.webhooks()
        if webhooks:
            return webhooks[0]  # Devuelve el primer webhook en el canal si ya existe uno
        else:
            return await channel.create_webhook(name="Anuncio Webhook")  # Crea un nuevo webhook si no hay ninguno
    else:
        return None

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
    embed = discord.Embed(title="Mensaje Enviado", description=f'Se ha enviado un mensaje a {usuario.mention}', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def verificar(ctx):
    if discord.utils.get(ctx.author.roles, name='Admin'):
        embed = discord.Embed(title="Verificación", description="¡Eres un administrador! :crown:", color=0x00ff00)
    else:
        embed = discord.Embed(title="Verificación", description="No eres un administrador.", color=0xff0000)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def anunciar(ctx, canal: discord.TextChannel, *, mensaje: str):
    await canal.send(embed=discord.Embed(title="Anuncio", description=mensaje, color=0x00ff00))
    embed = discord.Embed(title="Anuncio", description=f'Anuncio enviado al canal {canal.mention}', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def consulta_api(ctx):
    fact = await consulta_ninja_cat_api()
    embed = discord.Embed(title="Consulta API", description=f'**Hecho de gatos:**\n\n*{fact}*', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def fact_gato(ctx):
    fact = await consulta_ninja_cat_api()
    embed = discord.Embed(title="Hecho de gatos", description=f'\n\n*{fact}*', color=0x00ff00)
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)

async def announce_with_webhook(webhook, mensaje):
    await webhook.send(embed=discord.Embed(title="Anuncio", description=mensaje, color=0x00ff00))

async def call_anunciar():
    # Aquí necesitas el ID del canal en el que quieres realizar el anuncio
    canal_id = 1224440282058199222
    mensaje = "Este es un anuncio realizado desde el bot usando un webhook."
    webhook = await get_webhook(canal_id)
    if webhook:
        await announce_with_webhook(webhook, mensaje)
    else:
        print("No se pudo encontrar el webhook o crear uno nuevo.")

async def main():
    await bot.start(TOKEN)
    await call_anunciar()

asyncio.run(main())
