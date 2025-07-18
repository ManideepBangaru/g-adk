from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

def add_reminder(reminder : str, tool_context : ToolContext) -> dict:
    """
    Add a new reminder to the user's reminder list.

    Args:
        reminder: The reminder text to add
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool : add_reminder called for '{reminder}' ---")

    # Get current reminders from state
    reminders = tool_context.state.get("reminders", [])

    # Add the new reminder
    reminders.append(reminder)

    # update state with the new list of reminders
    tool_context.state["reminders"] = reminders

    return {
        "action" : "add_reminder",
        "reminder" : reminder,
        "message" : f"Added reminder: {reminder}",
    }

def view_reminders(tool_context : ToolContext) -> dict:
    """
    View all current reminders.

    Args:
        tool_context: Context for accessing session state

    Returns:
        The list of reminders
    """
    print("--- Tool : view_reminders called ---")

    # Get reminders from state
    reminders = tool_context.state.get("reminders", [])

    return {
        "action" : "view_reminders",
        "reminders" : reminders,
        "count" : len(reminders),
    }