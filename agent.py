"""
Weather Voice Assistant Agent
=============================
A voice-controlled weather assistant built with LiveKit Agents Framework.

This agent:
- Listens to user voice queries via LiveKit
- Uses OpenAI GPT-4o-mini for natural language understanding
- Fetches real-time weather data from OpenWeatherMap API
- Responds with natural voice using Cartesia TTS

Author: Krishnansh
Assignment: Vaiu AI Software Developer Internship
"""

from dotenv import load_dotenv
import logging

from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent
from livekit.agents.llm import function_tool

# Import weather functions from weather_api module
from weather_api import get_current_weather, get_weather_forecast

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger("weather-agent")


class WeatherAgent(Agent):
    """
    Voice agent that provides weather information for any city.
    
    Features:
    - Current weather lookup via get_weather()
    - Tomorrow's forecast via get_forecast()
    - Natural conversational responses
    """
    
    def __init__(self) -> None:
        """Initialize the weather agent with system instructions."""
        super().__init__(
            instructions="""You are a weather assistant. Be brief and natural.
            
            RULES:
            - Use get_weather for current weather questions
            - Use get_forecast for tomorrow/future weather questions
            - ALWAYS use the tools, never make up data
            - Keep responses SHORT (1-2 sentences max)
            - NO emojis
            - Sound natural, like: "It's 25°C and sunny in Mumbai. Great day!"
            """
        )
    
    @function_tool
    async def get_weather(self, city: str) -> str:
        """
        Fetches CURRENT weather for a city.
        Use for questions about current conditions.
        
        Args:
            city: Name of the city (e.g., "Mumbai", "Delhi")
        """
        return await get_current_weather(city)

    @function_tool
    async def get_forecast(self, city: str) -> str:
        """
        Fetches TOMORROW's weather forecast.
        Use for questions about future weather or rain chances.
        
        Args:
            city: Name of the city (e.g., "Mumbai", "Pune")
        """
        return await get_weather_forecast(city)


# Initialize the LiveKit Agent Server
server = AgentServer()


@server.rtc_session()
async def handler(ctx: agents.JobContext):
    """
    Handles incoming WebRTC sessions from LiveKit.
    Sets up STT, LLM, and TTS pipeline.
    """
    logger.info(f"Starting session in room: {ctx.room.name}")

    session = AgentSession(
        stt="assemblyai/universal-streaming:en",  # Speech-to-text
        llm="openai/gpt-4o-mini",                 # Language model
        tts="cartesia/sonic-3",                   # Text-to-speech
    )

    await session.start(
        room=ctx.room,
        agent=WeatherAgent(),
    )

    await session.generate_reply(
        instructions="Greet the user briefly and say you can help with weather info."
    )


if __name__ == "__main__":
    agents.cli.run_app(server)
