#----------------Classes for working with anime---------------

import discord

class Anime:
    def __init__(self, anime_data):
        self.data = anime_data

    @property
    def title(self):
        return self.data["node"]["title"]

    @property
    def url(self):
        return f"https://myanimelist.net/anime/{self.data['node']['id']}"

    @property
    def mean_score(self):
        return self.data["node"].get("mean", "N/A")

    @property
    def episodes(self):
        return self.data["node"].get("num_episodes", "Unknown")

    @property
    def status(self):
        return self.data["node"].get("status", "Unknown")

    @property
    def duration(self):
        return self.data["node"].get("average_episode_duration", 0) // 60

    @property
    def start_date(self):
        return self.data["node"].get("start_date", "Unknown")

    @property
    def end_date(self):
        return self.data["node"].get("end_date", "Unknown")

    @property
    def genres(self):
        return ", ".join(genre["name"] for genre in self.data["node"].get("genres", [])) or "Unknown"

    @property
    def studios(self):
        return ", ".join(studio["name"] for studio in self.data["node"].get("studios", [])) or "Unknown"

    @property
    def image_url(self):
        return self.data["node"].get("main_picture", {}).get("large") or self.data["node"].get("main_picture", {}).get("medium")

    @property
    def synopsis(self):
        return self.data["node"].get("synopsis", "No description available.")

    def get_embed(self):
        embed = discord.Embed(title=self.title, url=self.url, description="📌 " + self.synopsis, color=discord.Color.pink())
        
        embed.add_field(name="⭐ Rating:", value=f"{self.mean_score}/10", inline=True)
        embed.add_field(name="🎞️ Episodes:", value=self.episodes, inline=True)
        embed.add_field(name="⏳ Status:", value=self.status, inline=True)

        embed.add_field(name="⏱️ Episode duration:", value=f"{self.duration} min", inline=True)
        embed.add_field(name="📆 Airing start:", value=self.start_date, inline=True)
        embed.add_field(name="📅 Airing end:", value=self.end_date, inline=True)

        embed.add_field(name="🎭 Genres:", value=self.genres, inline=False)
        embed.add_field(name="🏢 Studio:", value=self.studios, inline=False)

        if self.image_url:
            embed.set_image(url=self.image_url)

        embed.set_footer(text="🎥 Click the title to see more on MyAnimeList")

        return embed
