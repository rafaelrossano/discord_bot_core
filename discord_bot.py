import discord
from discord.ext import commands
from discord import app_commands
from main import *

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=1318039961005592688)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        
        except Exception as e:
            print(e)

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1318039961005592688)

@client.tree.command(name="nickname_com_data", description='Filtra os logs de acesso, realizados dentro do intervalo inserido, através do nickname.', guild = GUILD_ID)
async def by_nickname_with_date(interaction: discord.Interaction, nickname: str, data_inicial: str, data_final: str):
    #await interaction.response.send_message("teste")
    get_by_nickname_with_date(nickname, data_inicial, data_final)
    with open("result.txt", "rb") as file:
        await interaction.response.send_message("Baixe o arquivo disponibilizado para acessar as informações.", file=discord.File(file, "result.txt"))


@client.tree.command(name="ip_com_data", description='Filtra os logs de acesso, realizados dentro do intervalo inserido, através do IP.', guild = GUILD_ID)
async def by_nickname_with_date(interaction: discord.Interaction, ip: str, data_inicial: str, data_final: str):
    #await interaction.response.send_message("teste")
    get_by_ip_with_date(ip, data_inicial, data_final)
    with open("result.txt", "rb") as file:
        await interaction.response.send_message("Baixe o arquivo disponibilizado para acessar as informações.", file=discord.File(file, "result.txt"))


@client.tree.command(name="url_com_data", description='Filtra os logs de acesso, realizados dentro do intervalo inserido, através do URL.', guild = GUILD_ID)
async def by_nickname_with_date(interaction: discord.Interaction, url: str, data_inicial: str, data_final: str):
    #await interaction.response.send_message("teste")
    get_by_path_with_date(url, data_inicial, data_final)
    with open("result.txt", "rb") as file:
        await interaction.response.send_message("Baixe o arquivo disponibilizado para acessar as informações.", file=discord.File(file, "result.txt"))


@client.tree.command(name="nickname", description='Filtra os logs de acesso, sem intervalos definidos, por nickname.', guild = GUILD_ID)
async def by_nickname(interaction: discord.Interaction, nickname: str):
    #await interaction.response.send_message("teste")
    get_by_nickname(nickname)
    with open("result.txt", "rb") as file:
        await interaction.response.send_message("Baixe o arquivo disponibilizado para acessar as informações.", file=discord.File(file, "result.txt"))


@client.tree.command(name="ip", description='Filtra os logs de acesso, sem intervalos definidos, por IP.', guild = GUILD_ID)
async def by_ip(interaction: discord.Interaction, ip: str):
    #await interaction.response.send_message("teste")
    get_by_ip(ip)
    with open("result.txt", "rb") as file:
        await interaction.response.send_message("Baixe o arquivo disponibilizado para acessar as informações.", file=discord.File(file, "result.txt"))


@client.tree.command(name="url", description='Filtra os logs de acesso, sem intervalos definidos, por URL.', guild = GUILD_ID)
async def by_url(interaction: discord.Interaction, url: str):
    #await interaction.response.send_message("teste")
    get_by_path(url)
    with open("result.txt", "rb") as file:
        await interaction.response.send_message("Baixe o arquivo disponibilizado para acessar as informações.", file=discord.File(file, "result.txt"))


client.run(<discord_token>)