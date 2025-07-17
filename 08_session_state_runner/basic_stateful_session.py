import uuid
import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent.agent import question_answering_agent

load_dotenv()

async def main():
    # create a new session service to store state
    session_service_stateful = InMemorySessionService()

    initial_state = {
        "user_name" : "Manideep Bangaru",
        "user_preferences" : """
        I like to play table tennis and I like to read books.
        My Favorite food is Biryani.
        My Favorite TV show is Game of Thrones.
        I'm also trying to get in to fitness recently.
        """
            }

    # Create a New session
    APP_NAME = "Manideep Bangaru"
    USER_ID = "manideep_bangaru"
    SESSION_ID = str(uuid.uuid4())

    stateful_session = await session_service_stateful.create_session(
        app_name = APP_NAME,
        user_id = USER_ID,
        session_id = SESSION_ID,
        state = initial_state,
    )
    print("Created a new session with ID: ", SESSION_ID)

    # Create a Runner
    runner = Runner(
        agent = question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )

    new_message = types.Content(
        role = "user", 
        parts = [types.Part(text = "What is Manideep's recent activity?")]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id = SESSION_ID,
        new_message=new_message
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print("Final Response: ", {event.content.parts[0].text})

    print("========= Session Event Explorations ==========")
    session = await session_service_stateful.get_session(
        app_name = APP_NAME,
        user_id = USER_ID,
        session_id = SESSION_ID,
    )

    # Log final session state
    print("========= Final Session state ==========")
    for key, value in session.state.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    asyncio.run(main())