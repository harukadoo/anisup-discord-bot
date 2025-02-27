#--------------Команди, пов'язані з аніме---------------

import discord
from discord import app_commands
from discord.ext import commands
from api import get_popular_anime, get_airing_anime, get_anime_by_season, find_anime_by_description, recommend_anime_by_preferences
import datetime
import asyncio
from models.anime import Anime 

FIRST_ANIME_YEAR = 1917
CURRENT_YEAR = datetime.datetime.now().year

class AnimeDetailsButton(discord.ui.Button):
    def __init__(self, anime: Anime, number: int):
        super().__init__(label=f"More info ({number})", style=discord.ButtonStyle.primary)
        self.anime = anime
        self.number = number

    async def callback(self, interaction: discord.Interaction):
        embed = self.anime.get_embed()
        await interaction.response.send_message(embed=embed, ephemeral=True)


class AnimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_data = {}

    async def send_anime_list(self, interaction: discord.Interaction, anime_list, title, start_index=0):
        if not anime_list:
            await interaction.followup.send("Failed to retrieve the anime list. Please try again later.")
            return

        user_id = interaction.user.id
        self.user_data[user_id] = {"anime_list": anime_list, "index": start_index + 10}

        embed = discord.Embed(title=title, color=discord.Color.pink())
        view = discord.ui.View()

        for i, anime_data in enumerate(anime_list[start_index:start_index + 10], start=start_index + 1):
            anime = Anime(anime_data)
            title = anime.title
            url = anime.url
            mean_score = anime.mean_score
            year = anime.start_date

            if year != "Unknown" and year:
                year = year.split("-")[0]

            embed.add_field(
                name=f"{i}. {title}",
                value=f"📅 Release date: {year}\n⭐ Score: {mean_score}\n[Watch on MAL]({url})\n\u200b",
                inline=False
            )

            view.add_item(AnimeDetailsButton(anime, i))

        embed.set_footer(text="Want to see more anime? Use the command: /more")

        await interaction.followup.send(embed=embed, view=view)

    @app_commands.command(name="top-anime", description="Show the top 10 popular anime")
    async def top_anime(self, interaction: discord.Interaction):
        await interaction.response.defer()

        try:
            anime_list = await asyncio.wait_for(get_popular_anime(), timeout=10)
            if anime_list is None:
                await interaction.followup.send("❌ Error: Failed to retrieve the anime list.")
                return

            await self.send_anime_list(interaction, anime_list, "🔥 **Top 10 Popular Anime**")

        except asyncio.TimeoutError:
            await interaction.followup.send("⏳ API is not responding, please try again later.")

        except Exception as e:
            await interaction.followup.send(f"❌ Error: {e}")


    @app_commands.command(name="airing-anime", description="Show the top 10 currently airing anime")
    async def airing_anime(self, interaction: discord.Interaction):
        await interaction.response.defer()

        anime_list = await get_airing_anime()
        await self.send_anime_list(interaction, anime_list, "📺 **Top 10 Airing Anime**")


    @app_commands.command(name="seasonal-anime", description="Show anime of a certain season")
    async def seasonal_anime(self, interaction: discord.Interaction, year: int, season: str):
        await interaction.response.defer()
        valid_seasons = ["winter", "spring", "summer", "fall"]
        
        if season.lower() not in valid_seasons:
            await interaction.followup.send("❌ Error: Invalid season. Choose from: winter, spring, summer, fall.")
            return
        
        if not (FIRST_ANIME_YEAR <= year <= CURRENT_YEAR):
            await interaction.followup.send(f"❌ Error: Year must be in range {FIRST_ANIME_YEAR}-{CURRENT_YEAR}.")
            return
        
        anime_list = await get_anime_by_season(year, season.lower())
        await self.send_anime_list(interaction, anime_list, f"📅 **Anime from {season.capitalize()} {year}**")


    @app_commands.command(name="more", description="Show 10 more anime")
    async def more(self, interaction: discord.Interaction):
        await interaction.response.defer()

        user_id = interaction.user.id
        if user_id not in self.user_data:
            await interaction.followup.send("No data available to load. Use one of the commands first: **/top-anime, /airing-anime, /seasonal-anime**")
            return

        user_info = self.user_data[user_id]
        anime_list = user_info["anime_list"]
        start_index = user_info["index"]

        if start_index >= len(anime_list):
            await interaction.followup.send("No more anime in the list.")
            return

        await self.send_anime_list(interaction, anime_list, "📜 **Continued list**", start_index)


    @app_commands.command(name="find-anime", description="Find an anime by description")
    async def find_anime(self, interaction: discord.Interaction, description: str):
        await interaction.response.defer()
        try:
            anime_name = find_anime_by_description(description)
            embed = discord.Embed(
                title="🔍 **Found Anime**",
                description=f"**Title:**   {anime_name}",
                color=discord.Color.yellow()
            )
            await interaction.followup.send(embed=embed)

        except Exception as e:
            await interaction.followup.send(f"❌ Error: {e}")

    @app_commands.command(name="recommend", description="Recommend an anime based on your preferences")
    async def recommend_anime(self, interaction: discord.Interaction, preferences: str):
        await interaction.response.defer()
        try:
            recommendation = recommend_anime_by_preferences(preferences)
            embed = discord.Embed(
                title="🎌 **Recommended Anime**",
                description=recommendation,
                color=discord.Color.purple()
            )
            await interaction.followup.send(embed=embed)

        except Exception as e:
            await interaction.followup.send(f"❌ Error: {e}")

async def setup(bot):
    await bot.add_cog(AnimeCog(bot))
