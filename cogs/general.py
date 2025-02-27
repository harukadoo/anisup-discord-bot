#--------------General commands (start, help)-------------

import discord
from discord import Interaction, app_commands
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="start", description="Start the bot and get an introduction message.")
    async def start(self, interaction: Interaction):
        embed = discord.Embed(
            title="👋 Hello! I am your AnimeBot.",
            description=(
                "The aim of the project is to create a bot on Discord that provides users with convenient access to information about anime. The bot enables:\n\n"
                "- Receive lists of popular and currently airing anime.\n"
                "- Search for anime by season and year.\n"
                "- Finding an anime title based on the description.\n"
                "- Receiving personalized recommendations based on user preferences.\n\n"
                "You can find out more about my project on GitHub: [GitHub Link](https://github.com/harukadoo/anisup-discord-bot)"
            ),
            
            color=discord.Color.pink() 
        )

        embed.set_thumbnail(url="attachment://logo.png") 

        file = discord.File("img/logo.png", filename="logo.png")
        await interaction.response.send_message(embed=embed, file=file)


    @app_commands.command(name="help", description="Get a list of available commands.")
    async def help(self, interaction: discord.Interaction):
        help_message = (
            "🧡 If you encounter any issues, feel free to contact the developer:\n"
            "Discord: kurap1kaa\n"
            "Telegram: @bakugoukk"
        )
        await interaction.response.send_message(help_message)

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))