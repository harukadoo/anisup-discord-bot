# Dokumentacja dla Discord Bota o Anime
## Opis projektu
### 1. Cel projektu
Celem projektu jest stworzenie bota na Discord, który zapewnia użytkownikom wygodny dostęp do informacji o anime. Bot umożliwia:

- Otrzymywanie list popularnych i aktualnie emitowanych anime.

- Wyszukiwanie anime według sezonu i roku.

- Znajdowanie tytułu anime na podstawie opisu.

- Otrzymywanie spersonalizowanych rekomendacji na podstawie preferencji użytkownika.

### 2. Zadania projektu
- Integracja z API MyAnimeList w celu uzyskania aktualnych danych o anime.

- Wykorzystanie Mistral AI do przetwarzania zapytań tekstowych (wyszukiwanie na podstawie opisu i rekomendacje).

- Implementacja interaktywnego interfejsu w Discord z wykorzystaniem przycisków i komend.

- Zapewnienie wygodnej nawigacji po listach anime z paginacją.

### 3. Oczekiwane rezultaty
- Użytkownicy będą mogli szybko znajdować informacje o anime, w tym oceny, opisy, gatunki i studia.

- Bot pomoże użytkownikom przypomnieć sobie tytuł anime na podstawie opisu.

- Użytkownicy otrzymają spersonalizowane rekomendacje, co ułatwi wybór nowego anime do obejrzenia.

- Bot będzie wspierał interaktywne interakcje, co zwiększy wygodę użytkowania.

## Główne funkcje
- Otrzymywanie listy popularnych anime.
Bot może wyświetlić top-10 popularnych anime na podstawie rankingu MyAnimeList.

- Otrzymywanie listy aktualnie emitowanych anime.
Bot pokazuje top-10 anime, które są obecnie emitowane.

- Wyszukiwanie anime według sezonu.
Bot może wyświetlić listę anime, które zostały wydane w określonym sezonie (zima, wiosna, lato, jesień) i roku.

- Wyszukiwanie anime na podstawie opisu.
Jeśli użytkownik zapomniał tytułu anime, ale pamięta jego opis, bot może pomóc znaleźć tytuł za pomocą Mistral AI.

- Rekomendacje anime.
Bot może zarekomendować anime na podstawie preferencji użytkownika (np. gatunek, tematyka, styl).

- Dodatkowe informacje o anime.
Dla każdego anime z listy można uzyskać szczegółowe informacje: ocenę, liczbę odcinków, gatunki, studia, daty wydania i opis.

## Funkcjonalności

### /start
- **Opis**: Wyświetla wiadomość powitalną.
- **Funkcjonalność**: Po wpisaniu komendy bot odpowiada wiadomością powitalną, informując użytkownika o dostępnych komendach i funkcjonalności bota.

### /help
- **Opis**: Wyświetla listę dostępnych komend.
- **Funkcjonalność**: Bot wysyła wiadomość z listą dostępnych komend i ich opisami, pomagając użytkownikowi w nawigacji po funkcjach.

### /top-anime
- **Opis**: Wyświetla 10 najpopularniejszych anime.
- **Funkcjonalność**: Pobiera dane z API MyAnimeList i prezentuje top-10 anime w rankingu popularności. Użytkownik może kliknąć przycisk, aby zobaczyć więcej szczegółów.

### /airing-anime
- **Opis**: Wyświetla 10 anime, które są obecnie emitowane.
- **Funkcjonalność**: Pokazuje top-10 anime, które są w trakcie emisji, z danymi o premierach, ocenach i linkiem do MyAnimeList.

### /seasonal-anime
- **Opis**: Wyświetla anime wydane w danym sezonie (zima, wiosna, lato, jesień) i roku.
- **Funkcjonalność**: Użytkownik wybiera rok oraz sezon, a bot wyświetla anime z danego okresu.

### /find-anime
- **Opis**: Znajduje anime na podstawie opisu.
- **Funkcjonalność**: Jeśli użytkownik nie pamięta tytułu anime, ale zna jego opis, bot pomoże w jego znalezieniu.

### /recommend
- **Opis**: Rekomendacje anime na podstawie preferencji użytkownika.
- **Funkcjonalność**: Użytkownik podaje preferencje dotyczące gatunku, tematyki lub stylu anime, a bot generuje rekomendacje.

### /more
- **Opis**: Wyświetla kolejne 10 anime z listy.
- **Funkcjonalność**: Umożliwia przejście do kolejnej strony z listą anime.

## Obsługa błędów

Bot posiada mechanizmy obsługi błędów:
- **TimeoutError**: Jeśli API nie odpowiada w ciągu określonego czasu, użytkownik otrzymuje komunikat o błędzie.
- **ValueError**: W przypadku nieprawidłowego opisu lub preferencji bot informuje użytkownika o konieczności poprawienia danych.

## Technologie

- **Python**: Język programowania do tworzenia bota.
- **discord.py**: Biblioteka do interakcji z Discord API.
- **python-dotenv**: Do zarządzania zmiennymi środowiskowymi, takimi jak token bota.
- **aiohttp**: Biblioteka do obsługi asynchronicznych żądań HTTP.
- **requests**: Biblioteka do wykonywania zapytań HTTP.
- **mistralai**: Sztuczna inteligencja do rozpoznawania anime na podstawie opisu.

## Instalacja

1. Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt

