import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model = "gemini/gemini-2.0-flash",
    api_key = os.getenv("GOOGLE_API_KEY"),
)

def dad_joke_agent():
    """
    Get a random dad joke
    """
    jokes = [
        "Why did the chicken cross the road? To get to the other side",
        "What do you call a fish with no eyes? A fsh",
        "what do you call a belt made of watches? A waist of time",
    ]
    return {
        "dad_joke": random.choice(jokes)
    }

root_agent = Agent(
    name = "dad_joke_agent",
    model = model,
    description = "Dad joke agent",
    instruction = """
You are a helpful assistant that tells dad jokes.
only use the tools `dad_joke_agent` to tell dad jokes.
""",
    tools = [dad_joke_agent],
)