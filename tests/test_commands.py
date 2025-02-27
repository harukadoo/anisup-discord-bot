import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from bot import bot

@pytest_asyncio.fixture
async def test_bot():
    bot._connection = AsyncMock()
    bot.http = AsyncMock() 
    return bot

@pytest.mark.asyncio
async def test_start_command(test_bot):
    ctx = AsyncMock()
    await test_bot.get_command("start").callback(test_bot, ctx)
    ctx.send.assert_called_with("Hello! I'm an anime bot. How can I help?")

@pytest.mark.asyncio
async def test_help_command(test_bot):
    ctx = AsyncMock()
    await test_bot.get_command("help").callback(test_bot, ctx)
    ctx.send.assert_called()

@pytest.mark.asyncio
async def test_top_anime_command(test_bot, monkeypatch):
    mock_response = [{"title": "Attack on Titan", "url": "https://example.com/aot"}]
    mock_api_call = AsyncMock(return_value=mock_response)
    monkeypatch.setattr("bot.get_top_anime", mock_api_call)

    ctx = AsyncMock()
    await test_bot.get_command("top-anime").callback(test_bot, ctx)
    ctx.send.assert_called_with("1. Attack on Titan - [Ссылка](https://example.com/aot)")

@pytest.mark.asyncio
async def test_airing_anime_command(test_bot, monkeypatch):
    mock_response = [{"title": "Jujutsu Kaisen", "url": "https://example.com/jjk"}]
    mock_api_call = AsyncMock(return_value=mock_response)
    monkeypatch.setattr("bot.get_airing_anime", mock_api_call)

    ctx = AsyncMock()
    await test_bot.get_command("airing-anime").callback(test_bot, ctx)
    ctx.send.assert_called_with("1. Jujutsu Kaisen - [Ссылка](https://example.com/jjk)")

@pytest.mark.asyncio
async def test_seasonal_anime_command(test_bot, monkeypatch):
    mock_response = [{"title": "Solo Leveling", "url": "https://example.com/sl"}]
    mock_api_call = AsyncMock(return_value=mock_response)
    monkeypatch.setattr("bot.get_seasonal_anime", mock_api_call)

    ctx = AsyncMock()
    await test_bot.get_command("seasonal-anime").callback(test_bot, ctx)
    ctx.send.assert_called_with("1. Solo Leveling - [Ссылка](https://example.com/sl)")

@pytest.mark.asyncio
async def test_find_anime_command(test_bot, monkeypatch):
    mock_response = [{"title": "Naruto", "url": "https://example.com/naruto"}]
    mock_api_call = AsyncMock(return_value=mock_response)
    monkeypatch.setattr("bot.find_anime_by_description", mock_api_call)

    ctx = AsyncMock()
    await test_bot.get_command("find-anime").callback(test_bot, ctx, "ninja")
    ctx.send.assert_called_with("1. Naruto - [Ссылка](https://example.com/naruto)")

@pytest.mark.asyncio
async def test_recommend_anime_command(test_bot, monkeypatch):
    mock_response = [{"title": "Death Note", "url": "https://example.com/dn"}]
    mock_api_call = AsyncMock(return_value=mock_response)
    monkeypatch.setattr("bot.recommend_anime", mock_api_call)

    ctx = AsyncMock()
    await test_bot.get_command("recommend").callback(test_bot, ctx, "psychological")
    ctx.send.assert_called_with("1. Death Note - [Ссылка](https://example.com/dn)")