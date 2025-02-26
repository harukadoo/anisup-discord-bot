#-------Основний файл запуску бота---------

import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class AnimeBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.load_extension("cogs.anime")
        await self.load_extension("cogs.general")
        await self.tree.sync()

    async def on_ready(self):
        print(f"Bot {self.user} is online and ready!")

bot = AnimeBot()

async def main():
    async with bot:
        await bot.start(TOKEN)  

asyncio.run(main())




