import discord
from discord.ext import commands

TOKEN = 'Agregar token de bot aqui'

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)


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
    # TODO Realizar la consulta a la API aquí
    await ctx.send('Resultado de la consulta a la API')

bot.run(TOKEN)


# Función para probar enviar un mensaje privado
# async def probar_enviar_mensaje():
#     # Reemplaza usuario_id con el ID de 'nachin7u7'
#     print("enviando mensaje...")
#     usuario = await bot.fetch_user("nachin7u7#0657")
#     await bot.invoke(await bot.get_context(discord.Message(content=f"!enviar_mensaje {usuario.mention} Hola, esto es un mensaje privado para ti.")))

# Función para probar hacer un anuncio


# async def probar_anunciar():
#     print("enviando anuncio...")
#     await bot.invoke(await bot.get_context(discord.Message(content="!anunciar Hola! Soy el bot de prueba y esto es una prueba.")))

# Llama a las funciones de prueba
# bot.loop.create_task(probar_enviar_mensaje())
# bot.loop.create_task(probar_anunciar())
