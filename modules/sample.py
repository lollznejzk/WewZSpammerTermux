import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="{cmdprefix}", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot connecté : {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("Bot opérationnel.")

bot.run("{bottoken}")
