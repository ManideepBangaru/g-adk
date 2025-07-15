import os
from google.adk.agents import Agent

question_answering_agent = Agent(
    name="question_answering_agent",
    model=os.getenv("GEMINI_MODEL"),
    description="Question and answering agent",
    instruction="""
You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
"""
)