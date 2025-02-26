#--------------Запити до API MyAnimeList-------------

import aiohttp
import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()
MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def find_anime_by_description(description: str) -> str:
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[ 
                {
                    "role": "system",
                    "content": "You are an anime expert. Based on the description, help the user remember the name of the anime."
                },
                {
                    "role": "user",
                    "content": f"What is the name of the anime if it is described like this, give only the title: {description}?"
                }
            ]
        )

        if not chat_response or not chat_response.choices:
            raise ValueError("No response from the AI model.")

        anime_name = chat_response.choices[0].message.content
        return anime_name

    except Exception as e:
        raise Exception(f"Error in find_anime_by_description: {e}")

def recommend_anime_by_preferences(preferences: str) -> str:
    """
    Recommend an anime based on user preferences using Mistral AI.
    """
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[ 
                {
                    "role": "system",
                    "content": "You are an anime expert. Based on the user's preferences, recommend an anime and provide a brief explanation."
                },
                {
                    "role": "user",
                    "content": f"I want to watch an anime that is: {preferences}. What do you recommend?"
                }
            ]
        )

        if not chat_response or not chat_response.choices:
            raise ValueError("No response from the AI model.")

        recommendation = chat_response.choices[0].message.content
        return recommendation

    except Exception as e:
        raise Exception(f"Error in recommend_anime_by_preferences: {e}")

async def get_popular_anime():
    url = ("https://api.myanimelist.net/v2/anime/ranking"
            "?ranking_type=bypopularity&limit=500"
            "&fields=mean,start_date,end_date,synopsis,num_episodes,"
            "status,average_episode_duration,genres,studios,main_picture")
    
    headers = {"X-MAL-CLIENT-ID": MAL_CLIENT_ID}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("data", [])
            return None

async def get_airing_anime():
    url = ("https://api.myanimelist.net/v2/anime/ranking"
           "?ranking_type=airing&limit=500"
           "&fields=mean,start_date,end_date,synopsis,num_episodes,"
           "status,average_episode_duration,genres,studios,main_picture")
    
    headers = {"X-MAL-CLIENT-ID": MAL_CLIENT_ID}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("data", [])
            return None

async def get_anime_by_season(year: int, season: str):
    url = (f"https://api.myanimelist.net/v2/anime/season/{year}/{season}"
           "?limit=500"
           "&fields=mean,start_date,end_date,synopsis,num_episodes,"
           "status,average_episode_duration,genres,studios,main_picture")
    
    headers = {"X-MAL-CLIENT-ID": MAL_CLIENT_ID}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("data", [])
            return None