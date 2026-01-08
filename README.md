🌤️ Voice Weather Assistant

A voice-controlled weather assistant built with **LiveKit Agents Framework** for the Vaiu AI Software Developer Internship Assignment.

## Features

- **Voice Interaction**: Speak naturally to get weather information
- **Real-time Weather**: Current conditions from OpenWeatherMap
- **Forecasts**: Tomorrow's weather with rain probability
- **Natural Responses**: Brief, conversational replies
- **Error Handling**: Gracefully handles invalid cities and API failures

## Example Interactions

```
User: "What's the weather in Mumbai?"
Agent: "It's 26°C and clear sky in Mumbai."

User: "How about Bangalore?"
Agent: "It's 23°C with broken clouds in Bangalore."

User: "Will it rain in Pune tomorrow?"
Agent: "Tomorrow in Pune, around 22°C with 30% chance of rain."
```

## Architecture

```
┌─────────────┐     ┌─────────┐     ┌────────────┐     ┌─────────┐
│ User Voice  │────▶│ LiveKit │────▶│ GPT-4o-mini│────▶│ Cartesia│
│   (Mic)     │     │   STT   │     │    LLM     │     │   TTS   │
└─────────────┘     └─────────┘     └──────┬─────┘     └─────────┘
                                           │
                                    ┌──────▼──────┐
                                    │ Weather API │
                                    │(OpenWeather)│
                                    └─────────────┘
```

## Prerequisites

- Python 3.9+
- LiveKit Cloud account ([sign up free](https://cloud.livekit.io))
- OpenWeatherMap API key ([get free](https://openweathermap.org/api))
- OpenAI API key

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/MukeshCheekatla/voice-weather-agent
cd voice-weather-agent

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file:

```env
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
OPENWEATHER_KEY=your_openweathermap_key
OPENAI_API_KEY=your_openai_key
```

### 3. Run the Agent

```bash
python agent.py dev
```

### 4. Test

Connect via [LiveKit Agents Playground](https://agents-playground.livekit.io/) or your own frontend.

## Project Structure

```
voice-weather-agent/
├── agent.py          # Main agent entry point
├── weather_api.py    # Core weather API functions
├── test_weather.py   # API integration tests
├── generate_token.py # LiveKit token generator
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (not committed)
└── README.md         # This file
```

## How It Works

1. **Voice Input**: User speaks → AssemblyAI transcribes to text
2. **Understanding**: GPT-4o-mini interprets the query
3. **Function Calling**: LLM calls `get_weather()` or `get_forecast()` 
4. **API Request**: Functions fetch real data from OpenWeatherMap
5. **Response**: LLM formats a natural response
6. **Voice Output**: Cartesia TTS speaks the response

## Key Functions

### `get_weather(city: str) -> str`
Fetches current weather conditions including temperature and description.

### `get_forecast(city: str) -> str`
Fetches tomorrow's forecast including temperature and rain probability.

## Error Handling

| Scenario | Response |
|----------|----------|
| City not found | "City 'xyz' not found. Please check the spelling." |
| API unavailable | "Weather service temporarily unavailable." |
| No city provided | "Please provide a city name." |

## Tech Stack

- **Framework**: LiveKit Agents 1.3.x
- **LLM**: OpenAI GPT-4o-mini
- **STT**: AssemblyAI
- **TTS**: Cartesia Sonic-3
- **Weather API**: OpenWeatherMap

## Testing

```bash
# Test weather API independently
python test_weather.py
```

## License

MIT

---

Built for Vaiu AI Software Developer Internship Assignment
