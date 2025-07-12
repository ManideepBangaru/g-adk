import os
from google.adk.agents import Agent

AGENT_MODEL = os.getenv("GEMINI_MODEL")

root_agent = Agent(
    name="greeting_agent",
    model=AGENT_MODEL,
    description="A helpful assistant that greets the user",
    instruction="""You are a helpful assistant that greets the user.
                   Ask for User's Name and greet them by name. """,
)