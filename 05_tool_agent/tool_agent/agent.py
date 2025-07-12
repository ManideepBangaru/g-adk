import os
from google.adk.agents import Agent
from google.adk.tools import google_search

AGENT_MODEL = os.getenv("GEMINI_MODEL")

root_agent = Agent(
    name="tool_agent",
    model=AGENT_MODEL,
    description="Agent to answer questions using Google Search.",
    instruction="""Your are an helpful agent that have access to below tools: 
                   - google_search: to search the web for information""",
    tools=[google_search],
)