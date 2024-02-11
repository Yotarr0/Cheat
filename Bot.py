import discord
from discord import app_commands
from discord.ext import commands
import json, requests

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='c!', intents=intents)

@bot.event
async def on_ready():
  await bot.tree.sync()
  print(f"Logged In As {bot.user}")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Key Links | Made By Culty"))
  
@discord.app_commands.checks.cooldown(1, 180)
@bot.tree.command(name="fluxus-key", description="Get Fluxus Key")
async def fluxus(interaction, link: str):
    try:
        url = 'https://tiger-unbiased-quagga.ngrok-free.app/api/fluxus/v1/'
        data = {'link': link}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=data, headers=headers)
        key = r.json()["info"]["key"]
        await interaction.response.send_message(key)
    except Exception as e:
      print(e)
      await interaction.response.send_message("an error accured", ephemeral=True)

@fluxus.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)
        
bot.run("MTIwNjI5NTc0ODEyODQwNzY3Mw.GQ36FX.M5fQarndZyGT3mSbcGYbHA8Ww8dK5yXXr7I7U8")
