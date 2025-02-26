#--------------Загальні команди (start, help)-------------

import discord
from discord import app_commands
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="start", description="Start the bot and get an introduction message.")
    async def start(self, interaction: discord.Interaction):
        await interaction.response.send_message("👋 Hello! I am your AnimeBot. Use /top-anime to see the top anime, or /airing-anime to view currently airing anime!")

    @app_commands.command(name="help", description="Get a list of available commands.")
    async def help(self, interaction: discord.Interaction):
        help_message = (
            "Here are the commands you can use:\n"
            "/start - Introduction message\n"
            "/top-anime - Displays the top 10 popular anime\n"
            "/airing-anime - Shows the top 10 currently airing anime\n"
        )
        await interaction.response.send_message(help_message)

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))