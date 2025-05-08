# Documentation for Discord Anime Bot
## Project Description
### 1. Project Goal
The goal of the project is to create a Discord bot that provides users with convenient access to anime information. The bot allows:

- Receiving lists of popular and currently airing anime.

- Searching for anime by season and year.

- Finding the title of an anime based on its description.

- Getting personalized recommendations based on user preferences.

### 2. Project Tasks
- Integration with the MyAnimeList API to obtain up-to-date anime data.

- Using Mistral AI to process text queries (description-based search and recommendations).

- Implementation of an interactive interface in Discord using buttons and commands.

- Providing easy navigation through anime lists with pagination.

### 3. Expected Results
- Users will be able to quickly find information about anime, including ratings, descriptions, genres, and studios.

- The bot will help users remember the title of an anime based on its description.

- Users will receive personalized recommendations, making it easier to choose a new anime to watch.

- The bot will support interactive interactions, enhancing the user experience.

## Main Features
- Receiving a list of popular anime
The bot can display the top 10 most popular anime based on the MyAnimeList ranking.

- Receiving a list of currently airing anime
The bot shows the top 10 anime that are currently airing.

- Searching anime by season
The bot can display a list of anime released in a specific season (winter, spring, summer, fall) and year.

- Searching anime based on description
If a user forgets the anime title but remembers the description, the bot can help find the title using Mistral AI.

- Anime recommendations
The bot can recommend anime based on the user's preferences (e.g., genre, theme, style).

- Additional information about anime
For each anime in the list, you can get detailed information: rating, number of episodes, genres, studios, release dates, and description.

## Functionalities

### /start
Description: Displays a welcome message.

Functionality: Upon entering the command, the bot responds with a welcome message informing the user about the available commands and bot features.

### /help
Description: Displays a list of available commands.

Functionality: The bot sends a message with a list of commands and their descriptions to help the user navigate the features.

### /top-anime
Description: Displays the top 10 most popular anime.

Functionality: Retrieves data from the MyAnimeList API and presents the top 10 anime in the popularity ranking. The user can click a button to view more details.

### /airing-anime
Description: Displays 10 anime that are currently airing.

Functionality: Shows the top 10 anime currently airing, with data about premieres, ratings, and a link to MyAnimeList.

### /seasonal-anime
Description: Displays anime released in a given season (winter, spring, summer, fall) and year.

Functionality: The user selects the year and season, and the bot displays anime from that period.

### /find-anime
Description: Finds anime based on a description.

Functionality: If the user doesn’t remember the title but knows the description, the bot helps find it.

### /recommend
Description: Anime recommendations based on user preferences.

Functionality: The user provides preferences regarding genre, theme, or style, and the bot generates recommendations.

### /more
Description: Displays the next 10 anime from the list.

Functionality: Allows navigating to the next page of the anime list.

## Error Handling
The bot has error handling mechanisms:

- TimeoutError: If the API does not respond within a certain time, the user receives an error message.

- ValueError: In case of an invalid description or preferences, the bot informs the user that the input needs to be corrected.

## Technologies
- Python: Programming language used to build the bot.

- discord.py: Library for interacting with the Discord API.

- python-dotenv: For managing environment variables such as the bot token.

- aiohttp: Library for handling asynchronous HTTP requests.

- requests: Library for making HTTP requests.

- mistralai: AI for recognizing anime based on description.

## Installation
Install the required libraries:

```bash
pip install -r requirements.txt

