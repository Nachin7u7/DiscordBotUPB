import discord
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='b!', intents=intents)
my_secret = os.environ['MyToken']
api_base_url = "https://grades-microservice.vercel.app/api/v1"


async def get_payment_details(enrollment_code):
    api_url = f"{api_base_url}/paymentDetail/{enrollment_code}"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        if response.status_code == 200:
            coins = float(data['data']['coins'])
            diamonds = float(data['data']['diamond'])
            return coins, diamonds
        else:
            return None, None
    except Exception as e:
        print(f'Error al conectar con la API: {str(e)}')
        return None, None


@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="¡Bienvenido soy UPB Server Bot!",
        description="Aquí tienes una lista de comandos disponibles:",
        color=0x00ff00  # Color verde
    )
    embed.add_field(name="b!saldo [código de estudiante UPB]",
                    value="Consulta el saldo de monedas y diamantes.")
    embed.add_field(name="b!coins [cantidad] [código de estudiante UPB]",
                    value="Añade monedas a la cuenta.(Solo para personal autorizado)")
    embed.add_field(name="b!diamonds [cantidad] [código de estudiante UPB]",
                    value="Añade diamantes a la cuenta.(Solo para personal autorizado)")
    embed.add_field(name="b!ayuda", value="Muestra este mensaje de ayuda.")
    await ctx.send(embed=embed)


@bot.command()
async def saldo(ctx, enrollment_code: int):
    coins, diamonds = await get_payment_details(enrollment_code)
    if coins is not None and diamonds is not None:
        embed = discord.Embed(
            title="Saldo",
            description=f"Saldo actual: {coins} monedas, {diamonds} diamantes",
            color=0x00ff00  # Color verde
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send('Error al obtener el saldo.')


@bot.command()
@commands.has_any_role('Lead', 'Senior Admin')
async def coins(ctx, amount: float, enrollment_code: int):
    current_coins, current_diamonds = await get_payment_details(enrollment_code)
    if current_coins is not None:
        new_coins = current_coins + amount
        api_url = f"{api_base_url}/paymentDetail/{enrollment_code}"
        headers = {"Content-Type": "application/json"}
        body = {"coins": new_coins}
        try:
            response = requests.put(api_url, json=body, headers=headers)
            data = response.json()
            if response.status_code == 200:
                embed = discord.Embed(
                    title="Monedas añadidas correctamente",
                    description=f'Se han añadido {amount} monedas correctamente. Nuevo saldo: {new_coins} monedas.',
                    color=0x00ff00  # Color verde
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Error al añadir monedas",
                    description=f'Error: {data["message"]}',
                    color=0xff0000  # Color rojo
                )
                await ctx.send(embed=embed)
        except Exception as e:
            print(f'Error al conectar con la API: {str(e)}')
            await ctx.send('Error al conectar con la API.')
    else:
        await ctx.send('Error al obtener el saldo actual.')


@bot.command()
@commands.has_any_role('Lead', 'Senior Admin')
async def diamonds(ctx, amount: float, enrollment_code: int):
    current_coins, current_diamonds = await get_payment_details(enrollment_code)
    if current_diamonds is not None:
        new_diamonds = current_diamonds + amount
        api_url = f"{api_base_url}/paymentDetail/{enrollment_code}"
        headers = {"Content-Type": "application/json"}
        body = {"diamond": new_diamonds}
        try:
            response = requests.put(api_url, json=body, headers=headers)
            data = response.json()
            if response.status_code == 200:
                embed = discord.Embed(
                    title="Diamantes añadidos correctamente",
                    description=f'Se han añadido {amount} diamantes correctamente. Nuevo saldo: {new_diamonds} diamantes.',
                    color=0x00ff00  # Color verde
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Error al añadir diamantes",
                    description=f'Error: {data["message"]}',
                    color=0xff0000  # Color rojo
                )
                await ctx.send(embed=embed)
        except Exception as e:
            print(f'Error al conectar con la API: {str(e)}')
            await ctx.send('Error al conectar con la API.')
    else:
        await ctx.send('Error al obtener el saldo actual.')

bot.run(my_secret)
