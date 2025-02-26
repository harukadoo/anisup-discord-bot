#----------------Класи для роботи з аніме---------------

class Anime:
    def __init__(self, title: str, year: int, genres: list, rating: float, description: str = "", image_url: str = ""):
        self.title = title
        self.year = year
        self.genres = genres
        self.rating = rating
        self.description = description
        self.image_url = image_url

    def __str__(self) -> str:
        genres_str = ", ".join(self.genres) if self.genres else "Unknown genres"
        return f"**{self.title} ({self.year})**\nGenres: {genres_str}\nRating: {self.rating}/10\n{self.description}"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "year": self.year,
            "genres": self.genres,
            "rating": self.rating,
            "description": self.description,
            "image_url": self.image_url
        }

