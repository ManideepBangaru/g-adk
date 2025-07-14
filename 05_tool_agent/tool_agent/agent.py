import os
from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

AGENT_MODEL = os.getenv("GEMINI_MODEL")

def get_current_time() -> dict:
    """
    Get the current time in the format of dd/mm/yyyy hh:mm:ss
    """
    return {
        "Current Time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

root_agent = Agent(
    name="tool_agent",
    model=AGENT_MODEL,
    description="Agent to answer questions using Google Search.",
    instruction="""Your are an helpful agent that have access to below tools: 
                   - google_search: to search the web for information""",
    # tools = [google_search],
    tools = [get_current_time]
)