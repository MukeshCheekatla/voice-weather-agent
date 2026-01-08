import os
from dotenv import load_dotenv
from livekit import api

load_dotenv()

api_key = os.getenv("LIVEKIT_API_KEY")
api_secret = os.getenv("LIVEKIT_API_SECRET")

# Create a token
token = api.AccessToken(api_key, api_secret) \
    .with_identity("human-tester") \
    .with_name("Human Tester") \
    .with_grants(api.VideoGrants(room_join=True, room="weather-room")) \
    .to_jwt()

print(token)
