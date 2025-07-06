from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    # A unique name for the agent
    name = "basic_search_agent",
    model = "gemini-2.0-flash",
    # A description of the agent's purpose
    description = "Agent to answer questions using Google Search.",
    # Instructions to set the agent's behavior
    Instruction = "You are an expert researcher. You always stick to the facts.",
    # A list of tools that the agent can use
    tools = [google_search],
)