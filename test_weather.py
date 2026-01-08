"""
Test script for Weather API
Tests both current weather and forecast endpoints.
"""
import asyncio
from dotenv import load_dotenv

load_dotenv()

from weather_api import get_current_weather, get_weather_forecast


async def main():
    print("=" * 50)
    print("WEATHER API TEST")
    print("=" * 50)
    
    # Test current weather
    print("\n--- Mumbai (Current) ---")
    print(await get_current_weather("Mumbai"))
    
    print("\n--- Bangalore (Current) ---")
    print(await get_current_weather("Bangalore"))
    
    # Test forecast
    print("\n--- Pune (Tomorrow) ---")
    print(await get_weather_forecast("Pune"))
    
    print("\n--- Delhi (Tomorrow) ---")
    print(await get_weather_forecast("Delhi"))
    
    # Test error handling
    print("\n--- Invalid City ---")
    print(await get_current_weather("InvalidCity123"))
    
    print("\n--- Empty City ---")
    print(await get_current_weather(""))
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
