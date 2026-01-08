"""
Weather API Module
==================
Core weather functions used by the voice agent.
Integrates with OpenWeatherMap API for real-time data.

Author: Krishnansh
"""

import os
import aiohttp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenWeatherMap API key - get free at https://openweathermap.org/api
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")


async def get_current_weather(city: str) -> str:
    """
    Fetches current weather for a city from OpenWeatherMap.
    
    Args:
        city: Name of the city (e.g., "Mumbai", "Delhi")
        
    Returns:
        Formatted weather string with temperature and conditions
    """
    if not city:
        return "Please provide a city name."

    if not OPENWEATHER_KEY:
        return "Weather service is not configured."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 404:
                    return f"City '{city}' not found. Please check the spelling."

                if resp.status != 200:
                    return "Weather service temporarily unavailable."

                data = await resp.json()
                temp = round(data["main"]["temp"])
                desc = data["weather"][0]["description"]
                
                return f"{city.title()}: {temp}°C, {desc}."
                    
    except Exception:
        return "Failed to fetch weather data."


async def get_weather_forecast(city: str) -> str:
    """
    Fetches tomorrow's weather forecast for a city.
    
    Args:
        city: Name of the city (e.g., "Mumbai", "Pune")
        
    Returns:
        Forecast with temperature and rain probability
    """
    if not city:
        return "Please provide a city name."

    if not OPENWEATHER_KEY:
        return "Weather service is not configured."

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHER_KEY}&units=metric&cnt=8"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 404:
                    return f"City '{city}' not found. Please check the spelling."

                if resp.status != 200:
                    return "Weather service temporarily unavailable."

                data = await resp.json()
                forecasts = data.get("list", [])
                
                if not forecasts:
                    return "No forecast data available."
                
                tomorrow_data = forecasts[4:8] if len(forecasts) >= 8 else forecasts
                
                temps = [f["main"]["temp"] for f in tomorrow_data]
                avg_temp = round(sum(temps) / len(temps), 1)
                
                rain_chance = 0
                for f in tomorrow_data:
                    if "pop" in f:
                        rain_chance = max(rain_chance, int(f["pop"] * 100))
                
                desc = tomorrow_data[0]["weather"][0]["description"]
                
                return (
                    f"Tomorrow in {city.title()}: around {avg_temp}°C with {desc}. "
                    f"Rain probability: {rain_chance}%."
                )
                    
    except Exception:
        return "Failed to fetch forecast data."
